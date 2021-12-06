dataFile = open('d:\datamahasiswa.txt', 'a')

while True:
    nim = input('\nMasukkan NIM       : ')
    nama = input('Masukkan Nama Mhs  : ')
    alamat = input('Masukkan Alamat    : ')
    myString = nim +'|'+ nama +'|'+ alamat + '\n'
    dataFile.write(myString)
    pilih = input('\nUlangi input lagi (y/n):')
    
    if pilih == 'y' :
        True
    elif pilih == 'n':
        break
dataFile.close()
