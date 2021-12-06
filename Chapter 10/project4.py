file = open('d:/datamahasiswa.txt', 'r')
read = file.readlines()
cari = input('\nMasukkan NIM yang mau dicari : ')

for datamahasiswa in range(len(read)):
    if cari in read[datamahasiswa]:
        split = read[datamahasiswa].split('|')
        print('\nData Mahasiswa')
        print('NIM    : ' + split[0])
        print('Nama   : ' + split[1])
        print('Alamat : ' + split[2])
        break
if cari not in read[datamahasiswa]:
    print('Data mahasiswa tidak ditemukan')

file.close()
