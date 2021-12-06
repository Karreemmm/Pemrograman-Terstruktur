myFile = open('d:/file.txt', 'r')
myList = myFile.readlines()
	
genap =[]
ganjil =[]
for i in range (len(myList)) :
    data = myList[i].replace('\n', '')
    if (int(data)%2 == 0) :
        genap += [data]
    elif (int(data)%2 != 0):
        ganjil +=[data]
myFile.close()

print('Banyaknya bilangan genap : ', len(genap))
print('Banyaknya bilangan ganjil : ', len(ganjil))
