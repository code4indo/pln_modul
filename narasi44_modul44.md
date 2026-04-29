# Naskah Narasumber — Modul 4.4 (Level 4 Mastery)
## Perancangan Sistem Keamanan & Keterlacakan Terintegrasi
**PT PLN (Persero) — Center of Excellence Records Management**

> **Petunjuk Penggunaan:** Dokumen ini adalah naskah *verbatim* yang dibacakan oleh narasumber. Tanda `[jeda]` menandakan narasumber berhenti sejenak untuk memberi waktu peserta mencerna. Tanda `[tunjuk layar]` menandakan gesture ke slide. Tanda `[interaksi]` menandakan narasumber meminta respons peserta.

---

### Slide 1 — Halaman Judul

"Selamat pagi, Bapak dan Ibu. Terima kasih atas kehadiran Anda di tengah kesibukan operasional. Saya pastikan 45 menit ke depan akan memberikan nilai tambah yang signifikan bagi tugas pengawasan dan pengambilan keputusan Anda.

Hari ini kita membahas topik yang menjadi fondasi dari seluruh transformasi kearsipan digital: keamanan dan keterlacakan. [jeda] Tanpa sistem keamanan yang terintegrasi, setiap dokumen yang telah dioptimalkan pada Modul 4.3 tetap rentan terhadap akses tidak berwenang, manipulasi data, dan kegagalan pemulihan saat bencana.

Judul modul ini adalah Perancangan Sistem Keamanan dan Keterlacakan Terintegrasi. Level 4, Mastery. Artinya, setelah sesi ini, Bapak-Ibu tidak hanya memahami konsep, tetapi mampu merancang, mengesahkan, dan memastikan implementasi keempat pilar keamanan arsip di unit kerja masing-masing."

---

### Slide 2 — Sasaran & Prasyarat Peserta

"Modul ini dirancang khusus untuk Manajemen Atas. [jeda] Mengapa? Karena keputusan mengenai skema kontrol akses, kebijakan keamanan, dan anggaran disaster recovery tidak dapat diambil di tingkat operasional. Hanya Bapak-Ibu yang memiliki kewenangan untuk menetapkan klasifikasi arsip vital, mengesahkan kebijakan ISMS, dan mengalokasikan sumber daya untuk infrastruktur keamanan.

Sebagai prasyarat, saya asumsikan Bapak-Ibu telah menyelesaikan Modul 4.1 hingga 4.3. Jadi kita tidak akan membahas dasar-dasar arsitektur atau optimalisasi prosedur dari nol. Kita akan langsung masuk ke pertanyaan strategis: apakah arsip kita benar-benar aman, terlacak, dan dapat dipulihkan?"

---

### Slide 3 — Tujuan Pembelajaran & Target Kompetensi

"Di akhir sesi ini, Bapak-Ibu akan menguasai empat kompetensi utama. [tunjuk layar]

Pertama, merancang skema RBAC terintegrasi — yaitu menentukan siapa yang boleh mengakses apa, berdasarkan peran organisasi, bukan berdasarkan personal request. Kedua, merancang audit trail otomatis — memastikan setiap sentuhan terhadap arsip tercatat secara permanen dan tidak dapat dimanipulasi. Ketiga, merumuskan kebijakan ISMS — menerjemahkan standar ISO 27001 dan NIST ke dalam kebijakan internal PLN yang mengikat. Dan keempat, merancang strategi backup dan disaster recovery — menjamin ketersediaan arsip vital meskipun terjadi kegagalan sistem atau bencana.

Setiap kompetensi ini akan menghasilkan satu dokumen portofolio yang dapat langsung Bapak-Ibu bawa sebagai usulan kebijakan di unit kerja."

---

### Slide 4 — Agenda Pembelajaran

"Perjalanan kita hari ini terbagi tiga bagian. [tunjuk layar]

Bagian I: Fondasi dan Urgensi, sekitar 5 menit, untuk memahami konteks ancaman dan arsitektur keempat pilar. Bagian II: Empat Pilar Keamanan, sekitar 37 menit, di mana kita akan membahas RBAC, audit trail, kebijakan ISMS, dan backup atau DR secara mendalam. Bagian III: Studi Kasus dan Validasi, sekitar 3 menit, untuk menguji pemahaman melalui simulasi insiden dan executive tollgate.

Terdapat empat sesi workshop mandiri yang masing-masing berdurasi 30 menit, di luar sesi fasilitasi ini. Total durasi fasilitasi adalah 45 menit. [jeda] Sebelum kita masuk ke pilar pertama, kita perlu menyamakan persepsi mengapa topik ini menjadi prioritas strategis."

---

### Slide 5 — Konteks & Urgensi: Mengapa Ini Penting bagi PLN?

"Bapak-Ibu, ancaman terhadap keamanan informasi tidak lagi bersifat potensial — ancaman tersebut sudah nyata dan terus meningkat. [tunjuk layar]

Data internal menunjukkan adanya peningkatan insiden keamanan siber, termasuk upaya akses tidak berwenang dan kehilangan data akibat human error. Di luar organisasi, regulasi semakin ketat. PP 71 Tahun 2019 menetapkan bahwa setiap lembaga negara wajib menjamin keamanan arsip digital. ISO 27001:2022 telah memperbarui daftar kontrol keamanannya. Dan sebagai BUMN, PLN wajib memenuhi prinsip Tata Kelola Perusahaan yang Baik, termasuk transparansi dan akuntabilitas pengelolaan informasi.

Risikonya bersifat ganda. [jeda] Risiko hukum: sanksi administratif dan pidana apabila terjadi kebocoran data pribadi atau kontrak strategis. Risiko operasional: lumpuhnya proses bisnis akibat hilangnya arsip vital yang tidak memiliki cadangan. Dan risiko reputasi: kehilangan kepercayaan pemangku kepentingan, termasuk regulator dan mitra kerja.

