n = 4
s = []
summa_chisel = 0
for i in range (1, n+1):
  element = (1+1/i)**i
  s.append(element)
  summa_chisel+=element
print ("сумма чисел в последовательности {} равна {}".format(s, summa_chisel))