# Program pembelajaran dasar Python sesuai roadmap

# Basic Syntax
print("Belajar Dasar Python")

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