Oleh karena itu, keamanan arsip bukan lagi tugas unit IT semata. Ini adalah tanggung jawab tata kelola perusahaan yang berada di tangan Manajemen Atas."

---

### Slide 6 — Arsitektur Keamanan Terintegrasi: 4 Pilar

"Inilah arsitektur keamanan yang akan kita bangun bersama. [tunjuk layar]

Empat pilar yang saling terhubung. Pilar pertama: RBAC — kontrol akses berbasis peran. Ini menjawab pertanyaan SIAPA yang boleh masuk. Pilar kedua: Audit Trail — keterlacakan. Ini menjawab pertanyaan KAPAN dan APA yang dilakukan. Pilar ketiga: Kebijakan ISMS — tata kelola keamanan. Ini menjawab pertanyaan BAGAIMANA aturan mainnya. Dan pilar keempat: Backup dan DR — ketersediaan. Ini menjawab pertanyaan BAGAIMANA jika terjadi kegagalan.

Satu hal yang harus Bapak-Ibu catat: keempat pilar ini harus dirancang bersamaan, bukan berurutan oleh unit yang berbeda tanpa koordinasi. [jeda] Solusi parsial sama dengan celah keamanan yang tidak terdeteksi hingga terjadi insiden. RBAC yang kuat tidak ada artinya jika log audit dapat dihapus. Audit trail yang lengkap tidak ada artinya jika tidak ada kebijakan yang mengaturnya. Dan kebijakan yang sempurna tidak ada artinya jika arsip vital tidak memiliki cadangan saat sistem utama rusak.

Kita akan membahas masing-masing pilar secara sistematis."

---

### Slide 7 — Kerangka Berpikir Modul 4.4

"Sebelum masuk ke detail teknis, izinkan saya menunjukkan kerangka berpikir modul ini. [tunjuk layar]

Kita berangkat dari fondasi: pemahaman ancaman, regulasi, dan risiko. Dari situ, kita naik ke perancangan keempat pilar keamanan. Setiap pilar memiliki output berupa dokumen portofolio yang dapat diimplementasikan. Puncaknya adalah studi kasus integratif pada Bagian III, di mana kita akan menguji apakah keempat pilar benar-benar bekerja secara sinergis saat terjadi insiden.

Bapak-Ibu tidak perlu menjadi ahli kriptografi atau administrator jaringan. Tugas Anda adalah memastikan keempat pilar ini dirancang dengan benar, diimplementasikan dengan konsisten, dan diaudit secara berkala. [jeda] Sekarang kita masuk ke Pilar pertama: RBAC."

---

### Section Divider — Pilar 1: Kontrol Akses Berbasis Peran (RBAC)

"Kita masuk ke Pilar pertama: Kontrol Akses Berbasis Peran atau RBAC. [jeda] Di bagian ini, kita akan membahas siapa yang boleh mengakses apa, bagaimana hak akses dikelola, dan bagaimana mencegah penyalahgunaan wewenang."

---

### Slide 8 — Section Divider: Pilar 1 — RBAC

"Kita masuk ke Bagian II: Empat Pilar Keamanan. [jeda] Pilar pertama adalah Kontrol Akses Berbasis Peran atau RBAC. Di bagian ini, kita akan merancang siapa yang boleh mengakses apa, berdasarkan peran organisasi."

---

## BAGIAN I: PILAR 1 — RBAC (10 Menit)

### Slide 9 — Tiga Prinsip Fundamental RBAC

"Kita mulai dari fondasi keamanan paling dasar: mengontrol siapa yang boleh mengakses apa. [tunjuk layar]

Terdapat tiga prinsip fundamental dalam RBAC. Pertama, Least Privilege — hak akses minimum yang benar-benar diperlukan. Seorang staf tata usaha tidak perlu memiliki hak ekspor terhadap arsip rahasia jika tugasnya hanya membaca. Kedua, Segregation of Duties — pemisahan tugas. Tidak boleh ada satu peran yang sekaligus memiliki kombinasi hak menciptakan, menyetujui, dan mengekspor arsip vital. Ketiga, Break-Glass — akses darurat di luar hak normal, dengan pencatatan audit trail lengkap dan persetujuan atasan pasca-kejadian.

Mengapa RBAC menjadi fondasi keterlacakan? [jeda] Karena tanpa kontrol akses terstruktur, log audit menjadi tidak bermakna. RBAC memastikan setiap jejak digital merepresentasikan tindakan pihak yang berwenang. Jika siapa saja bisa mengakses apa saja, maka siapa pun bisa menjadi tersangka saat terjadi kebocoran."

---

### Slide 9 — Model RBAC NIST

"Ini adalah model RBAC standar NIST yang kita adopsi. [tunjuk layar]

Perhatikan strukturnya. Pengguna tidak diberikan hak akses langsung. Pengguna dihubungkan dengan peran — role — melalui relasi User Assignment. Peran kemudian dihubungkan dengan izin — permission — melalui relasi Permission Assignment. Saat pengguna login, sesi aktif dibentuk, dan sesi tersebut mengaktifkan peran yang dimiliki pengguna.

Pendekatan ini mempermudah manajemen siklus hidup akses. [jeda] Saat seorang pegawai mutasi, kita tidak perlu mengubah puluhan izin satu per satu. Kita cukup mengubah peran yang melekat pada pegawai tersebut. Saat pensiun, akses dapat dicabut secara sistematis tanpa risiko ada izin yang tertinggal. Ini adalah tata kelola akses yang scalable untuk organisasi sebesar PLN."

---

### Slide 11 — Matriks RBAC: Role × Klasifikasi Arsip PLN

"Inilah contoh Matriks RBAC yang menghubungkan peran dengan klasifikasi arsip. [tunjuk layar]

