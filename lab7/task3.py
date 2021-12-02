#Вариант 3
def nod(a, b):
  if a == 0:
     return b
  if b == 0:
     return a
  return nod(a % b, b) if a >= b else nod(a, b % a)

a, b = (int(i) for i in input().split())
print(f'НОД ( { a } , { b } ) = { nod(a, b) } ')