teks = input('Input teks yang akan dienkripsi : ')
while True:
    n = int(input('Banyaknya pergeseran yang diinginkan : '))
    if n == True:
        True
    break

def enkripsi(teks, n):
    mylist = list(teks)
    for charact in range(len(mylist)) :
        if mylist[charact] != (' '):
            encrypt = (ord(mylist[charact]) + n)
            if encrypt > ord('Z'):
                encrypt -= 26
                mylist[charact] = chr(encrypt)
            elif encrypt < ord('Z'):
                mylist[charact] = chr(encrypt)
        else:
            continue
    tekshasil = ''.join(mylist)
    print ("Hasil enkripsi dari teks yang diinputkan adalah : ", tekshasil)

    buka = open('d:/enkripsi.txt', 'w')
    buka.write(tekshasil)
    buka.close()
    return tekshasil
    
enkripsi(teks, n)
