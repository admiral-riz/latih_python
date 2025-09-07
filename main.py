# Program pembelajaran dasar Python sesuai roadmap

# =========================
# Bagian Sederhana
# =========================

print("Belajar Dasar Python")  # Menampilkan teks ke layar

# Variables and Data Types
nama = "Andi"
umur = 20
tinggi = 1.75
is_student = True
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa?", is_student)

# Type Casting
umur_str = str(umur)
tinggi_int = int(tinggi)
print("Umur (string):", umur_str)
print("Tinggi (int):", tinggi_int)

# Conditionals
if umur >= 18:
    print("Sudah dewasa")
else:
    print("Masih anak-anak")

# Loops
print("Cetak angka 1 sampai 5:")
for i in range(1, 6):
    print(i)

# Exceptions
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Terjadi pembagian dengan nol!")

# Functions & Builtin Functions
def sapa(nama):
    print("Halo,", nama)

sapa("Budi")
print("Panjang nama:", len(nama))

# Lists
buah = ["apel", "jeruk", "mangga"]
print("List buah:", buah)
buah.append("pisang")
print("List buah setelah ditambah:", buah)

# Tuples
warna = ("merah", "biru", "hijau")
print("Tuple warna:", warna)

# Sets
angka_unik = {1, 2, 3, 3, 2}
print("Set angka unik:", angka_unik)

# Dictionaries
mahasiswa = {"nama": "Siti", "umur": 19, "jurusan": "Informatika"}
print("Dictionary mahasiswa:", mahasiswa)

# =========================
# Bagian Kompleks
# =========================

print("\n=== Bagian Kompleks ===")

# Fungsi dengan parameter default dan return value
def hitung_gaji(jam_kerja, upah_per_jam=20000):
    return jam_kerja * upah_per_jam

gaji = hitung_gaji(40)
print(f"Gaji mingguan: {gaji}")

# List komprehensi dan manipulasi data
angka = [i for i in range(1, 11)]
kuadrat = [x**2 for x in angka]
print("Angka:", angka)
print("Kuadrat:", kuadrat)

# Nested dictionary dan akses data
data_mahasiswa = {
    "001": {"nama": "Andi", "nilai": [80, 90, 85]},
    "002": {"nama": "Siti", "nilai": [88, 92, 79]},
}
for nim, info in data_mahasiswa.items():
    rata2 = sum(info["nilai"]) / len(info["nilai"])
    print(f"NIM: {nim}, Nama: {info['nama']}, Rata-rata nilai: {rata2:.2f}")

# Penggunaan lambda dan fungsi map/filter
angka_ganjil = list(filter(lambda x: x % 2 != 0, angka))
print("Angka ganjil:", angka_ganjil)
hasil_map = list(map(lambda x: x * 10, angka))
print("Angka dikali 10:", hasil_map)

# Error handling dengan multiple exception
try:
    nilai = int(input("Masukkan nilai: "))
    print("Nilai yang dimasukkan:", nilai)
except ValueError:
    print("Input bukan angka!")
except Exception as e:
    print("Terjadi error lain:", e)

# Class dan OOP sederhana
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
print(f"Mahasiswa: {mhs1.nama}, Rata-rata: {mhs1.rata_rata()}")

# Penggunaan modul eksternal (math)
import math
print("Akar dari 144:", math.sqrt(144))
print("Pi:", math.pi)

# Membaca dan menulis file
with open("contoh.txt", "w") as f:
    f.write("Ini contoh menulis file dengan Python.\n")

with open("contoh.txt", "r") as f:
    isi = f.read()
    print("Isi file:", isi)