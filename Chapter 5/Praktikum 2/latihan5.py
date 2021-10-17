from random import randint
bil = randint(0, 100)

print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
while True:
    tebak = int(input('Tebakan Anda : '))
    if(tebak > bil):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
    elif(tebak < bil):
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
    elif(tebak == bil):
        print('Yeeee,... Bilangan tebakan anda BENAR :-)')
        break
