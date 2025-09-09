# Latihan - Python

Repository ini berisi kumpulan contoh program sederhana untuk pembelajaran dasar bahasa pemrograman **Python**.  
Materi disusun mengikuti roadmap fundamental Python agar mudah dipahami oleh pemula, baik untuk latihan di terminal maupun eksplorasi melalui web interaktif dengan Flask.

---

## 🎯 Roadmap Materi

1. **Basic Syntax**

   - Penulisan kode Python yang benar (indentasi, statement dasar).
   - `print()` untuk menampilkan teks.

2. **Variables and Data Types**

   - String (`"teks"`), Integer (`123`), Float (`3.14`), Boolean (`True/False`).
   - Cara membuat dan menampilkan variabel.

3. **Type Casting**

   - Konversi antar tipe data, contoh: `int()`, `str()`, `float()`.

4. **Conditionals**

   - Percabangan logika dengan `if`, `elif`, `else`.

5. **Loops**

   - Perulangan `for` dan `while`.
   - Iterasi menggunakan `range()`.

6. **Exceptions**

   - Penanganan error dengan `try` dan `except`.
   - Contoh: pembagian dengan nol.

7. **Functions & Builtin Functions**

   - Membuat fungsi sendiri dengan `def`.
   - Menggunakan fungsi bawaan seperti `len()`, `print()`.

8. **Lists, Tuples, Sets**

   - **List**: data dinamis, bisa ditambah/ubah.
   - **Tuple**: data statis (immutable).
   - **Set**: data unik, tanpa duplikat.

9. **Dictionaries**

   - Menyimpan data dalam bentuk pasangan `key:value`.

10. **Object Oriented Programming (OOP)**

    - Membuat class & objek.
    - Method untuk tambah data dan hitung rata-rata.

11. **File I/O**
    - Membuat file teks baru dan menulis isi.
    - Membaca isi file.

---

## 📂 Struktur Folder & File

```bash
.
├── app.py            # Entry point Flask, menghubungkan coba1 & coba2
├── main.py           # Program latihan roadmap Python di terminal
├── coba1.py          # Blueprint Flask: materi dasar & kompleks Python (web)
├── coba2.py          # Blueprint Flask: aplikasi web sederhana (CRUD user)
├── src/
│   └── style.css     # CSS untuk mempercantik tampilan aplikasi Flask
├── requirements.txt  # Daftar dependensi (Flask, requests)
└── README.md         # Dokumentasi proyek
```

````

---

## ⚙️ Instalasi

1. Clone repository:

   ```sh
   git clone <url-repo-kamu>
   cd <folder-repo>
   ```

2. Buat virtual environment (opsional, tapi disarankan):

   ```sh
   python -m venv venv
   source venv/bin/activate   # Linux / MacOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependensi:

   ```sh
   pip install -r requirements.txt
   ```

---

## 🚀 Menjalankan Program

### Mode Terminal

Jalankan `main.py` untuk latihan dasar di terminal:

```sh
python main.py
```

Program akan menampilkan semua contoh roadmap Python langsung di console.

### Mode Web (Flask)

1. Jalankan aplikasi Flask:

   ```sh
   python app.py
   ```

2. Akses di browser:

   - [http://localhost:5000/coba1](http://localhost:5000/coba1) → Materi Dasar Python
   - [http://localhost:5000/coba2](http://localhost:5000/coba2) → Aplikasi Web Dev (user list & tambah user)

---

## 🎨 Tampilan Web

- **coba1.py** → menampilkan roadmap Python (Bagian Sederhana & Kompleks).
- **coba2.py** → aplikasi web dev sederhana: menampilkan daftar user & menambah user.
- **style.css** → mempercantik tampilan web agar lebih rapi dan interaktif.

Navigasi antar halaman tersedia melalui tombol:

- Dari **coba1** → pindah ke **coba2**.
- Dari **coba2** → kembali ke **coba1**.

---

## 🧑‍💻 Tujuan Proyek

- Memberikan pemahaman dasar sintaks dan konsep fundamental Python untuk pemula.
- Menyediakan **dua cara belajar**:

  1. **Terminal (main.py)** → fokus pada logika & sintaks dasar.
  2. **Web (app.py, coba1.py, coba2.py)** → eksplorasi materi secara visual & interaktif.

---

## 📝 Catatan

- `main.py` cocok untuk latihan langsung di command line / IDE.
- `app.py` menjalankan server Flask yang menghubungkan blueprint `coba1` & `coba2`.
- CSS (`style.css`) ada di folder `src` dan otomatis dilayani Flask.
- Semua kode bisa dimodifikasi sesuai kebutuhan belajar.

---

## 📖 Referensi Belajar Tambahan

- [Dokumentasi Resmi Python](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Roadmap untuk Pemula](https://roadmap.sh/python)

---

## 🤝 Kontribusi

Silakan fork repository ini, buat branch baru, lalu ajukan pull request jika ingin menambahkan fitur atau materi baru.
Contoh kontribusi: menambah materi Python lanjutan, mempercantik UI web, atau menambahkan contoh soal latihan.

---

## 📜 Lisensi

Proyek ini bebas digunakan untuk keperluan belajar.
Lisensi: **MIT License**.


````
