from datetime import *

def diffDate(x):
    split  = x.split('-')
    tahun  = int(split[0])
    bulan  = int(split[1])
    hari   = int(split[2])
    tgl = date(tahun, bulan, hari)
    today  = datetime.date(datetime.now())
    selisih = tgl - today
    hasil = selisih.days

    return(hasil)

file = open('d:/dataPeminjam.txt', 'r')
read = file.readlines()

kode = input('Masukkan Kode Member : ')

for listdata in range(len(read)):
    if kode in read[listdata]:
        y = read[listdata].split('|')
        kembali = datetime.date(datetime.now())
        terlambat = diffDate(y[4])
        denda = int(terlambat) * 2000
        print('Data Peminjaman Buku')
        print('Kode Member                 : ', y[0])
        print('Nama Member                 : ', y[1])
        print('Judul Buku                  : ', y[2])
        print('Tanggal Mulai Peminjaman    : ', y[3])
        print('Tanggal Maksimal Peminjaman : ', y[4],end = (''))
        print('Tanggal Pengembalian        : ', kembali)
        print('Terlambat                   : ', terlambat)
        print('Denda                       : ', 'Rp ', denda)

        break

if kode not in read[listdata]:
    print('Data tidak ditemukan')

file.close()
