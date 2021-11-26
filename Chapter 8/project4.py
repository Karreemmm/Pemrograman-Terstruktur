sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print('Data Sayur :', sayur)
while True:
    print('Menu : ')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    pilihan = input('Pilihan Anda : ')
    if pilihan == 'A' or pilihan == 'a' :
        while True :
            tambah = input('Tambahkan sayur yang diinginkan: ')
            sayur.append(tambah)
            lagi = input('\nMau menambahkan sayur lagi (y/n) : ')
            if lagi == 'y' :
                True
            elif lagi == 'n' :
                break

    elif pilihan == 'B'or pilihan == 'b' :
        while True :
            try :
                hapus = input('Sayur yang ingin di hapus : ')
                sayur.remove(hapus)
                lagi = input('\nMau menghapus sayur lagi (y/n) : ')
                if lagi == 'y' :
                    True
                elif lagi == 'n' :
                    break
            except ValueError:
                print('Sayur tidak ditemukan')
                break

    elif pilihan == 'C' or pilihan == 'c' :
        print('Data Sayur :','\n',sayur)
        print('')
