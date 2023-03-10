import math

a = float(input('Entrez le premier terme: '))
b = float(input('Entrez le deuxieme terme: '))
op = input("Entrez l'opération: ")

if op == '*':
    print(a * b)

elif op == '+':
    print(a + b)

elif op == '-':
    print(a - b)


elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print('No division by 0')

elif op == '^':
    print(a ** b)

elif op == '&':
    print(math.sqrt(a))

else:
    print('Error')
    

