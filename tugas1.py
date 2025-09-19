# Data diri disimpan ke dalam variabel
nama = "MOH.RODIDUL MA'ASYI"
umur = 19
tinggi = 175.5  # dalam cm
angka_favorit = 28

# Tampilkan data diri
print("=== Data Diri ===")
print("Nama:", nama)
print("Umur:", umur, "tahun")
print("Tinggi:", tinggi, "cm")
print("Angka favorit:", angka_favorit)

# Hitung total harga belanja
pensil = 4 * 2000
buku = 2 * 5000
total = pensil + buku

print("\n=== Total Belanja ===")
print("Total belanja di toko alat tulis: Rp", total)

# Mengecek angka favorit (genap atau ganjil) menggunakanan modulus dan samadengan if-else
print("\n=== Angka Favorit ===")

if angka_favorit % 2 == 0:
    print(angka_favorit, "adalah angka genap.")
else:
    print(angka_favorit, "adalah angka ganjil.")