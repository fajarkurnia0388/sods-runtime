<div align="center">
  <h1>⚙️ SODS — Sandbox Observer-Driven Specializer</h1>
  <p><b>A Research Concept & Educational PoC for Observer-Driven Runtime Specialization</b></p>

[![Version](https://img.shields.io/badge/version-2.4.0%20(Research%20PoC)-58a6ff.svg)](./prototype_sods.py)
[![Theory](https://img.shields.io/badge/theory-Rice's%20Theorem%20Workaround-a371f7.svg)](./WHITEPAPER_EN.md)
[![Genesis](https://img.shields.io/badge/genesis-Di%20TeknoIn%20Inspiration-ffbd2e.svg)](./GENESIS_EN.md)
[![Speedup](https://img.shields.io/badge/speedup-3.25×_vs_generic_/_0.24×_vs_native-56d364.svg)](./benchmarks/bench_add.py)
[![Status](https://img.shields.io/badge/status-Educational_PoC_Python-yellow.svg)](#)
[![Tests](https://img.shields.io/badge/tests-9/9_(3.10--3.13)_passing-success.svg)](./tests/test_sods.py)
[![Vibe](https://img.shields.io/badge/vibe-Doom%20(1993)%20-Apple%20Task%20Manager%20Efficiency-f0883e.svg)](./GENESIS_EN.md)

</div>

---

> **🚀 Authors & Collaborative Research Attribution**
>
> - **Original Conceptual Design & Building of SODS:** Fajar Kurnia ([@fajarkurnia0388](https://github.com/fajarkurnia0388))
> - **Theory Elaborations & Agentic Instrumentation Assistant:** Arena.ai (Agent Mode)
> - **Release Date:** June 19, 2026

---

## 💡 What is SODS?

**SODS (*Sandbox Observer-Driven Specializer*)** is a conceptual runtime wrapper architecture at the Operating System level, designed to explore restoring the extreme computational efficiency of *Doom* (1993) and the original *Windows Task Manager* (1995) to bloated modern software (e.g., Electron, Node.js, or Python applications).

SODS starts with a fundamental theoretical question: *"Since Rice's Theorem (1953) mathematically forbids us from creating a universal, instant converter tool that guarantees 100% semantic equivalence for all infinite inputs ($\infty$), what if we build a runtime that observes execution behavior, specializes the binary ONLY for observed inputs, stores a persistent profile (like a cookie), and prepares an emergency escape hatch (OSR Deoptimization) when assumptions are violated?"*

This project models the philosophy of modern JIT compilers (*V8*, *PyPy*, *GraalVM*) and contemporary AI systems dynamic compilation techniques (such as *torch.compile* and *Apache TVM*) at the industrial level, packaging them into a roadmap for an *external OS-level wrapper converter*.

---

## ⚠️ Limitations & Disclaimer (Research PoC)

This project is purely an **Educational Python PoC** and not a *production runtime*. Please see [ROADMAP_STATUS.md](./ROADMAP_STATUS.md) for the reality matrix of capabilities that are *Implemented*, *Simulated*, or merely *Proposed Roadmap*.

## 🌟 The Massive Potential of SODS Tools (Why SODS Matters)

To help professionals at all levels understand the revolutionary impact of this research, we map out what would happen if the SODS Roadmap is realized as actual production tools (e.g., `sods-pack` or `ExoRuntime`):

### 🌱 1. For Beginners (*Junior Developers / Students*): "Making Lightweight Applications Without the Headache"

When beginners learn to build desktop applications using HTML/JS/Python, they often rely on frameworks like *Electron* or *PyQt*. However, they are often discouraged to see that a simple calculator app they built is **150 MB** in size and consumes **300 MB** of RAM.

- **Potential of the SODS Tool:** If the autonomous SODS converter tool becomes available, beginners only need to write the plain JS/Python code they are used to. The SODS tool will wrap, monitor, and magically specialize their app behind the scenes to be as fast and lightweight as a C binary. They can showcase smooth apps running on old laptops or cheap phones without having to learn complex C/Rust optimization techniques.

### ⚡ 2. For Web / Mobile Professionals (*Intermediate Frontend / Mobile Devs*): "Silicon-level Performance Without Rewriting Code"

Contemporary developers are frequently required to build heavy computation on the client-side (rendering 10,000 rows of data, canvas graphics, or local cryptography). Currently, the only way to get high performance is to learn **Rust** or **Zig** to compile to WebAssembly. For many teams, this steep learning curve slows down feature delivery velocity.

- **Potential of the SODS Tool:** Developers can simply keep their established **TypeScript** or **Python** codebases. The SODS Runtime Wrapper engine will intercept execution, trace *Hot Paths*, and emit raw Assembly/WASM instructions *on-the-fly*. Teams get **3×–5× speedups "for free"** without sacrificing feature delivery speed.

### 🏢 3. For Cloud Architects & Business Executives (*Senior Cloud/Backend Enterprise Architects*): "Cutting AWS / Cloud Server Bills by Millions"

At enterprise/unicorn scales, monolithic backend servers (Node.js, Python, Ruby) handle billions of requests per day. The overhead of dynamic languages forces corporations to spend large sums renting thousands of *Kubernetes pods* or *AWS EC2* instances with massive RAM and expensive CPUs.

- **Potential of the SODS Tool:** Instrumented at the *Container Hypervisor* level (like *Wasmtime Fuel Pods* or *eBPF Mesh*), every microservice will be empirically specialized as the server runs. Reducing the memory footprint by up to 70% and cutting CPU cycles means servers can handle **3× more traffic on the exact same hardware infrastructure**. Corporations save millions in cloud billing annually, increasing profit margins.

### 🌍 4. For Green Computing & Macro Ecosystems: "Saving Legacy Silicon and the Planet"

Millions of old laptops and smartphones are thrown into landfills every year as electronic waste (*e-waste*) simply because their silicon can no longer run modern operating systems and chat apps that consume large amounts of RAM.

- **Potential of the SODS Tool:** The autonomous SODS converter acts as a **Global Digital Accessibility Hero**. By streamlining software execution from the outside, it extends the lifespan of legacy hardware by 5–10 years, slows down the accumulation of *e-waste*, and lowers the carbon footprint of data centers worldwide.

---

## 🏛️ Modular Project Showcase

This repository presents a **Hybrid Research Design (*Design Science Research* & Qualitative Literature Review)** packaged into modular pillars:

### 1. 📜 [Technical Whitepaper, Research Notes & Genesis Transcript (`WHITEPAPER_EN.md`)](./WHITEPAPER_EN.md)

- **[Original Inspiration (`GENESIS_EN.md`):](./GENESIS_EN.md)** Records the transcript of the YouTube essay by **Di TeknoIn** (*Ketika Performance Bukan Prioritas Lagi*) that sparked the creation of this architecture.
- In-depth research paper formatted for the open-source ecosystem with transparent evidence stratification (**T1 Canonical Primary** to **T4 Forum Anecdote**).
- **Reality Gap Audit:** Explicitly separates the current Python PoC implementation from the true OS kernel JIT roadmap.
- **Section 5.6:** Outlines the mitigation map for 5 production obstacles via *Selective Taint Analysis (Mozilla `rr`)*, kernel interception without modifications (*eBPF* + *DynamoRIO*), *Hardware PMU Statistical Sampling (&lt;1% overhead)*, and *Timing Noise Randomization*.
- **PEP 669 Integration:** Analyzes the utilization of Python 3.12+ `sys.monitoring` as a zero-overhead silicon tracing bridge.

### 2. 💻 [Modular Software Package (`src/sods`)](./src/sods)

- **Polymorphic Inline Caches (PIC: 2–3):** Specializes comparison computations without fragile monomorphism, including support for mixed numerics (`int + float`).
- **WASI I/O Boundary:** Intercepts functions with I/O side effects using *Taint Analysis*.
- **Thread-Safety Locked:** Protected by `threading.Lock()` to handle concurrent execution in multithreaded or asyncio workloads.
- **Tier-Lowering Protection:** Monitors volatile megamorphic call sites. If the guard failure ratio exceeds **30%**, the system permanently deoptimizes the specialized path and locks execution to safe generic mode.
- **Cookie Security (Iteration 2):** HMAC-SHA256 signature + chmod 400 + tamper detection. Production roadmap: Ed25519.
- **Scientific Performance Audit (CPython 3.13, Linux x86_64, 50k ops):**
  - Stable Scenario: **3.25× faster vs `generic_add`**
  - vs `operator.add` native: **0.24× (4.26× slower)**
  - Volatile Scenario: **0.69× vs generic (31% slower — Guard thrashing)**
  - See `benchmarks/bench_add.py` for full reproduction.

### 3. ⚖️ [Scientific Benchmarks & Tests (`benchmarks/` & `tests/`)](./benchmarks)

- `benchmarks/bench_add.py` runs comparative benchmarks across 2 scenarios (Stable vs. Volatile Workloads) against Python's native C implementation (`operator.add`).
- `tests/test_sods.py` verifies 9/9 JIT invariants automatically (PIC, Guard deopt, Tier-Lowering, WASI taint, cookie HMAC, thread-safety, guard thrashing stress) and ensures zero modification of Python user code.

### 4. 🌐 [Visual Architecture Preview (`index.html`)](https://fajarkurnia0388.github.io/sods-runtime/)

- Interactive graphical visualization featuring a *Premium 2026 Dark-Mode* UI (`SF Mono` / layered cards structure).
- Illustrates the complete 5-stage pipeline flow (from Cold Run to Warm Run).

### 🍪 5. Example Cookie State (profile.json)
Here is a telemetry snippet recorded by SODS after a *Cold Run*, protected with an HMAC-SHA256 signature to prevent tampering:
```json
{
  "payload": {
    "schema_version": 2,
    "program_hash": "e3b0c44298fc1c14...",
    "profile": {
      "type_seen": { "generic_add": { "int,int": 100 } }
    },
    "specialized": {
      "generic_add": {
        "label": "Polymorphic Inline Cache (PIC: 1)",
        "supported_signatures": [["int", "int"]]
      }
    },
    "tier_lowered": []
  },
  "signature": "8a3f...d7",
  "signature_algo": "hmac-sha256"
}
```

---

## 🚀 How to Run CLI Tools & Prototypes

You can run and audit the prototype using the CLI entrypoints:

```bash
# Clone the repository
git clone https://github.com/fajarkurnia0388/sods-runtime.git
cd sods-runtime

# Install the package in editable mode
pip install -e .

# ── 1. Explore CLI Tools ──────────────────────────────────────────────────
sods observe --target generic_add --workload-size 1000
sods specialize --target generic_add --workload-size 25000
sods verify --target generic_add

# ── 2. Run Terminal Educational Prototype Script ─────────────────────────
python3 prototype_sods.py

# ── 3. Run Scientific Benchmark against Python's Native C Operator ────────
PYTHONPATH=src python3 benchmarks/bench_add.py

# ── 4. Run Automated Test Suite ───────────────────────────────────────────
PYTHONPATH=src python3 -m unittest discover tests
```

---

## 🛠️ Implementation Status vs. Production Roadmap

To maintain strict scientific objectivity, we divide project capabilities into 4 reality strata:

| Capability / Obstacle | Actual Status in Repo | Target Technology for Production |
| --- | --- | --- |
| **Polymorphic Inline Caches (PIC)** | **Implemented** (Python PoC wrapper) | Register-level `cmp` + `jne` Machine Code |
| **On-Stack Replacement (OSR)** | **Implemented** (Python Stack Evacuation) | Native Stack Frame Reconstruction |
| **Tier-Lowering Protection** | **Implemented** (Persistent Locked Set) | Polymorphic Call Site Tier-Lowering |
| **WASI Side-Effect Boundary** | **Simulated** (Manual Taint Flag) | `Seccomp` / WASI POSIX Interception |
| **Sandbox Evasion Mitigation** | **Simulated** (Virtual Timing Noise) | KVM/VMware High-Res Clock Randomization |
| **Closed-Binary Observability** | **Proposed** (Roadmap Phase 2) | Kernel Interception via **eBPF** + **DynamoRIO** |
| **Zero-Overhead Profiling** | **Proposed** (Roadmap Phase 1) | **Hardware PMU Statistical Sampling** |
| **Tauri Drop-In Companion Runtime** | **Future Work** (Roadmap Phase 4) | Experimental Tauri Companion Module |

---

## 🤝 License & Contributions

This architecture project is distributed under the **MIT / Apache-2.0** license. Contributions, discussions, and further experimentation in integrating *eBPF Probe Hooks*, *Python 3.12+ `sys.monitoring`*, or *Cranelift JIT Emitters* are highly welcome!

<div align="center">
  <p>Created consciously and with high discipline under the philosophy of returning computational elegance.</p>
</div>
