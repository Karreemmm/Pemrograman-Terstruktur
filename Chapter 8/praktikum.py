# Membuat tipe data list
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

# Menyisipkan nilai 10 ke dalam indeks ke 3 pada list  a, dan 15 ke dalam indeks ke 2 pada list b 
a.insert(3, 10)
print(a)
b.insert(2, 15)
print(b)

# Menyisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b
a.append(4)
print(a)
b.append(8)
print(b)

# Mengurutkan secara ascending pada list a dan b
a.sort()
print(a)
b.sort()
print(b)

# Membuat list c yangg elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7) 
c = a[0:8]
print(c)
# Membuat list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)
d = b[2:10]
print(d)

# Membuat list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d
e = []
for i in range (len(c)):
    jmlh = c[i] + d[i]
    e = e + [jmlh]
print(e)

#  Mengubah list e ke dalam tuple
myTuple = tuple(e)
print(myTuple)

# Mencari nilai min, maks, dan sum elemen dari e
print(min(myTuple))
print(max(myTuple))
print(sum(myTuple))

# Membuat string
myString = 'python adalah bahasa pemrograman yang menyenangkan'

# Menentukan karakter huruf dari susunan kata
print(set(myString))

# Mengubah kedalam list dan mengurutkan sesuai alfabet
myList = list(set(myString))
myList.sort()
print(myList)
