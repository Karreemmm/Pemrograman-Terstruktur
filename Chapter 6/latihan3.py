#Menghitung faktorial
def faktorial(n):
    if (n > 1):
        return n * (faktorial(n - 1))
    else:
        return 1

#Menghitung Kombinasi
def C(n, r):
    return faktorial(n) / (faktorial(r) * faktorial(n - r))



#Menghitung Permutasi
def P(n, r):
    return faktorial(n) / faktorial(n - r)

n = 5
r = 3
print('Hasil dari C(',n,',',r,') adalah',(C(5, 3)))
n = 10
r = 7
print('Hasil dari P(',n,',',r,') adalah',(P(10, 7)))