Baris menunjukkan peran: Staf Kearsipan, Staf Administrasi, Kabag TU, Staf Hukum, Staf IT, General Manager, Auditor SPI, dan VP Cyber Security. Kolom menunjukkan klasifikasi: Publik, Terbatas, Rahasia, dan Vital.

Perhatikan pola aksesnya. Staf Administrasi hanya boleh Create dan Read pada arsip Publik dan Terbatas, tidak boleh menyentuh Rahasia dan Vital. Kabag TU memiliki hak Create, Read, dan Update pada Publik dan Terbatas, serta Read dan Export pada Rahasia. General Manager memiliki hak paling luas, termasuk Approve pada Rahasia dan Vital.

Yang paling kritis adalah baris Staf IT atau DBA. [jeda] Mereka memiliki akses Read pada hampir semua klasifikasi, bahkan Vital, karena tugas teknis mereka memerlukan akses ke database. Namun, mereka tidak memiliki hak Create, Update, atau Approve. Ini adalah penerapan Segregation of Duties. Mereka bisa melihat, tetapi tidak boleh mengubah atau menyetujui.

Sebagai Manajemen Atas, tugas Anda adalah memvalidasi bahwa tidak ada satu peran yang sekaligus memiliki kombinasi Create, Approve, dan Export pada arsip Vital tanpa mekanisme pengawasan."

---

### Slide 12 — Langkah Perancangan Skema RBAC

"Bagaimana cara merancang skema RBAC di unit kerja Anda? [tunjuk layar]

Terdapat lima langkah tata kelola. Pertama, identifikasi peran berdasarkan struktur organisasi dan jabatan yang ada di sistem kepegawaian. Kedua, tetapkan klasifikasi arsip sesuai dengan sensitivitas informasi. Ketiga, tetapkan matriks izin dengan menerapkan prinsip least privilege. Keempat, integrasikan dengan sistem SSO atau HRIS agar perubahan jabatan otomatis memperbarui hak akses. Dan kelima, tetapkan mekanisme review berkala minimal enam bulan sekali.

Validasi kritis yang harus Bapak-Ibu lakukan: periksa apakah ada akun aktif milik pegawai yang sudah mutasi atau pensiun. [jeda] Periksa apakah ada peran yang memiliki hak akses berlebihan tanpa justifikasi bisnis. Dan periksa apakah mekanisme break-glass pernah digunakan dan dicatat dengan lengkap.

Pertanyaan kuncinya adalah: apakah hak akses langsung dicabut saat mutasi atau pensiun tanpa menunggu keluhan? Kalau masih menunggu keluhan, berarti ada celah keamanan yang terbuka."

---

### Slide 13 — Output & Workshop: Pilar 1 (RBAC)

"Workshop pertama meminta Bapak-Ibu menyusun Matriks RBAC untuk satu unit kerja. [tunjuk layar]

Identifikasi minimal enam peran, tetapkan klasifikasi arsip, dan isi matriks izin dengan kode C, R, U, A, E. Kemudian validasi dengan prinsip least privilege dan segregation of duties. Outputnya adalah Matriks RBAC dan Prosedur Akses Darurat. Ini adalah portofolio pertama Anda untuk kriteria 4.4.1.

Silakan kerjakan pada lembar kerja yang telah disediakan. [jeda] Setelah RBAC terdefinisi, pertanyaan berikutnya adalah: bagaimana kita memastikan setiap aktivitas yang dilakukan oleh peran-peran tersebut tercatat secara permanen? Jawabannya ada di Pilar kedua: Audit Trail."

---

### Slide 13 — Section Divider: Pilar 2 — Audit Trail

"Kita selesai dengan Pilar 1. Sekarang kita masuk ke Pilar kedua: Audit Trail dan Keterlacakan. [jeda] Di bagian ini, kita akan memastikan setiap aktivitas terhadap arsip tercatat secara permanen dan tidak dapat dimanipulasi."

---

## BAGIAN II: PILAR 2 — AUDIT TRAIL (10 Menit)

### Slide 14 — Mengapa Audit Trail Berurutan setelah RBAC?

"RBAC mengontrol siapa yang boleh masuk pintu. Audit trail adalah kamera pengawas yang merekam setiap orang yang masuk, kapan, dan melakukan apa. [jeda]

Tanpa audit trail, RBAC hanya menjadi gerbang tanpa pengawas. Kita tidak akan pernah tahu apakah seseorang yang berwenang menyalahgunakan aksesnya. Atau apakah ada yang berhasil menembus RBAC melalui cara yang tidak sah.

Dalam konteks PLN, audit trail tidak lagi berupa buku catatan manual atau log file yang tersebar di berbagai server. [tunjuk layar] Kita membutuhkan Security Information and Event Management — SIEM — yang mengubah ribuan log mentah menjadi informasi yang dapat ditindaklanjuti secara proaktif. Dan kita membutuhkan Hash Chain, yang menghubungkan setiap entri log secara kriptografis. Jika satu byte diubah, seluruh rantai hash berikutnya gagal verifikasi. Manipulasi langsung terdeteksi."

---

### Slide 15 — Diagram Alur Audit Trail Sistem Arsip Digital PLN

"Perhatikan diagram alur ini. [tunjuk layar]

Setiap aktivitas pada sistem arsip — baik itu view, edit, maupun export — menghasilkan log yang mencakup empat elemen utama. WHO: ID pegawai dan peran yang terautentikasi melalui SSO. WHAT: jenis aksi yang dilakukan. WHEN: timestamp dalam format ISO 8601. WHERE: alamat IP dan lokasi unit kerja.

Keempat elemen ini adalah minimum yang harus tercatat untuk setiap sentuhan terhadap arsip. [jeda] Tanpa salah satu dari empat elemen ini, log tersebut tidak memiliki nilai pembuktian hukum. Timestamp yang tidak standar, IP yang tidak tercatat, atau ID pegawai yang tidak terhubung dengan SSO — semua itu akan merusak integritas audit trail.

