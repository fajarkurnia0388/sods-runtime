import sys
import os

# Add the src directory to PYTHONPATH so we can import sods
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sods.sandbox import SODSSandbox

def generic_json_parse(json_string):
    """
    A generic JSON parser that can accept any string.
    In real-world applications, this represents a target function we want to optimize.
    """
    import json
    return json.loads(json_string)

def impure_json_log(json_string):
    """
    A function that parses JSON but also writes to stdout/logs (I/O side effect).
    """
    import json
    parsed = json.loads(json_string)
    # Impure side effect: writing to standard output
    print(f"  [I/O LOG] Parsed JSON with keys: {list(parsed.keys())}")
    return parsed

def main():
    import io
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding='utf-8', errors='replace'
        )

    print("=" * 72)
    print(" 🚀 SODS DEMO: JSON PARSING".center(72))
    print("=" * 72)
    
    sandbox = SODSSandbox(reset_cache=True)
    
    print("\n[Tahap 1] Melakukan observasi (Cold Run) untuk pure function...")
    workload = [
        ('{"key": "value", "number": 1}',),
        ('{"message": "hello world"}',),
        ('{"status": "success", "code": 200}',)
    ]
    
    # cold_run signature: cold_run(fn_name, fn, workloads)
    sandbox.cold_run("generic_json_parse", generic_json_parse, workload)
    sandbox.save_cookie()
        
    print("\n[Tahap 2] Melakukan observasi (Cold Run) untuk impure function (WASI)...")
    workload_impure = [
        ('{"event": "login", "user": "alice"}',),
        ('{"event": "logout", "user": "bob"}',),
    ]
    # Mengamati fungsi dengan efek samping I/O (is_io_side_effect=True)
    sandbox.cold_run("impure_json_log", impure_json_log, workload_impure, is_io_side_effect=True)
    
    print("\n[Tahap 3] Eksekusi Cepat (Warm Run) - Pure Function...")
    results, deopts = sandbox.warm_run("generic_json_parse", generic_json_parse, [('{"status": "success"}',)])
    print(f" Hasil    : {results[0]}")
    print(f" Deopt OSR: {deopts}x")
    
    print("\n[Tahap 4] Eksekusi Cepat (Warm Run) - Impure Function (WASI Passthrough)...")
    results_wasi, deopts_wasi = sandbox.warm_run("impure_json_log", impure_json_log, [('{"event": "click"}',)])
    print(f" Hasil    : {results_wasi[0]}")
    print(f" Deopt OSR: {deopts_wasi}x (Tidak ada deopt karena bypass WASI/I/O aktif)")
    
    print("\n✨ Demo Selesai. Profile tersimpan di direktori .sods/")

if __name__ == "__main__":
    main()
