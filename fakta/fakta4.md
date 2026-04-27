# 📋 STANDAR METADATA WAJIB DALAM TATA KELOLA KEARSIPAN
## Konteks Modul 4.3 & 4.4 – PLN (Persero)

Berdasarkan regulasi Indonesia, standar internasional, dan praktik terbaik BUMN, berikut adalah **standar metadata wajib** yang harus dipenuhi dalam pengelolaan arsip digital terintegrasi.

---

## 🇮🇩 REGULASI NASIONAL: METADATA WAJIB MENURUT ANRI & PP 71/2019

### ✅ Perka ANRI No. 6 Tahun 2021 tentang Pengelolaan Arsip Elektronik
**Pasal 8–12** menetapkan metadata minimal yang harus melekat pada setiap arsip elektronik:

| Kategori | Field Metadata Wajib | Deskripsi & Contoh |
|----------|---------------------|------------------|
| **Identitas Arsip** | `Judul Arsip` | Nama dokumen yang mencerminkan isi (contoh: "Laporan Pemeliharaan Trafo GI Cengkareng") |
| | `Nomor Arsip/Kode Klasifikasi` | Kode unik berdasarkan skema klasifikasi organisasi (contoh: "OPS/PM/GI/2024/00123") |
| | `Jenis Arsip` | Kategori dokumen (Laporan, Kontrak, Surat Keputusan, Work Order, dll.) |
| **Konteks Penciptaan** | `Pencipta Arsip` | Unit/jabatan yang menghasilkan arsip (contoh: "Unit Pemeliharaan Transmisi Jawa-Bali") |
| | `Tanggal Penciptaan` | Waktu dokumen dibuat (format ISO 8601: `YYYY-MM-DDTHH:MM:SS+07:00`) |
| | `Lokasi Penciptaan` | Tempat/lokasi fisik atau sistem sumber (contoh: "SAP-PM Module, Server Jakarta") |
| **Konten & Struktur** | `Deskripsi/Abstrak` | Ringkasan isi arsip untuk keperluan temu kembali |
| | `Kata Kunci` | Istilah indeks untuk pencarian (contoh: "gardu induk, pemeliharaan, trafo, inspeksi") |
| | `Bahasa` | Bahasa dokumen (ID/EN) |
| **Manajemen & Akses** | `Klasifikasi Keamanan` | Tingkat sensitivitas: Publik / Internal / Terbatas / Rahasia / Vital |
| | `Masa Retensi` | Durasi penyimpanan aktif + inaktif (contoh: "10 tahun aktif + 5 tahun inaktif") |
| | `Nasib Akhir` | Disposisi akhir: Musnah / Serah ke ANRI / Permanen / Alih Media |
| **Integritas & Otentikasi** | `Format File` | Ekstensi & standar preservasi (PDF/A-1a, TIFF, XML terstruktur) |
| | `Ukuran File` | Ukuran dalam byte/KB/MB untuk validasi integritas |
| | `Checksum/Hash` | Nilai hash (SHA-256) untuk verifikasi keaslian & deteksi modifikasi |
| | `Tanda Tangan Elektronik` | Status & sertifikat TTE jika dokumen memerlukan otentikasi hukum |

> 📌 **Catatan Regulasi**: Metadata di atas **wajib tercatat secara sistemik** dan **tidak dapat diubah setelah arsip divalidasi final**, sesuai PP 71/2019 Pasal 35 tentang keamanan arsip elektronik.

---

## 🌍 STANDAR INTERNASIONAL YANG DIADOPSI

### ISO 23081-1:2017 – Metadata for Records
Standar ini memperkaya metadata ANRI dengan elemen kontekstual untuk interoperabilitas global:

```
✅ Elemen Tambahan Rekomendasi:
• `Identifier Unik Global` (UUID/DOI) untuk referensi lintas sistem
• `Hubungan Antar Arsip` (relasi: merupakan-bagian-dari, merujuk-ke, versi-dari)
• `Hak Akses & Lisensi` (copyright, ketentuan penggunaan ulang)
• `Riwayat Perubahan` (versioning: v1.0 → v1.1 dengan catatan revisi)
• `Keterkaitan Bisnis` (linked to: Kontrak #XYZ, Proyek #ABC, Aset ID #12345)
```

### ISO 15489-1:2016 – Records Management Principles
Menekankan prinsip **"metadata as evidence"**: metadata harus mampu membuktikan:
- 🔹 **Authenticity**: Arsip benar-benar diciptakan oleh pihak yang diklaim
- 🔹 **Reliability**: Isi arsip dapat diandalkan sebagai bukti transaksi bisnis
- 🔹 **Integrity**: Arsip lengkap dan terlindungi dari modifikasi tidak sah
- 🔹 **Usability**: Arsip dapat ditemukan, diakses, dan dipahami sepanjang masa retensi

