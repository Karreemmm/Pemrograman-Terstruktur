def starFormation1(n):
    kolom = 0
    i = 0
    while(i <= n):
        j = 0
        while(j < kolom):
            print('* ', end='')
            j += 1
        kolom += 1
        print('')
        i += 1
starFormation1(4)
print('\n')
def starFormation2(n):
    kolom = 4
    i = 0
    while(i < n):
        j = 0
        while(j < kolom):
            print('* ', end='')
            j += 1
        kolom -= 1
        print('')
        i += 1
starFormation2(4) 
print('\n')
def starFormation3(n):
    starFormation1(3)
    starFormation2(4)
starFormation3(7)
