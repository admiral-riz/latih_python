from flask import Blueprint, render_template_string, url_for
import math

coba1_bp = Blueprint("coba1", __name__)

@coba1_bp.route("/")
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

    # =========================
    # HTML Output
    # =========================
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coba1 - Materi Dasar Python</title>
        <link rel="stylesheet" href="/src/style.css">
    </head>
    <body>
        <div class="container">
        <h2>Bagian Sederhana</h2>
        <div class="section"><b>Variables:</b><br>
        Nama: {nama}<br>Umur: {umur}<br>Tinggi: {tinggi}<br>Mahasiswa?: {is_student}</div>
        <div class="section"><b>Type Casting:</b> Umur (str): {umur_str}, Tinggi (int): {tinggi_int}</div>
        <div class="section"><b>Conditionals:</b> {status}</div>
        <div class="section"><b>Loops:</b> {loop_result}</div>
        <div class="section"><b>Exceptions:</b> {exception_msg}</div>
        <div class="section"><b>Functions:</b> {sapa_result}, Panjang nama: {panjang_nama}</div>
        <div class="section"><b>Lists:</b> {buah}</div>
        <div class="section"><b>Tuples:</b> {warna}</div>
        <div class="section"><b>Sets:</b> {angka_unik}</div>
        <div class="section"><b>Dictionaries:</b> {mahasiswa}</div>

        <h2>Bagian Kompleks</h2>
        <div class="section"><b>Fungsi default:</b> Gaji mingguan: {gaji}</div>
        <div class="section"><b>List comprehension:</b> Angka: {angka}, Kuadrat: {kuadrat}</div>
        <div class="section"><b>Nested dict:</b><br>{data_mahasiswa_html}</div>
        <div class="section"><b>Lambda & map/filter:</b> Ganjil: {angka_ganjil}, x10: {hasil_map}</div>
        <div class="section"><b>Error handling:</b> {nilai_msg}</div>
        <div class="section"><b>Class & OOP:</b> {mhs1_msg}</div>
        <div class="section"><b>Modul math:</b> √144 = {akar_144}, π = {pi_val}</div>
        <div class="section"><b>File I/O:</b> {isi_file}</div>

        <div style="margin-top:30px;">
            <a href="{url_for('coba2.home')}"><button>Ke Web Dev (coba2.py)</button></a>
        </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)
