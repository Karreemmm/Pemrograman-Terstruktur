buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rata2():
    for buah_key in buah:
        print('Harga buah', buah_key, 'Rp', buah[buah_key])
    key = list(buah.keys())
    value = tuple(buah.values())
    average = int(sum(value) / len(value))
    print('\nHarga rata-rata :', 'Rp', average)

rata2()
