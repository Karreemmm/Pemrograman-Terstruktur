file = open('d:/datamahasiswa.txt', 'r')
read = file.readlines()

mydict = {}
List = []
mylist = list(read)

for datamahasiswa in mylist:
    split = datamahasiswa.split('|')
    nim = split[0]
    nama = split[1]
    alamat = split[2].replace('\n', '')

    Dict = {'nim' : nim, 'nama' : nama, 'alamat' : alamat}
    List.append(Dict)

print('DataMhs : ', List)
file.close
