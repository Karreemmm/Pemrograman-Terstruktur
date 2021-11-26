def kuadrat(bil):
    for i in range (len(bil)):
        bil[i]**=2
    return bil

bil=[]
n = int(input('Jumlah bilangan angka yang ingin dimasukkan = '))
for i in range (n):
    angka = int(input('Masukkan angka = '))
    bil.append(angka)

print('\nbil =', bil)
print('hasil =', kuadrat(bil))
