# Latihan - Python

Repository ini berisi kumpulan contoh program sederhana untuk pembelajaran dasar bahasa pemrograman Python . Materi dan contoh kode disusun mengikuti roadmap fundamental Python agar mudah dipahami oleh pemula.

## Roadmap Materi

1. **Basic Syntax**  
   Penjelasan tentang cara penulisan kode Python yang benar, seperti penggunaan indentasi dan penulisan perintah dasar.

2. **Variables and Data Types**  
   Cara membuat variabel dan mengenal tipe data utama di Python: string, integer, float, dan boolean.

3. **Type Casting**  
   Mengubah tipe data, misal dari integer ke string atau float ke integer, agar sesuai kebutuhan program.

4. **Conditionals**  
   Percabangan menggunakan `if`, `else`, dan `elif` untuk pengambilan keputusan berdasarkan kondisi tertentu.

5. **Loops**  
   Perulangan menggunakan `for` dan `while` untuk menjalankan kode secara berulang.

6. **Exceptions**  
   Penanganan error dengan `try`, `except`, agar program tidak berhenti saat terjadi kesalahan.

7. **Functions & Builtin Functions**  
   Membuat fungsi sendiri dengan `def` dan menggunakan fungsi bawaan Python seperti `len()`, `print()`, dll.

8. **Lists, Tuples, Sets**  
   Mengenal struktur data untuk menyimpan banyak nilai:

   - List: data yang bisa diubah
   - Tuple: data tetap
   - Set: data unik tanpa duplikat

9. **Dictionaries**  
   Struktur data untuk pasangan kunci-nilai, cocok untuk data terstruktur seperti biodata.

## Struktur Folder & File

- **src/main.py**  
  Berisi contoh kode untuk setiap materi roadmap di atas dalam bentuk aplikasi terminal.  
  Cocok untuk latihan langsung di command line atau IDE.

- **src/coba1.py**  
  Berisi contoh aplikasi web sederhana menggunakan Flask yang menampilkan semua materi roadmap Python secara interaktif di halaman web.  
  CSS terpisah di `src/style.css` untuk tampilan yang lebih rapi.

- **src/style.css**  
  File CSS untuk mempercantik tampilan web pada aplikasi Flask.

- **requirements.txt**  
  Daftar dependensi yang diperlukan, seperti Flask.

## Cara Instalasi dan Menjalankan coba1.py

1. Install Flask terlebih dahulu:
   ```sh
   pip install flask
   ```
2. Jalankan file aplikasi web:
   ```sh
   python src/coba1.py
   ```
3. Buka browser dan akses [http://localhost:5000](http://localhost:5000)  
   Tampilan web akan muncul dengan materi roadmap Python dan CSS.

## Tujuan

Memberikan pemahaman awal tentang sintaks dan konsep dasar Python sesuai roadmap untuk pemula, baik melalui aplikasi terminal (`main.py`) maupun aplikasi web interaktif (`coba1.py`).

## Catatan

- Fokus utama pembelajaran ada di `main.py` untuk latihan di terminal dan `coba1.py` untuk eksplorasi materi secara visual di web.
- File CSS (`style.css`) berada di folder `src` dan dilayani langsung oleh Flask.
- Semua contoh kode dapat dimodifikasi sesuai kebutuhan belajar.
