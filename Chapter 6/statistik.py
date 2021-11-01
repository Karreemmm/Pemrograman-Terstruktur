def sum(*n):
    hasil = 0
    for i in n:
        hasil += i
    return hasil

def avg(*n):
    hasil = sum(*n)
    jumlah = 0
    for i in n:
        jumlah += 1
    return hasil / jumlah

def maks(*n):
    hasil = n[0]
    for i in n:
        if i >= hasil :
            hasil = i
    return hasil

def min(*n):
    hasil = n[0]
    for i in n:
        if i <= hasil:
            hasil = i
    return hasil
