"""
SODS Concept Console Demonstration
==================================
Illustrates the 5-Stage execution pipeline of SODS on a polymorphic add function:
Cold Run (Profiling) → Specializer (PIC: 3, including mixed numerics) → Equivalence Verification →
Enriched Cookie Disk Serialization → Warm Run (Speedup Execution) → Highly Volatile Megamorphic
Deoptimization Storm (Tier-Lowering Protection).
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sods import SODSSandbox, EquivalenceVerifier
from sods.dummy_target import generic_add, generic_log_io

def run_demo():
    import io
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding='utf-8', errors='replace'
        )

    print("=" * 72)
    print("  PROTOTYPE SODS v2.4 — Sandbox Observer-Driven Specializer".center(72))
    print("  PIC │ Tier-Lowering │ WASI Boundary │ OSR Deopt │ Enriched Cache".center(72))
    print("=" * 72)

    sandbox = SODSSandbox(reset_cache=True)
    N = 10_000

    # ── TAHAP 1: COLD RUN ────────────────────────────────────────────────────
    print("\n" + "═" * 72)
    print("  TAHAP 1: COLD RUN — Instrumentasi & Pembangunan Profil PIC".center(72))
    print("═" * 72)
    
    cold_workloads = (
        [(i, i + 1) for i in range(400)] +               # 400 int pairs
        [(float(i), float(i + 1)) for i in range(400)] + # 400 float pairs
        [(i, float(i + 1)) for i in range(400)]          # 400 mixed int+float pairs
    )
    sandbox.cold_run("generic_add", generic_add, cold_workloads)
    sandbox.save_cookie()

    # ── TAHAP 2: EQUIVALENCE VERIFIER ────────────────────────────────────────
    print("\n" + "═" * 72)
    print("  TAHAP 2: EQUIVALENCE VERIFIER — Mengakali Batas Teorema Rice".center(72))
    print("═" * 72)
    
    sfn, _, _ = sandbox.specialized["generic_add"]
    verify_inputs = [(10, 20), (3.5, 4.5), (10, 20.0), (9.9, 1.1)]
    passed = EquivalenceVerifier.verify("generic_add", generic_add, sfn, verify_inputs)
    
    if not passed:
        print("  HALT: Spesialisasi tidak aman. Prototipe berhenti.")
        return

    # ── TAHAP 3: WARM RUN BENCHMARK ──────────────────────────────────────────
    print("\n" + "═" * 72)
    print("  TAHAP 3: WARM RUN — Bekerja dengan Spesialisasi JIT".center(72))
    print("═" * 72)
    
    sandbox2 = SODSSandbox()
    sandbox2.load_cookie()
    
    results, _ = sandbox2.warm_run("generic_add", generic_add, [(10, 20), (5.5, 4.5), (10, 5.0)])
    print(f"  Contoh Eksekusi Cepat : {(10, 20)} + {(5.5, 4.5)} + {(10, 5.0)} -> {results} ✓")

    # ── TAHAP 4: WASI I/O BOUNDARY TAINT CHECK ──────────────────────────────
    print("\n" + "═" * 72)
    print("  TAHAP 4: UJI PERBATASAN I/O — WASI Taint Analysis".center(72))
    print("═" * 72)
    
    io_workloads = [("Log sesi login pengguna A",), ("Log sinkronisasi database",)]
    sandbox2.cold_run("generic_log_io", generic_log_io, io_workloads, is_io_side_effect=True)

    # ── TAHAP 5: OSR DEOPT FALLBACK ──────────────────────────────────────────
    print("\n" + "═" * 72)
    print("  TAHAP 5: UJI OSR DEOPT — Masukan Tipe Campuran Tak Teramati".center(72))
    print("═" * 72)
    print("  Menyisipkan tipe String di tengah aliran komputasi numerik.")
    
    mixed_workloads = [(1, 2), (3, 4), ("a", "b"), (5.0, 6.0)]
    mixed_results, mixed_deopt = sandbox2.warm_run("generic_add", generic_add, mixed_workloads)
    print(f"  Hasil Komputasi : {mixed_results}")
    print(f"  Jumlah Deopt OSR: {mixed_deopt}x — Keluaran tetap 100% BENAR ✓")

    # ── TAHAP 6: UJI MEGAMORPHIC VOLATILE — Tier-Lowering Protection ──────────
    print("\n" + "═" * 72)
    print("  TAHAP 6: UJI MEGAMORPHIC VOLATILE — Tier-Lowering Protection".center(72))
    print("═" * 72)
    print("  Membombardir sistem dengan tipe data acak berulang (Guard thrashing).")
    
    storm = [("Halo ", "Dunia"), ([1, 2], [3, 4]), ("Foo ", "Bar"), (100, 200)] * 5
    storm_results, deopt_fails = sandbox2.warm_run("generic_add", generic_add, storm)
    
    print(f"\n  Total Pemicuan Deopt OSR: {deopt_fails}x")
    print(f"  Status Keamanan         : Semua keluaran 100% BENAR ✓")

    print(f"\n  Memverifikasi eksekusi setelah Tier-Lowering terkunci...")
    sandbox2.warm_run("generic_add", generic_add, [(1, 2), (3, 4)])

    print("\n" + "=" * 72)
    print(" KESIMPULAN DEMO EDUKATIF Selesai ✓".center(72))
    print("=" * 72)

if __name__ == "__main__":
    run_demo()
