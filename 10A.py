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
"""
n = int(input("Type a number: "))
cont = 1
a = 0
b = 0

while cont < n:
    a = n + 3
    b = n + 5
    cont += 1
print(a, b)
"""


#13) Desenvolva uma App em Python que receba 15 números e imprima quantos
#números maiores que 30 foram digitados.

"""
n = int(input("Digite um número: "))
cont = 1
num = 0

while cont <= 15:
    n = int(input("Digite um número: "))
    if n > 30:
        num += 1
    cont += 1
print(num)
"""



#14) Desenvolva uma App em Python que leia 20 números e imprima a soma dos
#positivos e o total de números negativos.

"""
n = 0
cont = 1
neg = 0
soma = 0

while cont <= 5:
    n = int(input("Digite um número: "))
    if n < 0:
        neg += 1
    if n >= 0:
        soma += n
    cont += 1
print("Soma dos positivos:", soma,"\nTotal de números negativos:", neg)
"""



#15) Desenvolva uma App em Python que determine todos os divisores de um
#dado número N.

"""
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
"""



#16) Seja a seguinte série: 1, 4, 9, 16, 25, 36, … Desenvolva
#uma App em Python que gere esta série até o N-ésimo
#termo. Este N-ésimo termo é digitado pelo usuário.

"""
n = int(input("Digite o N-ésimo termo: "))
cont = 1
i = 0

while cont <= n:
    i = cont * cont
    print(i)
    cont += 1
"""



#17) O valor aproximado do número p pode ser calculado
#usando-se a série: S = 1 - 1/33 + 1/53 - 1/73 + 1/93 - …
#Sendo PI = (S.32)**1/3. Desenvolva uma App em Python
#que calcule e imprima o valor de p usando os 51 primeiros
#termos da séria.

"""
n = 51
S = 0
x = 1

for i in range(1, n+1):
    if i == 1:
        S += 1
    if i % 2 == 0:
        S -= (1/x**3)
    if i % 3 == 0:
        S += (1/x**3)
    x += 2
    PI = (S*32)**(1/3)
print(PI)
"""
