dataBil = []
n = int(input('Tentukan banyak nilai yang ingin di masukkan : '))
    
for i in range(n):
    bil = int(input('Masukkan bilangan : '))
    dataBil.append(bil)

dataBil.sort(reverse=True)
print(dataBil)
