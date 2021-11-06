try:
    namafile = str(input('Masukkan nama file : '))
    file = open(namafile,'r')
    
    while True: 
        file = open(namafile,'a')
        data = str(input('Data yang mau ditambahkan: '))
        file.write(data)
        file.close()
        pilih = input('Mau lagi (y/n)?: ')
        if pilih == 'y':
            True
        elif pilih == 'n':
            file = open(namafile,'r')
            print('Isi File ',namafile)
            print(file.read())
            break
        else :
            file = open(namafile,'w')
            
except FileNotFoundError:
    print('File tidak ditemukan')
