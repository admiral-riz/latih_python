# Contoh aplikasi web sederhana dengan Flask, menampilkan materi dasar Python beserta penjelasannya

from flask import Flask, render_template_string, url_for, send_from_directory
import os

app = Flask(__name__)

# Route untuk melayani file CSS dari folder src
@app.route('/src/<path:filename>')
def src(filename):
    return send_from_directory(os.path.join(app.root_path, 'src'), filename)

@app.route('/')
def home():
    # Basic Syntax & Variables
    nama = "Andi"         # Variabel bertipe string
    umur = 20             # Variabel bertipe integer
    tinggi = 1.75         # Variabel bertipe float
    is_student = True     # Variabel bertipe boolean

    # Type Casting
    umur_str = str(umur)      # Mengubah integer ke string
    tinggi_int = int(tinggi)  # Mengubah float ke integer

    # Conditionals
    # Percabangan untuk menentukan status berdasarkan umur
    if umur >= 18:
        status = "Sudah dewasa"
    else:
        status = "Masih anak-anak"

    # Loops
    # Perulangan untuk mencetak angka 1 sampai 5
    loop_result = ""
    for i in range(1, 6):
        loop_result += f"{i} "

    # Exceptions
    # Penanganan error jika terjadi pembagian dengan nol
    try:
        hasil = 10 / 0
    except ZeroDivisionError:
        exception_msg = "Terjadi pembagian dengan nol!"

    # Functions & Builtin Functions
    # Fungsi untuk menyapa seseorang
    def sapa(nama):
        return f"Halo, {nama}"

    sapa_result = sapa("Budi")  # Memanggil fungsi
    panjang_nama = len(nama)    # Fungsi bawaan untuk menghitung panjang string

    # Lists
    buah = ["apel", "jeruk", "mangga"]  # List untuk menyimpan beberapa data
    buah.append("pisang")               # Menambah data ke list

    # Tuples
    warna = ("merah", "biru", "hijau")  # Tuple untuk data yang tidak bisa diubah

    # Sets
    angka_unik = {1, 2, 3, 3, 2}        # Set untuk data unik (tidak ada duplikat)

    # Dictionaries
    mahasiswa = {"nama": "Siti", "umur": 19, "jurusan": "Informatika"}  # Dictionary untuk pasangan kunci-nilai

    # Gabungkan semua hasil ke HTML sederhana dengan penjelasan
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Belajar Dasar Python (Web)</title>
        <link rel="stylesheet" href="{url_for('src', filename='style.css')}">
    </head>
    <body>
    <div class="container">
    <h2>Belajar Dasar Python (Web)</h2>
    <div class="section"><b>Basic Syntax:</b> Menampilkan teks ke layar</div>
    <div class="section"><b>Variables and Data Types:</b> nama (string), umur (integer), tinggi (float), is_student (boolean)<br>
    Nama: {nama}<br>
    Umur: {umur}<br>
    Tinggi: {tinggi}<br>
    Mahasiswa?: {is_student}</div>
    <div class="section"><b>Type Casting:</b> Mengubah tipe data<br>
    Umur (string): {umur_str}<br>
    Tinggi (int): {tinggi_int}</div>
    <div class="section"><b>Conditionals:</b> Percabangan berdasarkan umur<br>
    Status: {status}</div>
    <div class="section"><b>Loops:</b> Perulangan mencetak angka 1 sampai 5<br>
    {loop_result}</div>
    <div class="section"><b>Exceptions:</b> Penanganan error pembagian dengan nol<br>
    Exception: {exception_msg}</div>
    <div class="section"><b>Functions & Builtin Functions:</b> Fungsi sapa dan len()<br>
    Fungsi sapa: {sapa_result}<br>
    Panjang nama: {panjang_nama}</div>
    <div class="section"><b>Lists:</b> List buah<br>
    {buah}</div>
    <div class="section"><b>Tuples:</b> Tuple warna<br>
    {warna}</div>
    <div class="section"><b>Sets:</b> Set angka unik<br>
    {angka_unik}</div>
    <div class="section"><b>Dictionaries:</b> Dictionary mahasiswa<br>
    {mahasiswa}</div>
    </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run()