---

## 🏢 KONTEKSTUALISASI METADATA UNTUK PLN

Berikut adalah **12 Field Metadata Inti** yang direkomendasikan untuk integrasi sistem PLN (SAP-PM, AMS, E-Office → Repositori Arsip):

```latex
\begin{table}[htbp]
\centering
\small
\caption{Metadata Wajib Terintegrasi untuk Arsip Operasional PLN}
\begin{tabularx}{\textwidth}{@{} l >{\raggedright\arraybackslash}X c @{}}
\toprule
\textbf{Kode Field} & \textbf{Nama Field \& Definisi} & \textbf{Sumber Auto-Capture} \\
\midrule
\texttt{PLN\_DOC\_ID} & ID Dokumen Unik PLN (format: \texttt{[UNIT]/[JENIS]/[TAHN]/[NOMOR]}) & Sistem Nomor Otomatis \\
\texttt{ASSET\_ID} & ID Aset terkait (GI, Trafo, Saluran, Gardu) & SAP-PM / AMS \\
\texttt{WO\_REF} & Referensi Work Order (jika berlaku) & SAP-PM Module \\
\texttt{CONTRACT\_REF} & Referensi Kontrak/Perjanjian (jika berlaku) & E-Proc / Legal System \\
\texttt{LOCATION\_CODE} & Kode lokasi geografis/operasional (Wilayah, Rayon, GI) & GIS / Master Data \\
\texttt{CREATOR\_UNIT} & Unit pencipta arsip (struktur organisasi PLN) & IAM / HR System \\
\texttt{CREATOR\_ROLE} & Peran/jabatan pencipta (Teknisi, Supervisor, Manajer) & IAM / RBAC \\
\texttt{TIMESTAMP\_CREATE} & Waktu penciptaan arsip (ISO 8601, timezone WIB/WITA/WIT) & System Clock \\
\texttt{CLASSIFICATION} & Klasifikasi keamanan + fungsi bisnis (misal: \texttt{VITAL/OPS/PM}) & Policy Engine \\
\texttt{RETENTION\_RULE} & Aturan retensi otomatis berdasarkan jenis + klasifikasi & Retention Schedule DB \\
\texttt{INTEGRITY\_HASH} & SHA-256 hash untuk verifikasi keaslian & Cryptographic Module \\
\texttt{AUDIT\_TRAIL\_REF} & ID log audit yang merekam riwayat akses/perubahan & SIEM / Audit Log \\
\bottomrule
\end{tabularx}
\end{table}
```

### 🔗 Mekanisme Auto-Capture (Konseptual)
```
SAP-PM Status: "TECO" (Technically Complete)
       ↓
Pemicu → Generate Draft Arsip + Auto-Populate 12 Field Metadata
       ↓
Routing Digital → Validasi Supervisor → Validasi Unit Kearsipan
       ↓
Finalisasi → Hash Calculation + Immutable Audit Log Entry
       ↓
Penyimpanan → Repositori Arsip PLN dengan metadata terindeks
```

---

## 🎯 IMPLEMENTASI DALAM MODUL 4.3 (BAB 4: SOP DIGITAL)

### Klausul Metadata dalam SOP Digital Terintegrasi
```latex
\begin{plnbox}[📘 Pasal 5: Standar Metadata dalam SOP Digital]
\textbf{5.1 Kewajiban Pengisian Metadata}
\begin{enumerate}[leftmargin=*]
    \item Setiap arsip digital wajib dilengkapi 12 field metadata inti sebagaimana tercantum dalam Lampiran A.
    \item Field \texttt{PLN\_DOC\_ID}, \texttt{TIMESTAMP\_CREATE}, dan \texttt{INTEGRITY\_HASH} wajib dihasilkan otomatis oleh sistem, tidak boleh diinput manual.
    \item Field \texttt{CLASSIFICATION} dan \texttt{RETENTION\_RULE} ditentukan berdasarkan matriks kebijakan yang terintegrasi dengan Policy Engine.
\end{enumerate}

\textbf{5.2 Validasi & Penolakan}
\begin{enumerate}[leftmargin=*]
    \item Sistem wajib menolak penyimpanan arsip jika terdapat field wajib yang kosong atau tidak sesuai format.
    \item Unit Kearsipan berhak mengembalikan dokumen untuk perbaikan metadata sebelum proses validasi lanjutan.
\end{enumerate}

\textbf{5.3 Perubahan Metadata Pasca-Validasi}
\begin{enumerate}[leftmargin=*]
    \item Metadata yang telah divalidasi final bersifat \textit{immutable} (tidak dapat diubah).
    \item Koreksi hanya dapat dilakukan melalui prosedur \textit{metadata amendment} yang terekam dalam audit trail terpisah dan memerlukan persetujuan Direktur terkait.
\end{enumerate}
\end{plnbox}
```

