buah = {'apel': 5000,'jeruk' : 8500,'mangga' : 7800,'duku' : 6500}

print('====================================')
print('============ MENU BUAH =============')
print('====================================')
for buah_key in buah:
    print('- Buah', buah_key, '\n  Harga per kg : Rp', buah[buah_key])
print()    
while True:
    nama = str(input('Nama buah yang dibeli : '))
    jumlah = int(input('Berapa Kg             : '))
    if nama in buah:
        harga = jumlah * buah[nama]
        print('-------------------------------------')
        print('Total harga           :', harga)
        break
    else:
        print('Buah tidak tersedia')
