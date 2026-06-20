<div align="center">
  <h1>⚙️ SODS — Sandbox Observer-Driven Specializer</h1>
  <p><b>A Research Concept & Educational PoC for Observer-Driven Runtime Specialization</b></p>
  <p>📖 <b><a href="./README_EN.md">Read in English</a></b></p>

[![Version](<https://img.shields.io/badge/version-2.4.0%20(Research%20PoC)-58a6ff.svg>)](./prototype_sods.py)
[![Theory](https://img.shields.io/badge/theory-Rice's%20Theorem%20Workaround-a371f7.svg)](./WHITEPAPER.md)
[![Genesis](https://img.shields.io/badge/genesis-Di%20TeknoIn%20Inspiration-ffbd2e.svg)](./GENESIS.md)
[![Speedup](<https://img.shields.io/badge/speedup-3.25×%20vs%20generic%20/%200.24×%20vs%20native-56d364.svg>)](./benchmarks/bench_add.py)
[![Status](<https://img.shields.io/badge/status-Educational_PoC_Python-yellow.svg>)](#)
[![Tests](<https://img.shields.io/badge/tests-9/9_(3.10--3.13)_passing-success.svg>)](./tests/test_sods.py)
[![Vibe](<https://img.shields.io/badge/vibe-Doom%20(1993)%20-Apple%20Task%20Manager%20Efficiency-f0883e.svg>)](./GENESIS.md)

</div>

---

> **🚀 Penulis & Atribusi Kolaborasi Riset**
>
> - **Gagasan Konseptual Orisinal & Rancang Bangun SODS:** Fajar Kurnia ([@fajarkurnia0388](https://github.com/fajarkurnia0388))
> - **Asisten Elaborasi Teori & Instrumentasi Agentik:** Arena.ai (Agent Mode)
> - **Tanggal Rilis:** 19 Juni 2026

---

## 💡 Apa itu SODS?

**SODS (_Sandbox Observer-Driven Specializer_)** adalah sebuah rancang bangun arsitektur _runtime wrapper_ tingkat Sistem Operasi yang dirancang untuk mengeksplorasi pengembalian tingkat efisiensi komputasi ekstrem ala _Doom_ (1993) dan _Task Manager_ orisinal (1995) pada aplikasi modern yang mengalami pembengkakan parah (_software bloat_ — seperti aplikasi Electron, Node.js, atau Python).

SODS bertolak dari sebuah pertanyaan teoretis mendasar: _"Apabila Teorema Rice (1953) secara matematis melarang kita membuat alat konversi universal yang dijamin 100% ekuivalen untuk seluruh masukan tak terhingga ($\infty$), bagaimana jika kita membangun runtime yang mengamati perilaku eksekusi, menspesialisasi biner HANYA untuk masukan teramati, menyimpan profil persisten (seperti cookie), dan menyiapkan pintu darurat (OSR Deoptimization) saat asumsi dilanggar?"_

Proyek ini memodelkan filosofi kompilator JIT modern (_V8_, _PyPy_, _GraalVM_) serta teknik kompilasi dinamis rekayasa sistem AI kontemporer (seperti _torch.compile_ dan _Apache TVM_) tingkat industri, lalu mengemasnya menjadi konsep peta jalan _external OS-level wrapper converter_.

---

## ⚠️ Batasan & Disclaimer (Research PoC)

Proyek ini adalah murni **Educational Python PoC** dan bukan *production runtime*. Harap lihat [ROADMAP_STATUS.md](./ROADMAP_STATUS.md) untuk melihat matriks realita mengenai kapabilitas yang sudah *Implemented*, baru *Simulated*, atau sekadar rancangan (*Proposed Roadmap*).

## 🌟 Potensi Raksasa Jika Perkakas (*Tools*) SODS Kelak Dibangun (Why SODS Matters)

Agar setiap tingkatan profesional memahami dampak revolusioner riset ini, kami memetakan apa yang akan terjadi jika Peta Jalan SODS kelak diwujudkan menjadi perkakas produksi (*production tools*) nyata (misal: `sods-pack` atau `ExoRuntime`):

### 🌱 1. Bagi Pemula (_Junior Developers / Students_): "Membuat Aplikasi Ringan Tanpa Sakit Kepala"

Saat pemula belajar membangun aplikasi desktop menggunakan HTML/JS/Python, mereka sering menggunakan framework _Electron_ atau _PyQt_. Namun mereka terkejut dan berkecil hati saat melihat aplikasi kalkulator sederhana buatan mereka berukuran **150 MB** dan memakan RAM **300 MB**.

- **Potensi Alat SODS:** Jika konverter otonom SODS tersedia, pemula cukup menulis kode JS/Python murni yang biasa mereka tulis. Alat SODS akan membungkus, memantau, dan menyihir aplikasi mereka di belakang layar menjadi secepat dan seringan biner C. Mereka dapat memamerkan aplikasi yang berjalan mulus di laptop lama atau ponsel murah tanpa perlu mempelajari teknik optimisasi Rust/C yang luar biasa rumit.

### ⚡ 2. Bagi Profesional Web / Mobile (_Intermediate Frontend / Mobile Devs_): "Performa Perangkat Keras Tanpa Perlu Rewrite Bahasa"

Pengembang kontemporer kerap dituntut membangun komputasi berat di klien (_rendering_ data 10.000 baris, kanvas grafis, atau kriptografi lokal). Saat ini, satu-satunya cara mendapatkan performa tinggi adalah mempelajari **Rust** atau **Zig** untuk dikompilasi ke WebAssembly. Bagi banyak tim, kurva belajar Rust yang teramat curam memicu anjloknya produktivitas pengerjaan fitur (_velocity drop_).

- **Potensi Alat SODS:** Pengembang cukup mempertahankan basis kode **TypeScript** atau **Python** mapan mereka. Mesin _Runtime Wrapper_ SODS akan mencegat eksekusi, menjejak _Hot Paths_, dan memancarkan instruksi Assembly/WASM murni _on-the-fly_. Tim memperoleh **kecepatan 3×–5× lipat "gratis"** tanpa mengorbankan kecepatan penyerahan fitur.

### 🏢 3. Bagi Arsitek Cloud & Eksekutif Bisnis (_Senior Cloud/Backend Enterprise Architects_): "Memotong Tagihan Server AWS / Cloud Hingga Jutaan Dolar"

Di perusahaan berskala _Enterprise / Unicorn_, peladen _backend_ monolitik (Node.js, Python, Ruby) menangani miliaran permintaan per hari. Kelemahan _overhead_ bahasa dinamis memaksa korporasi membakar uang menyewa ribuan instansi _Kubernetes pod_ atau _AWS EC2_ berkapasitas RAM gajah dan prosesor mahal.

- **Potensi Alat SODS:** Diinstrumenkan di tingkat _Container Hypervisor_ (seperti _Wasmtime Fuel Pods_ atau _eBPF Mesh_), setiap mikrolayanan perusahaan akan dispesialisasi secara empiris saat peladen berjalan. Pengurangan _jejak memori_ hingga 70% dan pemotongan siklus CPU berarti peladen sanggup menelan trafik **3× lipat di atas infrastruktur perangkat keras (*hardware*) yang persis sama**. Korporasi menghemat anggaran tagihan peladen (_cloud billing_) hingga jutaan dolar per tahun dan menaikkan marjin laba bisnis.

### 🌍 4. Bagi Penggiat Green Computing & Ekosistem Makro: "Menyelamatkan Perangkat Keras Lawas dan Bumi"

Jutaan laptop lama dan perangkat ponsel dibuang ke tempat sampah setiap tahun menjadi limbah elektronik (_e-waste_) semata-mata karena perangkat keras mereka tidak sanggup lagi menahan sistem operasi dan aplikasi obrolan modern yang memakan RAM berkuintal-kuintal.

- **Potensi Alat SODS:** Konverter otonom SODS bertindak sebagai **Pahlawan Aksesibilitas Digital Global**. Dengan merampingkan eksekusi perangkat lunak dari luar, alat ini memperpanjang umur masa pakai perangkat keras (*hardware*) lama selama 5–10 tahun, menekan laju limbah _e-waste_, dan menurunkan jejak emisi karbon dari peladen pusat data di seluruh dunia.

---

## 🏛️ Etalase Proyek Modular

Repositori ini menyajikan **Desain Penelitian Hibrida (_Design Science Research_ & Studi Literatur Kualitatif)** yang dikemas ke dalam pilar modular siap pakai:

### 1. 📜 [Karya Tulis Ilmiah (*Whitepaper*) Teknis, Catatan Riset & Transkrip Genesis (`WHITEPAPER.md`)](./WHITEPAPER.md) (atau [Versi Bahasa Inggris](./WHITEPAPER_EN.md))

- **[Inspirasi Awal (`GENESIS.md`):](./GENESIS.md)** Mengabadikan transkrip esai YouTube **Di TeknoIn** (_Ketika Performance Bukan Prioritas Lagi_) yang menjadi pemantik lahirnya arsitektur ini. (atau [Versi Bahasa Inggris](./GENESIS_EN.md))
- Naskah riset mendalam yang diformat khusus untuk ekosistem sumber terbuka (*open-source*) dengan strata bukti transparan (**T1 Primer Kanonik** hingga **T4 Anekdot Forum**).
- **Audit Kesenjangan Realitas Peta Jalan (*Roadmap*):** Memisahkan secara tegas antara implementasi PoC Python saat ini berbanding peta jalan rekayasa kernel OS sejati.
- **Bab 5.6 Terdepan:** Mengurai peta mitigasi 5 rintangan produksi melalui analisis noda selektif (*selective taint analysis* menggunakan Mozilla `rr`), intersepsi kernel tanpa modifikasi (_eBPF_ + _DynamoRIO_), pengambilan sampel statistik PMU perangkat keras (*hardware PMU statistical sampling* dengan *overhead* <1%), dan pengacakan kebisingan waktu (*timing noise randomization*).
- **Injeksi PEP 669:** Menganalisis pemanfaatan modul Python 3.12+ `sys.monitoring` sebagai jembatan penjejakan (*tracing*) tingkat rendah bebas *overhead*.

### 2. 💻 [Paket Perangkat Lunak Modular (`src/sods`)](./src/sods)

- **Polymorphic Inline Caches (PIC: 2–3):** Menspesialisasi komputasi komparasi tanpa kerentanan tipe tunggal (*monomorphic*), termasuk dukungan numerik campuran (*mixed numerics* seperti `int + float`).
- **Batas WASI I/O (*WASI I/O Boundary*):** Mencegat fungsi dengan efek samping I/O melalui analisis noda (*taint analysis*).
- **Keamanan Ulir Terkunci (*Thread-Safety Locked*):** Dilindungi pengunci `threading.Lock()` yang menanggulangi kondisi balapan (*race conditions*) pada beban kerja multi-ulir (*multithreaded*) atau `asyncio`.
- **Perlindungan Penurunan Tingkat (*Tier-Lowering Protection*):** Memantau badai masukan acak pada lokasi megamorfik yang sangat tidak stabil (*highly volatile megamorphic sites*). Bila rasio kegagalan *guard* melampaui **30%**, sistem membakar spesialisasi secara permanen dan mengunci jalur ke mode aman.
- **Audit Kinerja Ilmiah:** Mengeliminasi *overhead* pengiriman (*dispatch*) dinamis Python menghasilkan peningkatan kecepatan laju keluaran (*throughput*) **3.1× hingga 3.25× lebih cepat vs target generik** (terukur konsisten di Python 3.10–3.13, Linux x86_64). Terhadap `operator.add` tingkat C bawaan (*native C-level*), SODS masih 4.3× lebih lambat — pertukaran timbal-balik (*trade-off*) yang jujur dari *wrapper* PoC Python.

### 3. ⚖️ [Pengujian & Benchmark Ilmiah (`benchmarks/` & `tests/`)](./benchmarks)

- `benchmarks/bench_add.py` mengeksekusi komparasi 2 skenario (Beban Kerja [*Workload*] Stabil vs Beban Kerja Volatile) berbanding eksekusi murni tingkat C bawaan Python (`operator.add`).
- `tests/test_sods.py` memverifikasi 100% invarian *compiler* JIT secara otomatis penuh.

### 4. 🌐 [Pratinjau Visual Arsitektur Sistem (`index.html`)](https://fajarkurnia0388.github.io/sods-runtime/)

- Visualisasi grafis interaktif berdesain mode gelap (*dark mode*) 2026 Premium (`SF Mono` / struktur kartu berlapis).
- Mengilustrasikan aliran 5 Tahap *pipeline* secara lengkap (dari eksekusi awal [*cold run*] hingga eksekusi hangat [*warm run*]).

### 🍪 5. Contoh State Cookie (profile.json)
Berikut adalah cuplikan metrik telemetri yang disimpan SODS pasca *cold run*, dilindungi HMAC-SHA256:
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

## 🚀 Cara Menjalankan Perkakas CLI (*CLI Tools*) & Prototipe

Anda dapat mengeksekusi dan mengaudit prototipe menggunakan titik masuk CLI yang elegan:

```bash
# Kloning repositori
git clone https://github.com/fajarkurnia0388/sods-runtime.git
cd sods-runtime

# Pasang paket dalam mode yang dapat diedit (editable mode)
pip install -e .

# ── 1. Eksplorasi Perkakas CLI (CLI Tools) ───────────────────────────────
sods observe --target generic_add --workload-size 1000
sods specialize --target generic_add --workload-size 25000
sods verify --target generic_add

# ── 2. Eksekusi Skrip Edukatif Terminal ─────────────────────────────────────
python3 prototype_sods.py

# ── 3. Eksekusi Uji Tolok Ukur Ilmiah (Scientific Benchmark) vs Operator C Bawaan Python ──
PYTHONPATH=src python3 benchmarks/bench_add.py

# ── 4. Jalankan Rangkaian Pengujian Otomatis (Automated Test Suite) ─────────
PYTHONPATH=src python3 -m unittest discover tests
```

---

## 🛠️ Status Implementasi vs Peta Jalan Produksi

Guna menjaga objektivitas ilmiah yang ketat, kami membagi kapabilitas proyek ke dalam 4 strata realitas:

| Kapabilitas / Rintangan             | Status Aktual di Repo                     | Pemilihan Teknologi Target Produksi        |
| ----------------------------------- | ----------------------------------------- | ------------------------------------------ |
| **Polymorphic Inline Caches (PIC)** | **Terimplementasi (*Implemented*)** (Python PoC *wrapper*)      | Kode Mesin `cmp` + `jne` Tingkat Register  |
| **On-Stack Replacement (OSR)**      | **Terimplementasi (*Implemented*)** (Python Stack Evacuation) | Rekonstruksi Bingkai Tumpukan (*Stack Frame*) Asli          |
| **Tier-Lowering Protection**        | **Terimplementasi (*Implemented*)** (Persistent Locked Set)   | Penurunan Tingkat Lokasi Pemanggilan Polimorfik (*Polymorphic Call Site*)        |
| **WASI Side-Effect Boundary**       | **Disimulasikan (*Simulated*)** (Manual Taint Flag)         | Intersepsi `Seccomp` / WASI POSIX Interception        |
| **Sandbox Evasion Mitigation**      | **Disimulasikan (*Simulated*)** (Timing Noise Virtual)      | Pengacakan Jam Resolusi Tinggi KVM/VMware    |
| **Closed-Binary Observability**     | **Diusulkan (*Proposed*)** (Peta Jalan [*Roadmap*] Fase 2)            | Intersepsi Kernel **eBPF** + **DynamoRIO** |
| **Zero-Overhead Profiling**         | **Diusulkan (*Proposed*)** (Peta Jalan [*Roadmap*] Fase 1)            | Pengambilan Sampel Statistik PMU Perangkat Keras (*Hardware PMU*)      |
| **Tauri Drop-In Companion Runtime** | **Pekerjaan Masa Depan (*Future Work*)** (Peta Jalan [*Roadmap*] Fase 4)         | Modul Eksperimental Pendamping (*Companion*) Tauri        |

---

## 🤝 Lisensi & Kontribusi

Proyek arsitektur ini didistribusikan di bawah lisensi **MIT / Apache-2.0**. Kontribusi, diskusi, dan eksperimen lanjutan dalam mengintegrasikan _eBPF Probe Hooks_, _Python 3.12+ `sys.monitoring`_, atau _Cranelift JIT Emitters_ sangat disambut hangat!

<div align="center">
  <p>Dibuat secara sadar dan berdisiplin tinggi di bawah filosofi kembalinya keanggunan komputasi.</p>
</div>
