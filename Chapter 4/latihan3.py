jarakKota = 795
konsumsiBensin = 1/12
kapasitasTangki = 50

# Hitung penggunaan bensin
totalBensin = jarakKota * konsumsiBensin

# Hitung banyak isi bensin
isiBensin = int(totalBensin // kapasitasTangki)

# Menampilkan Hasil
print("Bensin yang diperlukan untuk perjalanan dari kota A menuju kota C adalah", totalBensin, "Liter")
print("Maka Pak Budi akan mengisi bensin minimal sebanyka", isiBensin, "kali")
