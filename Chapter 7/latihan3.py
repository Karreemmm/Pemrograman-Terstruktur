print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

data = 0
jumlah = 0
while True:
    try:
        bil = int(input('Masukkan bilangan bulat : '))
        data = data + bil
        jumlah = jumlah + 1
        pilih = input('Lagi (y/n) : ')

        if pilih == 'y':
            True
        elif pilih == 'n':
            rata = int(data / jumlah)
            print('\nRata-ratanya adalah : ' + str(rata))
            break
        else:
            print('Tidak ada selain pilihan (y/n)')
            break
    
    except ValueError:
        print('Bukan bilangan bulat')
        continue