Sebagai Manajemen Atas, Anda tidak perlu memahami cara kerja SIEM di level teknis. Tetapi Anda wajib memastikan bahwa kontrak dengan vendor sistem arsip mensyaratkan keempat elemen ini sebagai fitur wajib, bukan fitur tambahan."

---

### Slide 16 — 14 Field Metadata Audit Trail

"Dari empat elemen dasar tadi, kita perluas menjadi 14 field metadata yang wajib tercatat dalam setiap audit trail. [tunjuk layar]

Dua belas field wajib meliputi: DOC_ID, Timestamp, User_ID, Role, Action, IP_Address, Device_ID, Session_ID, Hash_Previous, Hash_Current, TTE_Status, dan Retention_Class. Dua field semi-wajib adalah Geolocation dan Correlation_ID untuk keperluan analisis forensik.

Perhatikan bahwa field Hash_Previous dan Hash_Current inilah yang membentuk Hash Chain. [jeda] Setiap log baru mencakup hash dari log sebelumnya. Jika seseupan berusaha menghapus atau mengubah satu log di tengah, hash pada log berikutnya tidak akan cocok, dan seluruh rantai dinyatakan tidak valid.

Keempat belas field ini memenuhi persyaratan PP 71 Tahun 2019 dan Perka ANRI 6 Tahun 2021. Jadi ini bukan standar internal semata, tetapi standar yang memiliki dasar hukum."

---

### Slide 17 — Hash Chain: Immutability Log Audit

"Mari kita lihat cara kerja Hash Chain secara visual. [tunjuk layar]

Log 1 memiliki hash a4f8c2. Log 2 memiliki hash 7d3e91 yang mencakup referensi dari hash Log 1. Log 3 memiliki hash 3b6c45 yang mencakup referensi dari hash Log 2. Begitu seterusnya. Semua hash ditandai valid.

Sekarang, bayangkan seseupan mencoba mengubah Log 3 pada pukul 23.45. [jeda] Hash Log 3 berubah. Akibatnya, hash Log 4 yang mencakup referensi Log 3 juga tidak valid. Demikian pula Log 5. Seluruh rantai setelah Log 3 terdeteksi rusak.

Inilah yang dimaksud dengan immutability — ketidakterubahan. Log audit tidak dapat diubah, dihapus, maupun direkayasa tanpa terdeteksi. [jeda] Hash SHA-256 menjamin deteksi perubahan satu byte seketika. Log disimpan dalam media WORM — Write Once Read Many — sehingga tidak dapat ditimpa. Dan setiap persetujuan wajib menggunakan TTE untuk kekuatan hukum non-repudiation.

Pesan untuk Manajemen Atas: jangan percaya pada sistem yang hanya menjanjikan log audit. Pastikan sistem tersebut memiliki mekanisme hash chain dan penyimpanan terpisah yang tidak dapat dimanipulasi oleh administrator."

---

### Slide 18 — Langkah Perancangan Audit Trail

"Bagaimana cara merancang audit trail di unit kerja Anda? [tunjuk layar]

Terdapat empat langkah tata kelola. Pertama, tetapkan 14 field metadata sebagai standar wajib untuk semua sistem arsip. Kedua, integrasikan log dari berbagai sistem ke dalam SIEM pusat. Ketiga, tetapkan retensi log minimal sesuai klasifikasi arsip — arsip vital memerlukan retensi log lebih panjang. Keempat, tetapkan prosedur eskalasi jika terdeteksi anomali, seperti akses di luar jam kerja atau unduhan massal.

Validasi kritis: periksa apakah log disimpan terpisah dari database aplikasi. [jeda] Jika log dan data aplikasi berada di server yang sama, administrator dapat menghapus keduanya sekaligus. Periksa apakah hash diverifikasi secara otomatis setiap hari. Dan periksa apakah auditor internal memiliki akses read-only ke log tanpa melalui unit IT.

Pertanyaan kuncinya adalah: jika hari ini terjadi kebocoran, bisakah kita tunjukkan siapa yang mengakses dalam enam bulan terakhir dalam waktu kurang dari satu jam? Jika jawabannya tidak yakin, berarti audit trail kita belum siap."

---

### Slide 19 — Output & Workshop: Pilar 2 (Audit Trail)

"Workshop kedua meminta Bapak-Ibu merancang alur audit trail untuk satu proses bisnis. [tunjuk layar]

Te# Slide 19 — Section Divider: Pilar 3 — Kebijakan ISMS

"Kita selesai dengan Pilar 2. Sekarang kita masuk ke Pilar ketiga: Kebijakan Keamanan Terintegrasi dengan ISMS. [jeda] Di bagian ini, kita akan merumuskan aturan main yang mengikat secara hukum."

---

## BAGIAN III: PILAR 3 — KEBIJAKAN ISMS (10 Menit)

### Slide 20akan pada lembar kerja. [jeda] Setelah kita memastikan siapa yang boleh masuk dan setiap aktivitas tercatat, pertanyaan berikutnya adalah: aturan mainnya apa? Siapa yang bertanggung jawab jika terjadi pelanggaran? Jawabannya ada di Pilar ketiga: Kebijakan ISMS."

---

## BAGIAN III: PILAR 3 — KEBIJAKAN ISMS (10 Menit)

### Slide 21 — Mengapa Kebijakan Berurutan setelah RBAC & Audit Trail?

"RBAC adalah pintu dan kunci. Audit trail adalah kamera pengawas. Kebijakan ISMS adalah peraturan perusahaan yang memberikan kekuatan hukum agar pintu tidak dibuka sembarangan dan kamera tidak dimatikan. [jeda]

