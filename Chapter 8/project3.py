dataMhs = []
n = int(input('Tentukan banyak nama mahasiswa yang ingin di masukkan : '))
    	
for i in range(n):
    Mhs = input('Masukkan nama : ')
    dataMhs.append(Mhs)

for Mhs in dataMhs:
    jmlh = len(Mhs)
    print(Mhs , '(', jmlh, 'karakter )')
