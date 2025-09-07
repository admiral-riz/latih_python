# Contoh aplikasi web sederhana dengan Flask, menampilkan materi dasar Python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Basic Syntax & Variables
    nama = "Andi"
    umur = 20
    tinggi = 1.75
    is_student = True

    # Type Casting
    umur_str = str(umur)
    tinggi_int = int(tinggi)

    # Conditionals
    if umur >= 18:
        status = "Sudah dewasa"
    else:
        status = "Masih anak-anak"

    # Loops
    loop_result = ""
    for i in range(1, 6):
        loop_result += f"{i} "

    # Exceptions
    try:
        hasil = 10 / 0
    except ZeroDivisionError:
        exception_msg = "Terjadi pembagian dengan nol!"

    # Functions & Builtin Functions
    def sapa(nama):
        return f"Halo, {nama}"

    sapa_result = sapa("Budi")
    panjang_nama = len(nama)

    # Lists
    buah = ["apel", "jeruk", "mangga"]
    buah.append("pisang")

    # Tuples
    warna = ("merah", "biru", "hijau")

    # Sets
    angka_unik = {1, 2, 3, 3, 2}

    # Dictionaries
    mahasiswa = {"nama": "Siti", "umur": 19, "jurusan": "Informatika"}

    # Gabungkan semua hasil ke HTML sederhana
    html = f"""
    <h2>Belajar Dasar Python (Web)</h2>
    <b>Nama:</b> {nama}<br>
    <b>Umur:</b> {umur}<br>
    <b>Tinggi:</b> {tinggi}<br>
    <b>Mahasiswa?</b> {is_student}<br>
    <b>Umur (string):</b> {umur_str}<br>
    <b>Tinggi (int):</b> {tinggi_int}<br>
    <b>Status:</b> {status}<br>
    <b>Cetak angka 1 sampai 5:</b> {loop_result}<br>
    <b>Exception:</b> {exception_msg}<br>
    <b>Fungsi sapa:</b> {sapa_result}<br>
    <b>Panjang nama:</b> {panjang_nama}<br>
    <b>List buah:</b> {buah}<br>
    <b>Tuple warna:</b> {warna}<br>
    <b>Set angka unik:</b> {angka_unik}<br>
    <b>Dictionary mahasiswa:</b> {mahasiswa}<br>
    """
    return html

if __name__ == '__main__':
    app.run()