Tanpa kebijakan yang mengikat, RBAC dapat diabaikan dengan alasan darurat. Tanpa kebijakan, log audit dapat dihentikan dengan alasan performa sistem. Kebijakan adalah fondasi legal yang membuat teknologi keamanan menjadi kewajiban, bukan pilihan.

Standar yang kita gunakan adalah ISO IEC 27001:2022, yang memuat 93 kontrol keamanan dalam empat kelompok: Organizational, People, Physical, dan Technological. [tunjuk layar] Arsip digital dikategorikan sebagai aset informasi kritis yang harus dilindungi. Dan NIST Cybersecurity Framework memberikan referensi praktikal global untuk perancangan kebijakan, termasuk SP 800-53 dan SP 800-207 mengenai Zero Trust."

---

### Slide 22 — Siklus PDCA: Fondasi ISO 27001

"ISO 27001 dibangun di atas siklus PDCA yang berkelanjutan. [tunjuk layar]

Plan: menyusun kebijakan dan menilai risiko. Do: mengimplementasikan kontrol keamanan. Check: mengaudit dan mengevaluasi efektivitas. Act: melakukan perbaikan berkelanjutan. Siklus ini berputar terus-menerus, bukan sekali jalan.

Di PLN, penerapannya adalah sebagai berikut. [jeda] Plan: Unit Kearsipan bersama GCG menyusun kebijakan keamanan arsip berdasarkan risiko unit. Do: IT mengimplementasikan RBAC, audit trail, dan enkripsi sesuai kebijakan. Check: SPI melakukan audit internal setiap semester. Act: hasil audit menjadi masukan perbaikan kebijakan dan teknologi.

Sebagai Manajemen Atas, Anda bukan pelaksana siklus ini, tetapi Anda adalah penjamin bahwa siklus ini berjalan. Anda yang mengesahkan kebijakan, menetapkan anggaran audit, dan menindaklanjuti temuan."

---

### Slide 23 — Tiga Prinsip Fundamental Kebijakan

"Terdapat tiga prinsip fundamental yang harus tertuang dalam setiap kebijakan keamanan arsip PLN. [tunjuk layar]

Pertama, Least Privilege — hak akses minimum. Setiap permintaan akses harus diverifikasi secara eksplisit, tidak diberikan secara default. Kedua, Defense in Depth — pertahanan berlapis. Lima lapisan: kebijakan, fisik, jaringan, aplikasi, dan data. Jika satu lapisan jebol, masih ada lapisan lain yang melindungi. Ketiga, Zero Trust — tidak ada akses default meskipun dari dalam jaringan internal. Setiap akses harus diverifikasi berkelanjutan berdasarkan konteks: peran, perangkat, lokasi, dan waktu.

Zero Trust sangat relevan untuk PLN karena jaringan kita tersebar di seluruh Indonesia. [jeda] Seorang pegawai yang mengakses arsip vital dari kantor pusat di Jakarta mungkin diizinkan. Tetapi akses yang sama dari lokasi yang tidak dikenal pada pukul dua dini hari harus ditolak atau setidaknya memerlukan verifikasi tambahan.

Prinsip-prinsip ini harus tertuang dalam kebijakan tertulis, bukan hanya dipahami secara informal."

---

### Slide 24 — Integrasi GCG BUMN: Prinsip TARIF

"Sebagai BUMN, kebijakan keamanan arsip PLN tidak boleh lepas dari prinsip Tata Kelola Perusahaan yang Baik. [tunjuk layar]

Prinsip TARIF. Transparansi: audit trail dapat diakses auditor internal dan eksternal sesuai kewenangan. Akuntabilitas: setiap aksi terikat identitas dan TTE, dengan RACI digital yang jelas. Responsibilitas: kepatuhan terhadap PP 71 Tahun 2019 dan Perka ANRI wajib diuji secara berkala. Independensi: Unit Kearsipan berwenang menolak arsip yang tidak memenuhi standar metadata, tanpa intervensi unit pemilik. Fairness: akses berbasis need-to-know, tidak diskriminatif, dan terdapat mekanisme banding.

Perhatikan prinsip Independensi. [jeda] Ini penting. Unit Kearsipan harus memiliki kewenangan untuk menolak menerima arsip dari unit lain jika arsip tersebut tidak memenuhi standar metadata atau klasifikasi keamanan. Tanpa kewenangan ini, arsip berkualitas rendah akan masuk ke dalam sistem dan merusak integritas koleksi.

Sebagai Manajemen Atas, Anda harus menunjukkan komitmen dengan cara meninjau kebijakan secara berkala minimal tahunan. Kebijakan yang tidak ditinjau akan menjadi usang dan kehilangan kekuatan hukumnya."

---

### Slide 25 — Template Kerangka Kebijakan Keamanan Arsip

"Inilah enam klausul minimum yang harus ada dalam setiap kebijakan keamanan arsip. [tunjuk layar]

Klausul 1: Ruang Lingkup — menetapkan bahwa kebijakan ini berlaku untuk seluruh unit kerja dan seluruh jenis arsip digital. Klausul 2: Klasifikasi dan Labeling — menetapkan empat tingkat klasifikasi: Publik, Terbatas, Rahasia, Vital. Klausul 3: Hak Akses dan RBAC — mengacu pada Matriks RBAC yang telah disusun.

Klausul 4: Audit Trail dan Monitoring — mensyaratkan 14 field metadata dan hash chain. Klausul 5: Tindak Lanjut Pelanggaran — menetapkan sanksi administratif dan pidana sesuai tingkat pelanggaran. Klausul 6: Review dan Revisi — menetapkan jadwal review minimal tahunan dan pemicu revisi darurat.

Kebijakan ini harus terintegrasi dengan ISMS organisasi, bukan dokumen yang berdiri sendiri. [jeda] Jika unit GCG sudah memiliki kebijakan ISO 27001, maka kebijakan arsip harus menjadi lampiran atau referensi silang yang tidak bertentangan."

---

