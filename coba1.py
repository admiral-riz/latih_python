# Contoh aplikasi web sederhana dengan Flask, menampilkan materi dasar Python beserta penjelasannya

from flask import Flask, render_template_string, url_for, send_from_directory
import os
import math

app = Flask(__name__)

# Route untuk melayani file CSS dari folder src
@app.route('/src/<path:filename>')
def src(filename):
    return send_from_directory(os.path.join(app.root_path, 'src'), filename)

@app.route('/src/coba2')
def goto_coba2():
    return """
    <script>
        window.location.href = 'http://localhost:5000/';
    </script>
    """

@app.route('/')
def home():
    # =========================
    # Bagian Sederhana
    # =========================
    nama = "Andi"
    umur = 20
    tinggi = 1.75
    is_student = True
    umur_str = str(umur)
    tinggi_int = int(tinggi)
    if umur >= 18:
        status = "Sudah dewasa"
    else:
        status = "Masih anak-anak"
    loop_result = " ".join(str(i) for i in range(1, 6))
    try:
        hasil = 10 / 0
    except ZeroDivisionError:
        exception_msg = "Terjadi pembagian dengan nol!"
    def sapa(nama):
        return f"Halo, {nama}"
    sapa_result = sapa("Budi")
    panjang_nama = len(nama)
    buah = ["apel", "jeruk", "mangga"]
    buah.append("pisang")
    warna = ("merah", "biru", "hijau")
    angka_unik = {1, 2, 3, 3, 2}
    mahasiswa = {"nama": "Siti", "umur": 19, "jurusan": "Informatika"}

    # =========================
    # Bagian Kompleks
    # =========================
    def hitung_gaji(jam_kerja, upah_per_jam=20000):
        return jam_kerja * upah_per_jam
    gaji = hitung_gaji(40)
    angka = [i for i in range(1, 11)]
    kuadrat = [x**2 for x in angka]
    data_mahasiswa = {
        "001": {"nama": "Andi", "nilai": [80, 90, 85]},
        "002": {"nama": "Siti", "nilai": [88, 92, 79]},
    }
    data_mahasiswa_html = ""
    for nim, info in data_mahasiswa.items():
        rata2 = sum(info["nilai"]) / len(info["nilai"])
        data_mahasiswa_html += f"NIM: {nim}, Nama: {info['nama']}, Rata-rata nilai: {rata2:.2f}<br>"
    angka_ganjil = list(filter(lambda x: x % 2 != 0, angka))
    hasil_map = list(map(lambda x: x * 10, angka))
    # Error handling dengan multiple exception (simulasi input)
    try:
        nilai = int("80")  # Simulasi input
        nilai_msg = f"Nilai yang dimasukkan: {nilai}"
    except ValueError:
        nilai_msg = "Input bukan angka!"
    except Exception as e:
        nilai_msg = f"Terjadi error lain: {e}"
    class Mahasiswa:
        def __init__(self, nama, nim):
            self.nama = nama
            self.nim = nim
            self.nilai = []
        def tambah_nilai(self, nilai):
            self.nilai.append(nilai)
        def rata_rata(self):
            if self.nilai:
                return sum(self.nilai) / len(self.nilai)
            return 0
    mhs1 = Mahasiswa("Budi", "003")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(90)
    mhs1_msg = f"Mahasiswa: {mhs1.nama}, Rata-rata: {mhs1.rata_rata()}"
    akar_144 = math.sqrt(144)
    pi_val = math.pi
    isi_file = "Ini contoh menulis file dengan Python.\n"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Belajar Dasar Python (Web)</title>
        <link rel="stylesheet" href="{url_for('src', filename='style.css')}">
    </head>
    <body>
    <div class="container">
    <h2>Bagian Sederhana</h2>
    <div class="section"><b>Basic Syntax:</b> Menampilkan teks ke layar</div>
    <div class="section"><b>Variables and Data Types:</b><br>
    Nama: {nama}<br>
    Umur: {umur}<br>
    Tinggi: {tinggi}<br>
    Mahasiswa?: {is_student}</div>
    <div class="section"><b>Type Casting:</b><br>
    Umur (string): {umur_str}<br>
    Tinggi (int): {tinggi_int}</div>
    <div class="section"><b>Conditionals:</b><br>
    Status: {status}</div>
    <div class="section"><b>Loops:</b><br>
    Cetak angka 1 sampai 5: {loop_result}</div>
    <div class="section"><b>Exceptions:</b><br>
    {exception_msg}</div>
    <div class="section"><b>Functions & Builtin Functions:</b><br>
    Fungsi sapa: {sapa_result}<br>
    Panjang nama: {panjang_nama}</div>
    <div class="section"><b>Lists:</b><br>
    {buah}</div>
    <div class="section"><b>Tuples:</b><br>
    {warna}</div>
    <div class="section"><b>Sets:</b><br>
    {angka_unik}</div>
    <div class="section"><b>Dictionaries:</b><br>
    {mahasiswa}</div>

    <h2>Bagian Kompleks</h2>
    <div class="section"><b>Fungsi dengan parameter default dan return value:</b><br>
    Gaji mingguan: {gaji}</div>
    <div class="section"><b>List komprehensi dan manipulasi data:</b><br>
    Angka: {angka}<br>
    Kuadrat: {kuadrat}</div>
    <div class="section"><b>Nested dictionary dan akses data:</b><br>
    {data_mahasiswa_html}</div>
    <div class="section"><b>Penggunaan lambda dan fungsi map/filter:</b><br>
    Angka ganjil: {angka_ganjil}<br>
    Angka dikali 10: {hasil_map}</div>
    <div class="section"><b>Error handling dengan multiple exception:</b><br>
    {nilai_msg}</div>
    <div class="section"><b>Class dan OOP sederhana:</b><br>
    {mhs1_msg}</div>
    <div class="section"><b>Penggunaan modul eksternal (math):</b><br>
    Akar dari 144: {akar_144}<br>
    Pi: {pi_val}</div>
    <div class="section"><b>Membaca dan menulis file:</b><br>
    Isi file: {isi_file}</div>
    <div style="margin-top:30px;">
        <a href="/src/coba2"><button style="padding:10px 20px;">Ke Web Dev (coba2.py)</button></a>
    </div>
    </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run()