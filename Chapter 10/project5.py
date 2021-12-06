file = open('d:\dataBil.txt', 'r')
read = file.readlines()

for mydata in read:
    split = mydata.split('|')
    bil1 = int(split[0])
    bil2 = int(split[1])
    penjumlahan = bil1 + bil2
    print(penjumlahan)

file.close()