### Slide 26 — Langkah Perumusan Kebijakan

"Proses perumusan kebijakan mengikuti lima tahapan. [tunjuk layar]

Pertama, analisis risiko: identifikasi ancaman dan dampaknya terhadap arsip unit. Kedua, penyusunan draf oleh tim lintas fungsi: Kearsipan, IT, Hukum, dan GCG. Ketiga, konsultasi internal dengan unit terkait untuk memastikan kebijakan dapat diimplementasikan. Keempat, pengesahan oleh Manajemen Atas sebagai penanggung jawab tertinggi tata kelola. Kelima, sosialisasi dan review berkala.

Peran Manajemen Atas di sini sangat krusial. [jeda] Anda yang mengesahkan kebijakan, menetapkan tanggal efektif, menunjuk penanggung jawab implementasi, dan memastikan review berkala minimal tahunan. Tanpa tanda tangan Anda, kebijakan ini hanya menjadi dokumen diskusi tanpa kekuatan mengikat.

Satu hal lagi: jangan biarkan kebijakan disusun hanya oleh unit IT. Kebijakan keamanan arsip adalah kebijakan bisnis, bukan kebijakan teknis."

---

### Slide 27 — Output & Workshop: Pilar 3 (Kebijakan ISMS)

"Workshop ketiga meminta Bapak-Ibu menyusun rancangan kebijakan keamanan arsip. [tunjuk layar]

Id# Slide 26 — Section Divider: Pilar 4 — Backup & DR

"Kita selesai dengan Pilar 3. Sekarang kita masuk ke Pilar keempat dan terakhir: Backup dan Disaster Recovery. [jeda] Di bagian ini, kita akan memastikan arsip tetap tersedia meskipun terjadi kegagalan sistem atau bencana."

---

## BAGIAN IV: PILAR 4 — BACKUP & DR (7 Menit)

### Slide 27akan pada lembar kerja. [jeda] Setelah kita memiliki aturan main yang jelas, pertanyaan terakhir adalah: bagaimana jika semua sistem gagal? Bagaimana jika terjadi bencana? Jawabannya ada di Pilar keempat: Backup dan Disaster Recovery."

---

## BAGIAN IV: PILAR 4 — BACKUP & DR (7 Menit)

### Slide 28 — Strategi Backup 3-2-1 untuk Arsip PLN

"Kita masuk ke pilar terakhir: memastikan arsip tetap tersedia meskipun terjadi kegagalan. [tunjuk layar]

Strategi yang kita gunakan adalah 3-2-1. Tiga salinan data: satu salinan produksi dan dua salinan cadangan. Dua media berbeda: misalnya NAS atau tape untuk cadangan lokal, dan cloud atau offsite untuk cadangan jarak jauh. Satu salinan disimpan di lokasi geografis terpisah untuk melindungi dari bencana regional.

Mengapa tidak cukup dengan satu cadangan di server yang sama? [jeda] Karena jika server tersebut rusak akibat kebakaran, ransomware, atau kerusakan fisik, cadangan di server yang sama juga ikut hilang. Cadangan harus terpisah secara fisik dan geografis.

Sebagai Manajemen Atas, Anda tidak perlu memilih merek tape atau cloud provider. Tetapi Anda wajib memastikan bahwa strategi 3-2-1 tertuang dalam kontrak dengan vendor dan diaudit secara berkala."

---

### Slide 29 — RTO & RPO: Target Pemulihan Berbasis Klasifikasi

"Dua metrik kritis dalam perancangan DR adalah RTO dan RPO. [tunjuk layar]

RTO — Recovery Time Objective — adalah waktu maksimal yang diizinkan untuk memulihkan sistem agar bisnis dapat berjalan kembali. RPO — Recovery Point Objective — adalah waktu maksimal kehilangan data yang masih dapat ditoleransi. Semakin vital arsipnya, semakin ketat target RTO dan RPO-nya.

Untuk arsip Vital, RTO maksimal 4 jam dan RPO maksimal 15 menit. Artinya, jika sistem gagal pukul 08.00, maka paling lambat pukul 12.00 sistem harus berjalan kembali, dan data yang hilang tidak boleh lebih dari 15 menit sebelum kegagalan. [jeda] Untuk arsip Rahasia, RTO 8 jam dan RPO 1 jam. Untuk arsip Terbatas, RTO 24 jam dan RPO 4 jam. Untuk arsip Publik, RTO 72 jam dan RPO 24 jam.

RTO dan RPO adalah keputusan strategis, bukan teknis semata. [jeda] Target yang terlalu ketat memerlukan biaya infrastruktur yang sangat tinggi. Target yang terlalu longgar membahayakan kelangsungan operasional. Anda sebagai Manajemen Atas harus menetapkan target ini berdasarkan dampak bisnis, bukan berdasarkan kemampuan teknis semata."

---

### Slide 30 — Business Continuity Plan (BCP): Siklus Hidup ISO 22301

"Backup dan DR tidak berdiri sendiri. Mereka adalah bagian dari Business Continuity Plan yang mengikuti siklus hidup ISO 22301. [tunjuk layar]

Lima fase iteratif. Pertama, analisis dampak bisnis: menentukan proses kritis dan prioritas pemulihan. Kedua, perancangan strategi pemulihan: menetapkan RTO, RPO, dan lokasi cadangan. Ketiga, implementasi solusi cadangan: konfigurasi teknis dan pengujian awal. Keempat, simulasi dan latihan: memastikan tim siap saat bencana terjadi. Kelima, review dan perbaikan: memperbarui BCP berdasarkan hasil simulasi dan perubahan bisnis.

Pemeliharaan BCP memerlukan simulasi minimal enam bulan sekali. [jeda] Banyak organisasi yang menyusun BCP dengan bagus, tetapi tidak pernah mensimulasikannya. Saat bencana benar-benar terjadi, mereka menemukan bahwa prosedur tidak berjalan, kontak darurat tidak aktif, atau cadangan data tidak dapat dipulihkan.