---

## 📊 CHECKLIST VALIDASI METADATA (Untuk Workshop Bab 4)

```latex
\begin{table}[htbp]
\centering
\small
\caption{Checklist Validasi Metadata Wajib – Output Peserta}
\begin{tabularx}{\textwidth}{@{} l X c c @{}}
\toprule
\textbf{Field} & \textbf{Kriteria Validasi} & \textbf{Auto?} & \textbf{Status} \\
\midrule
\texttt{PLN\_DOC\_ID} & Format sesuai pola: [UNIT]/[JENIS]/[TAHN]/[NOMOR] & ✅ Ya & \text{\textsquare} \\
\texttt{ASSET\_ID} & Terdaftar dalam Master Data Aset PLN & ✅ Ya & \text{\textsquare} \\
\texttt{CREATOR\_UNIT} & Sesuai struktur organisasi resmi PLN & ✅ Ya & \text{\textsquare} \\
\texttt{TIMESTAMP\_CREATE} & Format ISO 8601, timezone konsisten & ✅ Ya & \text{\textsquare} \\
\texttt{CLASSIFICATION} & Memilih dari daftar terkontrol (Publik–Vital) & ⚠️ Semi & \text{\textsquare} \\
\texttt{RETENTION\_RULE} & Terhubung ke jadwal retensi terpusat & ✅ Ya & \text{\textsquare} \\
\texttt{INTEGRITY\_HASH} & SHA-256, diverifikasi sistem & ✅ Ya & \text{\textsquare} \\
\texttt{Deskripsi} & Minimal 20 kata, mencerminkan isi & ❌ Manual & \text{\textsquare} \\
\texttt{Kata Kunci} & 3–5 istilah, dari thesaurus terkontrol & ⚠️ Semi & \text{\textsquare} \\
\bottomrule
\end{tabularx}
\end{table}
```

---

## 📚 REFERENSI RESMI STANDAR METADATA

| Sumber | Relevansi | Akses |
|--------|-----------|--------|
| **Perka ANRI No. 6/2021** | Regulasi teknis metadata arsip elektronik Indonesia | anri.go.id |
| **PP 71/2019 tentang PSTE** | Dasar hukum otentikasi & integritas arsip elektronik | jdih.setkab.go.id |
| **ISO 23081-1:2017** | Standar internasional metadata for records | iso.org (berbayar) |
| **ISO 15489-1:2016** | Prinsip metadata sebagai bukti (evidence) | iso.org (berbayar) |
| **NARA Metadata Guidelines** | Praktik terbaik metadata untuk preservasi digital | archives.gov (gratis) |
| **UK National Archives Metadata Standard** | Implementasi metadata dalam konteks pemerintah | nationalarchives.gov.uk (gratis) |

---

## ✅ KESIMPULAN

| Pertanyaan | Jawaban |
|------------|---------|
| **Apa metadata wajib minimal menurut regulasi Indonesia?** | 15 field sesuai Perka ANRI No. 6/2021 Pasal 8–12, mencakup identitas, konteks, konten, manajemen, dan integritas |
| **Bagaimana mengadaptasinya untuk PLN?** | Tambahkan 12 field kontekstual terintegrasi (ASSET_ID, WO_REF, dll.) yang dapat di-capture otomatis dari SAP/AMS/E-Office |
| **Apakah metadata dapat diubah setelah validasi?** | ❌ Tidak. Metadata final bersifat *immutable*; koreksi memerlukan prosedur *amendment* ber-audit |
| **Bagaimana memastikan kepatuhan?** | Gunakan checklist validasi di SOP Digital + sistem menolak penyimpanan jika field wajib tidak terpenuhi |

> 📌 **Rekomendasi Implementasi**: Integrasikan standar metadata ini ke dalam **template SOP Digital** (Bab 4 Modul 4.3) dan **skema audit trail** (Bab 4 Modul 4.4) untuk memastikan output peserta selaras dengan regulasi dan siap implementasi.

Jika Anda memerlukan **kode LaTeX untuk lampiran standar metadata**, **template checklist validasi dalam format `.xlsx`**, atau **diagram alur auto-capture metadata untuk presentasi**, beri tahu saya dan akan saya susun secara instan. 🚀