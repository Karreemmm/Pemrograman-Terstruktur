buka = open('d:/enkripsi.txt', 'r')
read = buka.read()

teks = print('Ketikkan teks yang akan dienkripsi : ', read)
while True:
    n = int(input('Banyaknya pergeseran yang diinginkan : '))
    if n == True:
        True
    break

def enkripsi(teks, n):
    mylist = list(read)
    for charact in range(len(mylist)) :
        if mylist[charact] != (' '):
            encrypt = (ord(mylist[charact]) - n)
            if encrypt >= ord('A'):
                mylist[charact] = chr(encrypt)
            elif encrypt <= ord('A'):
                encrypt += 26
                mylist[charact] = chr(encrypt)
        else:
            continue   
    tekshasil = ''.join(mylist)
    print ("Hasil enkripsi dari teks yang diinputkan adalah : ", tekshasil)
    return tekshasil

enkripsi(teks, n)