Jangan biarkan PLN menjadi organisasi seperti itu. Simulasi adalah investasi, bukan pengeluaran."

---

### Slide 31 — Langkah Perancangan Sistem Backup/DR

"Bagaimana cara merancang sistem backup dan DR di unit kerja Anda? [tunjuk layar]

Empat langkah tata kelola. Pertama, klasifikasikan arsip berdasarkan dampak bisnis jika hilang. Kedua, tetapkan target RTO dan RPO untuk setiap klasifikasi. Ketiga, pilih strategi 3-2-1 dengan lokasi offsite yang terpisah secara geografis. Keempat, tetapkan prosedur fallback manual jika sistem otomatis gagal.

Dari sisi kesiapan organisasi: tetapkan tim tanggap darurat dengan nomor kontak 24 jam. [jeda] Sediakan dokumentasi pemulihan yang diperbarui setiap perubahan sistem. Dan jadwalkan simulasi pemulihan minimal dua kali setahun.

Pertanyaan kuncinya adalah: jika arsip vital musnah besok, berapa kerugian finansial per jamnya, dan apakah kita siap menghadapi regulator dengan bukti bahwa kita telah melakukan yang wajib dilakukan? Jika Anda tidak dapat menjawab dengan yakin, berarti DR Anda belum siap."

---

### Slide 32 — Output & Workshop: Pilar 4 (Backup & DR)

"Workshop keempat meminta Bapak-Ibu menyusun rencana backup dan DR. [tunjuk layar]

Te# Slide 31 — Section Divider: Studi Kasus

"Kita selesai dengan keempat pilar. Sekarang kita masuk ke Bagian III: Studi Kasus Integratif. [jeda] Di bagian ini, kita akan menguji apakah keempat pilar benar-benar bekerja saat terjadi insiden kebocoran arsip."

---

## BAGIAN V: STUDI KASUS INTEGRATIF (3 Menit)

### Slide 32akan pada lembar kerja. [jeda] Keempat pilar telah kita bahas. Sekarang saatnya kita uji apakah keempat pilar ini benar-benar bekerja saat terjadi insiden. Kita masuk ke studi kasus integratif."

---

## BAGIAN V: STUDI KASUS INTEGRATIF (3 Menit)

### Slide 33 — Skenario Insiden

"Perhatikan skenario berikut. [tunjuk layar]

Senin pukul 08.00, Manajer Keuangan Unit Bisnis PLN XYZ menemukan bahwa dokumen kontrak jangka panjang dengan vendor strategis telah diunduh oleh tiga orang tidak berwenang pada Jumat malam pukul 23.45. Status dokumen: Rahasia. Tidak ada notifikasi otomatis yang terkirim ke unit keamanan. Staf administrasi menemukan anomali tersebut secara kebetulan saat memeriksa log.

Pertanyaan strategisnya: apakah keempat pilar keamanan kita berfungsi? Di mana letak kelemahan sistemiknya? [jeda] Mari kita bedah satu per satu."

---

### Slide 34 — Analisis: Pilar 1 (RBAC) & Pilar 2 (Audit Trail)

"Dari sisi Pilar 1, RBAC: terdapat kelemahan pada provisioning akses. Pegawai yang sudah mutasi ke unit lain masih memiliki hak akses ke arsip Rahasia. Tidak ada mekanisme de-provisioning otomatis yang terintegrasi dengan HRIS. Dan tidak ada penerapan least privilege — beberapa akun memiliki hak akses yang lebih luas dari tugasnya.

Dari sisi Pilar 2, Audit Trail: log tercatat, tetapi tidak ada SIEM yang menganalisis secara proaktif. [jeda] Unduhan pada pukul 23.45 seharusnya memicu alert otomatis. Hash chain ada, tetapi tidak ada mekanisme verifikasi harian. Artinya, jika log diubah pada hari Sabtu, kecurangan tersebut baru akan terdeteksi jika seseupan secara manual memeriksa hash — yang dalam kasus ini tidak terjadi.

Dua pilar ini gagal mencegah dan mendeteksi insiden secara dini."

---

### Slide 35 — Analisis: Pilar 3 (Kebijakan) & Pilar 4 (Backup/DR)

"Dari sisi Pilar 3, Kebijakan ISMS: kebijakan keamanan arsip memang ada, tetapi tidak diintegrasikan dengan kebijakan ISO 27001 unit. Tidak ada klausul yang secara eksplisit melarang akses di luar jam kerja untuk arsip Rahasia. Dan tidak ada prosedur tindak lanjut pelanggaran yang jelas — sehingga saat insiden terjadi, unit bingung harus melapor ke siapa.

Dari sisi Pilar 4, Backup/DR: cadangan data memang ada, tetapi tidak teruji. [jeda] RTO untuk arsip Rahasia tidak pernah ditetapkan secara formal. Dan yang lebih membahayakan: tidak ada prosedur untuk memulihkan log audit yang mungkin ikut terhapus jika insiden ini disebabkan oleh ransomware.

Empat pilar ini seharusnya saling melindungi. Tetapi karena masing-masing dirancang secara parsial tanpa koordinasi, celah di satu pilar langsung menjadi celah di seluruh sistem."

--# Slide 35 — Section Divider: Validasi & Penutup

"Kita selesai dengan studi kasus. Sekarang kita masuk ke bagian terakhir: Validasi, Portofolio, dan Executive Tollgate. [jeda] Di bagian ini, kita akan merangkum empat dokumen portofolio yang harus Anda kumpulkan."

---

## BAGIAN VI: VALIDASI, PORTOFOLIO & PENUTUP

### Slide 36 — Pelajaran untuk Manajemen Atas

