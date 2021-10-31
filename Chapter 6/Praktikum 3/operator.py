from operation import *

a = 10
b = 7
print(a, '+', b, '=', jumlah(a, b))
print(a, '-', b, '=', kurang(a, b))
print(a, 'x', b, '=', kali(a, b))
print(a, '/', b, '=', bagi(a, b))
print('\n')
from operation import *

print('a. 2 + 6 x 6 - 4 =', kurang(jumlah(2, kali(6, 6)), 4))
print('b. (4 + 7) x (6 - 9) =', kali(jumlah(4, 7), kurang(6, 9)))
print('c. (10 + 2) / (7 + 5) / (12 - 34) =',bagi(bagi(jumlah(10, 2), jumlah(7, 5)), kurang(12, 34)))
