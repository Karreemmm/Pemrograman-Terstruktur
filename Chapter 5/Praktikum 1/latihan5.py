# Input data karyawan
Kode = input('Masukkan kode karyawan : ')
Nama = input('Masukkan nama karyawan : ')
Gol  = input('Masukkan golongan      : ')

# Menghitung gaji
if (Gol == 'A') :
    gajiPokok = 10000000
    potongan = 2.5
    gajiPotongan = gajiPokok * potongan / 100
elif (Gol == 'B') :
    gajiPokok = 8500000
    potongan = 2.0
    gajiPotongan = gajiPokok * potongan / 100
elif (Gol == 'C') :
    gajiPokok = 7000000
    potongan = 1.5
    gajiPotongan = gajiPokok * potongan / 100
elif (Gol == 'D')  :
    gajiPokok= 5500000
    potongan = 1.0
    gajiPotongan = gajiPokok * potongan / 100

Stus = int(input("Masukkan Status (1: Menikah, 2: Belum): "))
if (Stus == 1):
    status = "Menikah"
    tunjSatu = 10 / 100 * gajiPokok
    anak = int(input("Masukkan jumlah Anak  : "))
    tunjDua = 5 / 100 * gajiPokok
    tunjDua = tunjDua * anak
     
elif (Stus == 2):
    status = "Belum Menikah"
    anak = "-"
    tunjSatu = 0
    tunjDua = 0
    
gajiKotor = gajiPokok + tunjSatu + tunjDua
gajiBersih = gajiKotor - gajiPotongan

# Menampilkan hasil
print('\n')
print('========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('----------------------------------------')
print('Nama Karyawan     :', Nama , '(Kode :', Kode ,')')
print('Golongan          :', Gol)
print('Status Menikah    :', status)
print('Jumlah Anak       :', anak)
print('----------------------------------------')
print('Gaji Pokok        : Rp', gajiPokok)
print('Tunjangan Istri/Suami : Rp', int(tunjSatu))
print('Tunjangan Anak    : RP', int(tunjDua))
print('-------------------------------------- +')
print('Gaji Kotor        : Rp', int(gajiKotor))
print('Potongan (', (potongan) ,'%) : Rp', int(gajiPotongan))
print('-------------------------------------- -')
print('Gaji Bersih       : Rp', int(gajiBersih))