"Pelajaran utama dari skenario ini adalah: sistem keamanan harus terintegrasi, bukan parsial. [tunjuk layar]

Kelemahan pada satu pilar akan menetralisasi kekuatan pilar lainnya. RBAC yang tidak detail menciptakan celah akses. Audit trail yang tidak dianalisis membuat deteksi terlambat. Kebijakan yang tidak mengikat membuat sanksi tidak dapat diterapkan. Dan tanpa backup teruji, dampak insiden tidak dapat dipulihkan.

Saya minta Bapak-Ibu melakukan refleksi mandiri. [interaksi] Identifikasi minimal dua celah keamanan yang berpotensi terjadi di unit Anda. Tentukan tindakan perbaikan per pilar, penanggung jawab, dan timeline. Tuliskan di lembar refleksi. [jeda] Ini bukan latihan teoretis. Ini adalah diagnosis awal yang bisa Anda bawa ke rapat manajemen minggu depan."

---

## BAGIAN VI: VALIDASI, PORTOFOLIO & PENUTUP

### Slide 37 — Pemetaan Portofolio & Kriteria Penilaian

"Mari kita rangkum empat portofolio yang harus Bapak-Ibu kumpulkan. [tunjuk layar]

Portofolio 1 untuk kriteria 4.4.1: Matriks RBAC dan Prosedur Akses. Portofolio 2 untuk kriteria 4.4.2: Diagram Alur Audit Trail dan Template 14 Field. Portofolio 3 untuk kriteria 4.4.3: Rancangan Kebijakan Keamanan Arsip. Portofolio 4 untuk kriteria 4.4.4: Matriks RTO/RPO dan Rencana DR.

Masing-masing memiliki bobot 25 persen. Kriteria kelulusan: keempat dokumen lengkap, skor rubrik minimal 70, post-test minimal 65, dan komitmen tindak lanjut tertulis. [jeda]

Perlu diingat: keempat portofolio bersifat kumulatif dan terintegrasi. Pilar 1 menjadi input Pilar 2, yang menjadi input Pilar 3, dan seterusnya. Jangan menyusunnya sebagai dokumen yang saling lepas."

---

### Slide 38 — Executive Tollgate: 4 Gate Sebelum Implementasi

"Sebelum Bapak-Ibu mengusulkan implementasi kebijakan keamanan ini di unit kerja, terdapat empat gerbang keputusan yang harus dilewati. [tunjuk layar]

Gate 1: Legal Compliance — apakah kebijakan selaras dengan ISO 15489, PP 71 Tahun 2019, dan tata naskah dinas? Gate 2: Data Integrity — apakah audit trail dan TTE sudah menjamin keaslian arsip? Gate 3: Operational Value — apakah skema RBAC sudah mengurangi risiko akses tidak berwenang? Gate 4: Scalability — apakah infrastruktur backup siap untuk volume data jangka panjang?

Jika keempat gate berwarna hijau, Anda siap untuk go-live. [jeda] Jika ada yang masih merah, mundur satu langkah. Evaluasi ulang di bagian perancangan. Jangan pernah memaksakan implementasi yang belum siap, karena kegagalan implementasi keamanan lebih berbahaya daripada tidak ada implementasi sama sekali — karena kegagalan menciptakan rasa aman palsu."

---

### Slide 39 — Refleksi & Komitmen Tindak Lanjut

"Bapak-Ibu, kita telah membahas banyak hal hari ini — dari prinsip least privilege sampai strategi 3-2-1. Tetapi yang menentukan apakah semua ini berdampak atau tidak, ada di tangan masing-masing dari Anda. [jeda]

Saya minta Bapak-Ibu menjawab tiga pertanyaan. [tunjuk layar] Pertama, apa satu klasifikasi arsip yang paling rentan di unit Anda? Kedua, siapa yang harus Anda ajak bicara pertama kali — IT, GCG, atau Unit Kearsipan? Ketiga, hambatan apa yang paling mungkin muncul saat implementasi, dan bagaimana Anda akan mengatasinya?

Kemudian isi Lembar Komitmen 30 Hari. Tuliskan nama Anda, proses yang akan Anda amankan, target KPI-nya, dan tanggal pelaporan. [jeda] Komitmen ini bukan untuk saya. Ini untuk unit kerja Anda dan untuk masa depan tata kelola informasi PLN."

---

### Slide 40 — Terima Kasih & Dukungan Pasca Pelatihan

"Bapak dan Ibu yang saya hormati, kita telah sampai di akhir Modul 4.4. [jeda]

Saya ingin menutup dengan satu pesan: keamanan arsip bukan tentang teknologi. Keamanan arsip adalah tentang kepercayaan. Kepercayaan bahwa setiap keputusan bisnis yang kita ambil memiliki bukti yang sah. Kepercayaan bahwa jika terjadi sengketa, kita dapat membuktikan apa yang terjadi. Dan kepercayaan bahwa meskipun terjadi bencana, memori korporat PLN tetap terjaga.

Setelah pelatihan ini, Anda tidak sendirian. Center of Excellence Records Management PLN tersedia untuk konsultasi teknis. Komunitas PLN Archives Champion dapat menjadi wadah bertukar praktik terbaik. Dan pendampingan pilot project tersedia per unit.

Empat langkah selanjutnya: kerjakan post-test di LMS PLN, kumpulkan keempat portofolio ke Unit Kearsipan, jadwalkan peer review antar unit, dan gunakan modul ini sebagai acuan Annual Security Improvement Plan.

Terima kasih atas perhatian dan partisipasi aktif Bapak-Ibu. Selamat bekerja, dan salam transformasi."

---

> **Catatan Teknis:** Total slide: 40 (termasuk 6 section divider). Durasi fasilitasi: 45 menit (Fondasi 5, RBAC 10, Audit 10, ISMS 10, DR 7, Kasus 3). Workshop mandiri: 4×30 menit.
