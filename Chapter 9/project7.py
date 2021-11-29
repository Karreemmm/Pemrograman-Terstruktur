mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*72)
print('NIM'.ljust(11),'NAMA MAHASISWA'.ljust(23),'TGL LAHIR'.ljust(17),'TEMPAT LAHIR')
print('-'*72)
for i in mhs:
    data = i.split(':')
    nim = data[0]
    nama = data[1]
    tglLahir = data[2]
    tglLahirSplit = tglLahir.split('-')
    tgl = tglLahirSplit[2]
    bln = tglLahirSplit[1]
    thn = tglLahirSplit[0]
    tmptLahir = data[3]
    print(nim.ljust(12) + nama.ljust(24) + tgl + '/' + bln +'/'+ thn.ljust(12) + tmptLahir)
print('='*72)
