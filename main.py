# Program pembelajaran dasar Python sesuai roadmap

# =========================
# Bagian Sederhana
# =========================
print("Belajar Dasar Python")   # Cetak teks "Belajar Dasar Python"
print()
print("+----------------+")      # Cetak garis pembatas
print("|Bagian Sederhana|")     # Cetak judul "Bagian Sederhana"
print("+----------------+")      # Cetak garis pembatas
print()

# Variables and Data Types
nama = "Andi"        # Variabel string berisi nama
umur = 20            # Variabel integer berisi angka 20
tinggi = 1.75        # Variabel float berisi 1.75
is_student = True    # Variabel boolean bernilai True

print("Nama:", nama)           # Tampilkan isi variabel nama
print("Umur:", umur)           # Tampilkan isi variabel umur
print("Tinggi:", tinggi)       # Tampilkan isi variabel tinggi
print("Mahasiswa?", is_student) # Tampilkan isi variabel boolean

# Type Casting
umur_str = str(umur)     # Konversi umur (int) → string
tinggi_int = int(tinggi) # Konversi tinggi (float) → integer
print("Umur (string):", umur_str) # Cetak hasil konversi umur
print("Tinggi (int):", tinggi_int) # Cetak hasil konversi tinggi

# Conditionals
if umur >= 18:                 # Jika umur lebih besar/sama dengan 18
    print("Sudah dewasa")      # Jika kondisi benar
else:
    print("Masih anak-anak")   # Jika kondisi salah

# Loops
print("Cetak angka 1 sampai 5:")   # Judul untuk loop
for i in range(1, 6):              # Loop dari angka 1 sampai 5
    print(i)                       # Cetak angka saat ini

# Exceptions
try:
    hasil = 10 / 0                 # Percobaan bagi 10 dengan 0 (akan error)
except ZeroDivisionError:          # Tangkap error pembagian dengan nol
    print("Terjadi pembagian dengan nol!")  # Pesan error

# Functions & Builtin Functions
def sapa(nama):                    # Definisi fungsi dengan parameter nama
    print("Halo,", nama)           # Cetak sapaan

sapa("Budi")                       # Panggil fungsi dengan argumen "Budi"
print("Panjang nama:", len(nama))  # Gunakan fungsi len() untuk hitung panjang string

# Lists
buah = ["apel", "jeruk", "mangga"] # Buat list berisi nama buah
print("List buah:", buah)          # Cetak isi list
buah.append("pisang")              # Tambahkan "pisang" ke list
print("List buah setelah ditambah:", buah) # Cetak isi list setelah ditambah

# Tuples
warna = ("merah", "biru", "hijau") # Buat tuple berisi warna
print("Tuple warna:", warna)       # Cetak isi tuple

# Sets
angka_unik = {1, 2, 3, 3, 2}       # Buat set (duplikat otomatis dihapus)
print("Set angka unik:", angka_unik) # Cetak isi set

# Dictionaries
mahasiswa = {"nama": "Siti", "umur": 19, "jurusan": "Informatika"} # Buat dictionary
print("Dictionary mahasiswa:", mahasiswa) # Cetak isi dictionary

# =========================
# Bagian Kompleks
# =========================

print("+---------------+")        # Cetak garis pembatas
print("|Bagian Kompleks|")       # Cetak judul "Bagian Kompleks"
print("+---------------+")        # Cetak garis pembatas

# Fungsi dengan parameter default dan return value
def hitung_gaji(jam_kerja, upah_per_jam=20000) -> int: # Definisi fungsi dengan default parameter
    return jam_kerja * upah_per_jam  # Kembalikan hasil perkalian

gaji = hitung_gaji(40)             # Panggil fungsi dengan jam kerja 40
print(f"Gaji mingguan: {gaji}")    # Cetak hasil gaji

# List comprehension
angka = [i for i in range(1, 11)]  # Buat list angka 1 sampai 10
kuadrat = [x**2 for x in angka]    # Buat list kuadrat dari setiap angka
print("Angka:", angka)             # Cetak list angka
print("Kuadrat:", kuadrat)         # Cetak list kuadrat

# Nested dictionary
data_mahasiswa = {                  # Buat dictionary dengan key NIM
    "001": {"nama": "Andi", "nilai": [80, 90, 85]},
    "002": {"nama": "Siti", "nilai": [88, 92, 79]},
}
for nim, info in data_mahasiswa.items():    # Loop dictionary
    rata2 = sum(info["nilai"]) / len(info["nilai"])  # Hitung rata-rata nilai
    print(f"NIM: {nim}, Nama: {info['nama']}, Rata-rata nilai: {rata2:.2f}") # Cetak hasil

# Lambda + map + filter
angka_ganjil = list(filter(lambda x: x % 2 != 0, angka)) # Filter hanya angka ganjil
print("Angka ganjil:", angka_ganjil)                    # Cetak angka ganjil
hasil_map = list(map(lambda x: x * 10, angka))          # Kalikan setiap angka dengan 10
print("Angka dikali 10:", hasil_map)                    # Cetak hasil map

# Error handling dengan multiple exception
try:
    nilai = int(input("Masukkan nilai: "))              # Input angka dari user
    print("Nilai yang dimasukkan:", nilai)              # Cetak nilai
except ValueError:                                      # Jika input bukan angka
    print("Input bukan angka!")                         
except Exception as e:                                  # Jika error lain
    print("Terjadi error lain:", e)                     # Cetak error

# Class dan OOP sederhana
class Mahasiswa:                        # Definisi class Mahasiswa
    def __init__(self, nama, nim):      # Konstruktor dengan parameter nama & nim
        self.nama = nama                # Simpan nama
        self.nim = nim                  # Simpan NIM
        self.nilai = []                 # Inisialisasi list kosong untuk nilai

    def tambah_nilai(self, nilai):      # Method untuk menambah nilai
        self.nilai.append(nilai)

    def rata_rata(self):                # Method untuk hitung rata-rata nilai
        if self.nilai:                  # Jika list nilai tidak kosong
            return sum(self.nilai) / len(self.nilai)  # Hitung rata-rata
        return 0

mhs1 = Mahasiswa("Budi", "003")         # Buat objek Mahasiswa
mhs1.tambah_nilai(80)                   # Tambahkan nilai 80
mhs1.tambah_nilai(90)                   # Tambahkan nilai 90
print(f"Mahasiswa: {mhs1.nama}, Rata-rata: {mhs1.rata_rata()}") # Cetak nama & rata-rata

# Penggunaan modul eksternal
import math                             # Import modul math
print("Akar dari 144:", math.sqrt(144)) # Hitung akar kuadrat dari 144
print("Pi:", math.pi)                   # Cetak konstanta pi

# Membaca dan menulis file
with open("contoh.txt", "w") as f:      # Buka file untuk menulis (write mode)
    f.write("Ini contoh menulis file dengan Python.\n") # Tulis teks ke file

with open("contoh.txt", "r") as f:      # Buka file untuk membaca (read mode)
    isi = f.read()                      # Baca isi file
    print("Isi file:", isi)             # Cetak isi file
