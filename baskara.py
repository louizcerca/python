#python 2.7.12
import math

print("Hello, world!")

a = float(input('A:  '))
print(a)
b = float(input('B:  '))
print(b)
c = float(input('C:  '))
print(c)

delta = (b * b) + ((-4 * a) * c)
print ('delta =', delta)

if delta < 0:
    print ('essa equacao nao possui raizes reais')

if delta == 0:
    print ('raiz da equacao:', (-b/(2*a)))

raiz = math.sqrt(delta)
if delta > 0:
    r1 = (-b+raiz)/(2*a)
    r2 = (-b-raiz)/(2*a)
    print ('raizes da equacao:', r1, 'e', r2)
