# Input data karyawan
Kode = input('Masukkan kode karyawan : ')
Nama = input('Masukkan nama karyawan : ')
Gol  = input('Masukkan golongan      : ')

# Menghitung gaji
if (Gol == 'A') :
    gajiKotor = 10000000
    potongan = 2.5
    gajiPotongan = gajiKotor * potongan / 100
elif (Gol == 'B') :
    gajiKotor = 8500000
    potongan = 2.0
    gajiPotongan = gajiKotor * potongan / 100
elif (Gol == 'C') :
    gajiKotor = 7000000
    potongan = 1.5
    gajiPotongan = gajiKotor * potongan / 100
elif (Gol == 'D') :
    gajiKotor = 5500000
    potongan = 1.0
    gajiPotongan = gajiKotor * potongan / 100

gajiBersih = gajiKotor - gajiPotongan

# Menampilkan hasil
print('\n')
print('========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('----------------------------------------')
print('Nama Karyawan     :', Nama , '(Kode :', Kode ,')')
print('Golongan          :', Gol)
print('----------------------------------------')
print('Gaji Pokok        : Rp', gajiKotor)
print('Potongan (', (potongan) ,'%) : Rp', int(gajiPotongan))
print('----------------------------------------')
print('Gaji Bersih       : Rp', int(gajiBersih))
