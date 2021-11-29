import random
def shuffleString(x,n):
     list = []
     i = 0
     while i < n:
         list += [''.join(random.sample(x,len(x)))]
         i += 1
     print(list)
     
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
