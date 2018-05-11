#1) Desenvolva uma App em Python que imprima todos os números inteiros
#de 0 a 50.

"""
n = 0
while n <= 50:
    print(n)
    n = n + 1
"""

#2) Desenvolva uma App em Python que imprima todos os números
#múltiplos de 5, no intervalo fechado de 1 a 500.

"""
n = 5
while n <= 500:
    print(n)
    n += 5
"""

#3) Desenvolva uma App em Python que imprima todos os números pares
#do intervalo fechado de 1 a 100.

"""
n = 0
while n <= 100:
    print(n)
    n += 2
"""



#4) Desenvolva uma App em Python que imprima os 100 primeiros números
#ímpares

"""
n = 0

while n <= 200:
    if n % 2 != 0:
        print(n)
    n += 1
"""



#5) Desenvolva uma App em Python que receba dez números do usuário e
#imprima o quadrado de cada número

"""
n = int(input("Type a number: "))

print(n ** 2)
cont = 1
while cont < 10:
    n = int(input("Type a number: "))
    print(n ** 2)
    cont += 1
"""



#6) Desenvolva uma App em Python que receba dez números do usuário e
#imprima o cubo de cada número.

"""
n = int(input("Type a number: "))

print(n ** 3)
cont = 1
while cont < 10:
    n = int(input("Type a number: "))
    print(n ** 3)
    cont += 1
"""



#7) Desenvolva uma App em Python que imprima todos os números de 1
#até 100, inclusive, e a soma de todos eles.

"""
n = 0

for n in range(1, 101):
    print(n)

a = (1 + 100) * 100/2
print(a)
"""



#8) Desenvolva uma App em Python que imprima todos os números de 1
#até 100, inclusive, e a soma do cubo desses números.

"""
n = 0
soma = 0
cont = 1
while n <= 100:
    print(n)
    soma += (n**3)
    n += 1
print(soma)
"""


#9) Desenvolva uma App em Python que imprima todos os números de 1
#até 100, inclusive, e a média de todos eles.

"""
n = 0

for n in range(1, 101):
    print(n)

a = (1 + 100) * 100/2
print(a/100)
"""

#10) Desenvolva uma App em Python que leia um número (NUM), e depois
#leia NUM números inteiros e imprima o maior deles.

"""
n = int(input("Type a number: "))
cont = 1
maior = cont
while cont <= n:
    print(cont)
    if cont > maior:
        maior = cont
    cont += 1
print("maior:\n", maior)
"""



#11) Desenvolva uma App em Python que leia dez números inteiros e imprima o
#maior e o segundo maior número da lista.

"""
n = int(input("Type a number: "))
cont = 1
sec_maior = n
maior = n

while cont < 10:
    n = int(input("Type a number: "))
    if n > maior:
        sec_maior = maior
        maior = n
    elif n > sec_maior:
        sec_maior = n


    cont += 1
print("Higher number: ", maior)
print("Second higher number: ",sec_maior)
"""



#12) Desenvolva uma App em Python que leia um número (NUM) e então imprima
#os múltiplos de 3 e 5, ao mesmo tempo, no intervalo fechado de 1 a NUM.
n = int(input("Type a number: "))
cont = 1
a = 0
b = 0

while cont < n:
    a = n + 3
    b = n + 5
    cont += 1
print(a, b)


