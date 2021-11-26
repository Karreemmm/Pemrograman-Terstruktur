buah = {'apel': 5000,'jeruk' : 8500,'mangga' : 7800,'duku' : 6500}

print('====================================')
print('============ MENU BUAH =============')
print('====================================')
for buah_key in buah:
    print('- Buah', buah_key, '\n  Harga per kg : Rp', buah[buah_key])
  
sum = 0
while True:
    nama = str(input('\nNama buah yang dibeli : '))
    jumlah = int(input('Berapa Kg             : '))
    if nama in buah :
        harga = jumlah * buah[nama]
        sum = sum + harga
        lagi = input('\nBeli buah yang lain (y/n) ? ')
        if lagi == 'y' :
            nama in buah
        elif lagi == 'n' :
            print('-------------------------------------')
            print('Total harga           :', sum)
            break
    else :
        print('Buah tidak tersedia')
