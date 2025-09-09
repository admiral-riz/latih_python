Sip 👍 saya bikin README **lebih lengkap lagi**, isinya detail + visualisasi + instruksi tambahan, biar seperti dokumentasi project open source profesional.

---

````markdown
# 📘 Latihan - Python

Repository ini berisi kumpulan **contoh program Python** yang disusun sesuai roadmap fundamental Python.  
Materi mencakup sintaks dasar, struktur data, OOP, hingga aplikasi web sederhana menggunakan **Flask**.

Tujuan utama project ini adalah menyediakan **pembelajaran terstruktur** untuk pemula, baik melalui **terminal (CLI)** maupun **web interaktif**.

---

## 📑 Roadmap Materi

Materi disusun sesuai urutan yang biasa ditemui saat belajar Python:

1. **Basic Syntax**

   - Cara menulis kode Python dengan benar.
   - Penggunaan `print()`, indentasi, komentar.

2. **Variables and Data Types**

   - String (`"teks"`), Integer (`123`), Float (`3.14`), Boolean (`True/False`).

3. **Type Casting**

   - Konversi antar tipe data (`str()`, `int()`, `float()`).

4. **Conditionals**

   - Percabangan `if`, `elif`, `else`.

5. **Loops**

   - Perulangan `for` & `while`.
   - Iterasi dengan `range()`.

6. **Exceptions**

   - Penanganan error dengan `try`, `except`.
   - Contoh: `ZeroDivisionError`.

7. **Functions & Builtin Functions**

   - Membuat fungsi (`def`).
   - Fungsi bawaan: `len()`, `print()`, `type()`.

8. **Lists, Tuples, Sets**

   - List: array dinamis.
   - Tuple: data tetap.
   - Set: data unik tanpa duplikat.

9. **Dictionaries**

   - Struktur data `key:value`.
   - Contoh: biodata mahasiswa.

10. **Object Oriented Programming (OOP)**

    - Membuat class & objek.
    - Method untuk tambah nilai, hitung rata-rata.

11. **File I/O**

    - Membaca & menulis file teks (`open`, `with`).

12. **Web Development dengan Flask**
    - Membuat server sederhana.
    - Routing dengan `Blueprint`.
    - Menyajikan data Python ke web.

---

## 📂 Struktur Folder & File

```bash
.
├── app.py            # Entry point Flask (menghubungkan coba1 & coba2)
├── main.py           # Program roadmap Python di terminal
├── coba1.py          # Blueprint Flask: Materi dasar & kompleks Python
├── coba2.py          # Blueprint Flask: Web sederhana (CRUD User)
├── src/
│   └── style.css     # CSS untuk mempercantik tampilan Flask
├── requirements.txt  # Daftar dependensi (Flask, requests)
└── README.md         # Dokumentasi project
```
````

---

## ⚙️ Instalasi

1. **Clone repository**

   ```sh
   git clone <url-repo>
   cd <folder-repo>
   ```

2. **Buat virtual environment** (opsional tapi disarankan)

   ```sh
   python -m venv venv
   source venv/bin/activate   # Linux / MacOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

---

## 🚀 Menjalankan Program

### 1. Mode Terminal (CLI)

Jalankan roadmap Python langsung di terminal:

```sh
python main.py
```

Output akan menampilkan contoh kode sesuai roadmap (variabel, loop, fungsi, class, dll).

---

### 2. Mode Web (Flask)

1. Jalankan server Flask:

   ```sh
   python app.py
   ```

2. Buka di browser:

   - [http://localhost:5000/coba1](http://localhost:5000/coba1) → **Materi Dasar Python**
   - [http://localhost:5000/coba2](http://localhost:5000/coba2) → **Aplikasi Web Dev** (daftar user & tambah user)

---

## 🎨 Tampilan Web

- **coba1**: Menampilkan roadmap Python (Bagian Sederhana & Kompleks)

  - Variabel, tipe data, perulangan, error handling, OOP, file I/O.
  - Disajikan dalam HTML yang rapi dengan CSS.

- **coba2**: Contoh aplikasi Web Development sederhana

  - **Home** → Deskripsi aplikasi.
  - **Daftar User** → Menampilkan tabel user.
  - **Tambah User** → Form input nama & email.
  - Tombol navigasi untuk pindah antar halaman.

- **style.css**: Menambahkan tampilan modern (container, card, tombol biru, tabel rapi).

---

## 📖 Contoh Output Terminal

```text
Belajar Dasar Python
+----------------+
|Bagian Sederhana|
+----------------+
Nama: Andi
Umur: 20
Tinggi: 1.75
Mahasiswa? True
Umur (string): 20
Tinggi (int): 1
Sudah dewasa
Cetak angka 1 sampai 5:
1
2
3
4
5
Terjadi pembagian dengan nol!
Halo, Budi
Panjang nama: 4
List buah: ['apel', 'jeruk', 'mangga']
List buah setelah ditambah: ['apel', 'jeruk', 'mangga', 'pisang']
Tuple warna: ('merah', 'biru', 'hijau')
Set angka unik: {1, 2, 3}
Dictionary mahasiswa: {'nama': 'Siti', 'umur': 19, 'jurusan': 'Informatika'}

+---------------+
|Bagian Kompleks|
+---------------+
Gaji mingguan: 800000
Angka: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Kuadrat: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
NIM: 001, Nama: Andi, Rata-rata nilai: 85.00
NIM: 002, Nama: Siti, Rata-rata nilai: 86.33
Angka ganjil: [1, 3, 5, 7, 9]
Angka dikali 10: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Masukkan nilai: _
```

---

## 🧑‍💻 Tujuan Pembelajaran

- Memahami **konsep dasar Python** (syntax, variabel, kondisi, loop, fungsi, OOP).
- Berlatih membuat program **di terminal** (CLI).
- Mengenal **Flask** untuk membuat aplikasi web sederhana.
- Menyusun program Python ke dalam **struktur project yang rapi**.

---

## 📝 Catatan

- Gunakan **main.py** untuk latihan di terminal.
- Gunakan **app.py** untuk aplikasi web (menghubungkan coba1 & coba2).
- Navigasi antar halaman web tersedia dengan tombol (`coba1 ↔ coba2`).
- Semua kode bisa dimodifikasi sesuai kebutuhan belajar.

---

## 📖 Referensi Tambahan

- [Python Official Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Roadmap](https://roadmap.sh/python)

---

## 🤝 Kontribusi

Kontribusi sangat terbuka:

- Menambahkan materi Python lanjutan.
- Membuat tampilan web lebih interaktif.
- Menambahkan latihan soal.

Langkah kontribusi:

1. Fork repository ini.
2. Buat branch baru (`git checkout -b fitur-baru`).
3. Commit perubahan (`git commit -m "Tambah materi OOP lanjutan"`).
4. Push branch (`git push origin fitur-baru`).
5. Buat Pull Request.

---

## 📜 Lisensi

Proyek ini dirilis dengan lisensi **MIT License**.
Silakan digunakan, dimodifikasi, dan dibagikan untuk tujuan belajar.

```

---

👉 README ini sudah **super lengkap**:
- Roadmap materi detail
- Struktur project
- Instalasi & penggunaan (CLI & Flask)
- Contoh output
- Tujuan belajar
- Referensi
- Kontribusi & lisensi


```
