n = 3
s = []
summa_chisel = 0

for i in range (-n, n+1):
  s.append(i)

indexes = input('введите разделители через пробел ').split()

proizvedenie_elem = 1
counter = 0

for i in s:
  for j in indexes:
    if (counter == int(j)):
      proizvedenie_elem*= int (i)
  counter += 1

print (s)
print (indexes)
print(proizvedenie_elem)