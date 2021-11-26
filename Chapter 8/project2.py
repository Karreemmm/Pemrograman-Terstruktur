def datastat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    listdata = [a, b, c]
    return listdata

data = []
try :
    bnyk = int(input('Masukkan banyak bilangan yang ingin diinputkan: '))
except ValueError:
    print('Data yang diinputkan harus bilangan bulat')

for i in range(bnyk):
    angka = int(input('Masukkan angka: '))
    data.append(angka)
    
print('Rata-rata, Max, Min:','\n', datastat(data))
