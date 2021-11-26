buah = {'apel': 5000,'jeruk' : 8500,'mangga' : 7800,'duku' : 6500}

print('====================================')
print('============ MENU BUAH =============')
print('====================================')
for buah_key in buah:
    print('- Buah', buah_key, '\n  Harga per kg : Rp', buah[buah_key])

print('\nMenu : ')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')

while True:
    pilihan = input('\nPilihan menu : ')
    if pilihan == 'A' or pilihan == 'a' :
        while True :
            tambah = str(input('\nMasukkan nama buah     : '))
            if(tambah not in buah):
                harga = int(input('Masukkan harga satuan  : '))
                buah[tambah] = harga
                lagi = str(input('Tambah lagi (y/n)? :'))
                if lagi == 'y':
                    continue
                elif lagi == 'n':
                    print('Data Buah : ')
                    for buah_key in buah:
                        print('- ', buah_key, '(Harga Rp', buah[buah_key],')')
            elif(tambah in buah):
                print('Buah tersebut sudah tersedia dalam menu')
                continue
            break

    elif(pilihan == 'B' or pilihan == 'b'):
        sum = 0
        while True:
            nama = str(input('\nNama buah yang dibeli : '))
            jumlah = int(input('Berapa Kg             : '))
            if nama in buah :
                harga = jumlah * buah[nama]
                sum = sum + harga
                lagi = input('\nBeli buah yang lain (y/n) ? ')
                if lagi == 'y' :
                    continue
                elif lagi == 'n' :
                    print('-------------------------------------')
                    print('Total harga           :', sum)
                    break
            else :
                print('Buah tidak tersedia')
    
    elif(pilihan == 'C' or pilihan == 'c'):
            while True:
                hapus = str(input('Buah yang ingin dihapus : '))
                if(hapus in buah):
                    del buah[hapus]
                    lagi = str(input('Mau menghapus buah lagi (y/n)? :'))
                    if lagi == 'y':
                        continue
                    elif lagi == 'n':
                        print('Data Buah : ')
                        for buah_key in buah:
                            print('- ', buah_key, '(Harga Rp', buah[buah_key],')')
                elif(hapus not in buah):
                    print('Buah tidak ditemukan')
                    continue
                break
    
    else:
        print('Pilihan menu tidak tersedia')
