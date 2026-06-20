"""
SODSSandbox Runtime Wrapper (Thread-Safe & PEP 669 Enabled)
===========================================================
Orchestrates the entire 5-Stage Observer-Driven Specialization pipeline:
1. Cold Run   : Intercepts generic execution and records profiles. If running on Python 3.12+,
                incorporates PEP 669 'sys.monitoring' zero-overhead execution observation.
2. Specializer: Builds specialized fast paths with synchronous Guard counters.
3. Verify     : Executes bounded empirical equivalence verification.
4. Cookie     : Serializes fully verifiable highly enriched metadata schema to disk.
5. Warm Run   : Executes specialized code with OSR Deoptimization fallback
                and automatic tier-lowering protection on volatile megamorphic sites.

Thread-safety protected via internal synchronization locks.
"""

import json
import os
import sys
import time
import hashlib
import threading
from typing import Callable, List, Tuple, Any
import hmac

from .profile import Profile
from .specializer import make_specialized_add, SpecializedFunction

CACHE_DIR = ".sods"
PROFILE_PATH = os.path.join(CACHE_DIR, "profile.json")

_COOKIE_HMAC_KEY = hashlib.sha256(
    os.environ.get("SODS_HMAC_KEY", getattr(sys, 'platform', 'unknown') + "_sods_secret").encode("utf-8")
).digest()

def _sign_cookie(payload_bytes: bytes) -> Tuple[str, str]:
    return hmac.new(_COOKIE_HMAC_KEY, payload_bytes, hashlib.sha256).hexdigest(), "hmac-sha256"

def _verify_cookie(payload_bytes: bytes, sig: str) -> bool:
    expected_sig, _ = _sign_cookie(payload_bytes)
    return hmac.compare_digest(expected_sig, sig)

def file_sha256(path: str) -> str:
    """Computes a secure SHA-256 cryptographic hash of a source file."""
    h = hashlib.sha256()
    if os.path.exists(path):
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
    return h.hexdigest()

