def starFormation(n):
    for i in range(n):
        formasi = '*'*(i*2+1)
        print(formasi.center(2*n-1))

starFormation(4)
