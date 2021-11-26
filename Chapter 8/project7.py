buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def mahal():
    print(buah)
    key = list(buah.keys())
    value = tuple(buah.values())
    termahal = max(value)
    index = value.index(termahal)
    
    print('Buah Termahal :',key[index])

mahal()
