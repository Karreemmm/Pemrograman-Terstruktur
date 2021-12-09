from datetime import *
file    = open('d:/dataPeminjam.txt', 'w')

while True:
    kode  = input('\nMasukkan Kode Member : ')
    nama  = input('Masukkan Nama Member : ')
    buku  = input('Masukkan Judul Buku  : ')
    
    tglPinjam  = datetime.date(datetime.now())
    tglKembali = tglPinjam + timedelta(days = 7)
    
    lagi = input('\nUlangi lagi (y/n)    : ')
    if lagi == 'y' or lagi == 'Y':
        file.write(kode + '|' + nama + '|' + buku + '|' + str(tglPinjam) + '|' + str(tglKembali) + '\n')
    elif lagi == 'n' or lagi == 'N':
        file.write(kode + '|' + nama + '|' + buku + '|' + str(tglPinjam) + '|' + str(tglKembali) + '\n')
        file.close()
        break
