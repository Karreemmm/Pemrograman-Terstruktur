from datetime import *

def diffDate (x) :
    selisih = abs(x - y)
    hasil = selisih.days
    
    return hasil

y = datetime.date(datetime.now())
x = date(2021,12,31)
print('Selisih hari antara tanggal', y, 'dengan tanggal', x, 'adalah', diffDate(x), 'hari.')