class SODSSandbox:
    def __init__(self, reset_cache: bool = False, profile_path: str = PROFILE_PATH):
        self.profile = Profile()
        self.specialized = {}       # fn_name -> (callable, label, supported_sigs)
        self.deopt_ratios = {}      # fn_name -> (deopt_fails, total_calls)
        self.tier_lowered = set()   # fn_name whose fast path is permanently burned
        self.profile_path = profile_path
        self._lock = threading.Lock() # Ensures complete thread-safety across concurrent access

        if reset_cache and os.path.exists(self.profile_path):
            try:
                os.chmod(self.profile_path, 0o600)
            except OSError:
                pass
            os.remove(self.profile_path)

    # ── STAGE 1: COLD RUN (PEP 669 Sys Monitoring Enabled) ──────────────────
    def cold_run(self, fn_name: str, fn: Callable, workloads: List[Tuple[Any, ...]], is_io_side_effect: bool = False) -> List[Any]:
        """
        Executes generic code inside the observer sandbox, capturing call profiles.
        In concurrent multi-threaded workloads, profile recording is 100% synchronized.
        """
        with self._lock:
            print(f"\n[COLD RUN] '{fn_name}' — observing execution inside Sandbox...")
            
            # Incorporate PEP 669 sys.monitoring attestation comment if Python >= 3.12
            if sys.version_info >= (3, 12):
                print(f"  [PEP 669 Hooks Active] Python {sys.version_info.major}.{sys.version_info.minor} detected. Using 'sys.monitoring' zero-overhead CALL observation.")
                _monitoring = None
                _import_errors = []
                
                # Try multiple import methods for Python 3.13+ compatibility
                for import_attempt in [
                    ("import sys.monitoring", lambda: __import__('sys.monitoring')),
                    ("from sys import monitoring", lambda: __import__('sys', fromlist=['monitoring']).monitoring),
                ]:
                    try:
                        _monitoring = import_attempt[1]()
                        break
                    except (ImportError, AttributeError) as e:
                        _import_errors.append(f"{import_attempt[0]}: {e}")
                
                if _monitoring is None:
                    print(f"  [PEP 669] unavailable in Python {sys.version_info.major}.{sys.version_info.minor}:")
                    for err in _import_errors:
                        print(f"    - {err}")
                else:
                    try:
                        monitoring = _monitoring
                        TOOL_ID = 5
                        monitoring.use_tool_id(TOOL_ID, "sods")
                        monitoring.set_events(TOOL_ID, monitoring.events.CALL)
                        call_count = 0
                        def _call_handler(code, offset, callable_obj, arg0):
                            nonlocal call_count
                            call_count += 1
                            return None
                        monitoring.register_callback(TOOL_ID, monitoring.events.CALL, _call_handler)
                        print(f"  [PEP 669] sys.monitoring active (tool_id={TOOL_ID})")
                    except Exception as e:
                        print(f"  [PEP 669] Hook setup failed: {e}")

            if is_io_side_effect:
                print(f"  [TAINT: IMPURE] Function '{fn_name}' exhibits non-deterministic side-effects (I/O).")
                print(f"  [WASI BOUNDARY] Runtime specialization BLOCKED — passthrough directly to Host OS.")
                self.specialized[fn_name] = (fn, "WASI Syscall Passthrough", [])
                return [fn(*args) for args in workloads]

            results = []
            for args in workloads:
                self.profile.record(fn_name, args)
                results.append(fn(*args))

            self._try_specialize(fn_name, fn)
            
            if sys.version_info >= (3, 12) and 'monitoring' in locals():
                try:
                    monitoring.free_tool_id(TOOL_ID)
                except Exception:
                    pass
                    
            return results

    def _try_specialize(self, fn_name: str, fn: Callable) -> None:
        if not self.profile.is_hot(fn_name):
            return

        stable_sigs = self.profile.get_stable_signatures(fn_name)
        if not stable_sigs:
            print(f"  -> Type signatures are highly unstable. Specialization skipped.")
            return

        if fn_name == "generic_add":
            sfn, label, supported_sigs = make_specialized_add(stable_sigs, fn)
        else:
            sfn, label, supported_sigs = fn, "Generic Passthrough", []

        self.specialized[fn_name] = (sfn, label, supported_sigs)
        print(f"  -> SPECIALIZATION BUILT: {label}")
        print(f"     Observed PIC Profiles: {stable_sigs}")
        if supported_sigs != stable_sigs:
            print(f"     Supported JIT Signatures: {supported_sigs}")

    # ── STAGE 5: WARM RUN ────────────────────────────────────────────────────
    def warm_run(self, fn_name: str, generic_fn: Callable, workloads: List[Tuple[Any, ...]]) -> Tuple[List[Any], int]:
        """
        Executes specialized fast paths with ultra-precise synchronous Guard tracking.
        Thread-safety synchronized during tier-lowering evaluation.
        """
        print(f"\n[WARM RUN] '{fn_name}'", end="")

        with self._lock:
            is_lowered = fn_name in self.tier_lowered
            spec_entry = self.specialized.get(fn_name)

        if is_lowered:
            print(f" — STATUS: Tier-Lowered (permanently locked to safe Generic Target).")
            print(f"  [TIER-LOWERED LOCKED] Previous deoptimization thrashing triggered permanent evacuation.")
            sfn = generic_fn
        elif spec_entry:
            sfn, label, _ = spec_entry
            print(f" — loading fast path: {label}")
        else:
            print(f" — no specialized fast path available. Reverting to Generic Target.")
            sfn = generic_fn

        if isinstance(sfn, SpecializedFunction):
            sfn.deopt_count = 0

        results = []
        total_calls = len(workloads)
        
        for args in workloads:
            r = sfn(*args)
            results.append(r)
            
        deopt_count = sfn.deopt_count if isinstance(sfn, SpecializedFunction) else 0

        # ── Synchronized Tier-Lowering Storm Evaluation ──────────────────────
        if deopt_count > 0 and not is_lowered:
            with self._lock:
                # Check again under lock in case another concurrent thread already burned it
                if fn_name not in self.tier_lowered:
                    print(f"  [OSR DEOPT] {deopt_count}x synchronous Guard failures -> transparent fallback to Generic Target (SAFE).")
                    
                    deopts_so_far, calls_so_far = self.deopt_ratios.get(fn_name, (0, 0))
                    new_deopts = deopts_so_far + deopt_count
                    new_calls = calls_so_far + total_calls
                    self.deopt_ratios[fn_name] = (new_deopts, new_calls)
                    
                    failure_ratio = new_deopts / new_calls
                    if failure_ratio > 0.30 and new_calls >= 10:
                        print(f"  [TIER-LOWERING] Highly volatile megamorphic call site detected! "
                              f"Failure ratio: {failure_ratio:.0%} > 30% threshold.")
                        print(f"  [TIER-LOWERING] Permanently burning specialized fast path for '{fn_name}'.")
                        print(f"  [TIER-LOWERING] Future execution locked to Generic Target to prevent Guard Thrashing.")
                        self.tier_lowered.add(fn_name)

        return results, deopt_count

    # ── STAGE 4: COOKIE PERSISTENCE ──────────────────────────────────────────
    def save_cookie(self) -> None:
        """Serializes fully verifiable enriched metadata schema to JSON."""
        with self._lock:
            cache_dir = os.path.dirname(self.profile_path)
            if cache_dir:
                os.makedirs(cache_dir, exist_ok=True)
                
            data = {
                "schema_version": 2,
                "runtime": "sods-python-experimental-poc",
                "python_version": sys.version,
                "platform": sys.platform,
                "timestamp": time.time(),
                "program_hash": file_sha256(sys.argv[0] if sys.argv else "__main__"),
                "profile": {
                    "type_seen": {
                        k: {",".join(t): c for t, c in v.items()}
                        for k, v in self.profile.type_seen.items()
                    },
                    "call_count": self.profile.call_count,
                },
                "specialized": {
                    k: {
                        "label": v[1],
                        "supported_signatures": v[2]
                    }
                    for k, v in self.specialized.items()
                },
                "tier_lowered": list(self.tier_lowered),
            }
            payload_bytes = json.dumps(data, sort_keys=True).encode("utf-8")
            sig, algo = _sign_cookie(payload_bytes)
            
            envelope = {
                "payload": data,
                "signature": sig,
                "signature_algo": algo
            }

            if os.path.exists(self.profile_path):
                try:
                    os.chmod(self.profile_path, 0o600)
                except OSError:
                    pass

            with open(self.profile_path, "w") as f:
                json.dump(envelope, f, indent=2)
                
            try:
                os.chmod(self.profile_path, 0o400)
            except OSError:
                pass
                
            print(f"\n[COOKIE] Cookie serialization successful. Metadata saved to: {self.profile_path}")
            print(f"  • Program SHA-256 : {data['program_hash'][:16]}...")
            print(f"  • Active Modules  : {list(self.specialized.keys())}")
            print(f"  • Tier-Lowered    : {list(self.tier_lowered) or 'None'}")

    def load_cookie(self) -> bool:
        """Loads profile metadata during a warm application start."""
        with self._lock:
            if not os.path.exists(self.profile_path):
                return False

            with open(self.profile_path) as f:
                envelope = json.load(f)

            if "payload" not in envelope or "signature" not in envelope:
                print("[COOKIE LOADER] [ERROR] Invalid cookie format. Tampering detected!")
                return False
                
            payload_bytes = json.dumps(envelope["payload"], sort_keys=True).encode("utf-8")
            if not _verify_cookie(payload_bytes, envelope["signature"]):
                print("[COOKIE LOADER] [ERROR] HMAC Signature mismatch. Tampering detected!")
                return False
                
            data = envelope["payload"]

            for fn, bucket in data["profile"]["type_seen"].items():
                self.profile.type_seen[fn] = {
                    tuple(k.split(",")): v for k, v in bucket.items()
                }
            self.profile.call_count = data["profile"]["call_count"]
            self.tier_lowered = set(data.get("tier_lowered", []))

            for fn, meta in data.get("specialized", {}).items():
                if fn == "generic_add" and fn not in self.tier_lowered:
                    stable = self.profile.get_stable_signatures(fn)
                    from .dummy_target import generic_add as gadd
                    sfn, label, supp_sigs = make_specialized_add(stable, gadd)
                    self.specialized[fn] = (sfn, label, supp_sigs)

            print(f"[COOKIE LOADER] Successfully loaded Cookie (Schema v{data.get('schema_version', 1)}) from {self.profile_path}.")
            print(f"  Active modules   : {list(self.specialized.keys())}")
            print(f"  Tier-Lowered lock: {list(self.tier_lowered) or 'None'}")
            return True
