n = input()
summa_cifr = 0
n = (n.replace(',', '')).replace('.', '')
for i in n:
  summa_cifr+=int(i)
print (summa_cifr)