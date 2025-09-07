# Program pembelajaran dasar Python sesuai roadmap, dengan penjelasan tiap poin

# Basic Syntax
print("Belajar Dasar Python")  # Menampilkan teks ke layar

# Variables and Data Types
nama = "Andi"         # Variabel bertipe string
umur = 20             # Variabel bertipe integer
tinggi = 1.75         # Variabel bertipe float
is_student = True     # Variabel bertipe boolean
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa?", is_student)

# Type Casting
umur_str = str(umur)      # Mengubah integer ke string
tinggi_int = int(tinggi)  # Mengubah float ke integer
print("Umur (string):", umur_str)
print("Tinggi (int):", tinggi_int)

# Conditionals
# Percabangan untuk menentukan status berdasarkan umur
if umur >= 18:
    print("Sudah dewasa")
else:
    print("Masih anak-anak")

# Loops
# Perulangan untuk mencetak angka 1 sampai 5
print("Cetak angka 1 sampai 5:")
for i in range(1, 6):
    print(i)

# Exceptions
# Penanganan error jika terjadi pembagian dengan nol
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Terjadi pembagian dengan nol!")

# Functions & Builtin Functions
# Fungsi untuk menyapa seseorang
def sapa(nama):
    print("Halo,", nama)

sapa("Budi")  # Memanggil fungsi
print("Panjang nama:", len(nama))  # Fungsi bawaan untuk menghitung panjang string

# Lists
buah = ["apel", "jeruk", "mangga"]  # List untuk menyimpan beberapa data
print("List buah:", buah)
buah.append("pisang")               # Menambah data ke list
print("List buah setelah ditambah:", buah)

# Tuples
warna = ("merah", "biru", "hijau")  # Tuple untuk data yang tidak bisa diubah
print("Tuple warna:", warna)

# Sets
angka_unik = {1, 2, 3, 3, 2}        # Set untuk data unik (tidak ada duplikat)
print("Set angka unik:", angka_unik)

# Dictionaries
mahasiswa = {"nama": "Siti", "umur": 19, "jurusan": "Informatika"}  # Dictionary untuk pasangan kunci-nilai
print("Dictionary mahasiswa:", mahasiswa)