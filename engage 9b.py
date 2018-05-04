#1) Desenvolva uma App em Python que leia dois valores numéricos inteiros e efetue a
#adição; caso o resultado seja maior que 10, apresentá-lo.
"""
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

n = a + b

if n > 10:
    print(n)
else:
    print("Resultado menor ou igual que 10")
"""



#2) Desenvolva uma App em Python que determine (imprima) se um dado número N
#inteiro (recebido através do teclado) é POSITIVO ou NEGATIVO
"""

n = int(input("Digite um número: "))
if n >= 0:
    print("POSITIVO")
else:
    print("NEGATIVO")
"""



#3) Desenvolva uma App em Python que leia um número e imprima a raiz quadrada do
#número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja
#negativo.
"""
import math

n = int(input("Digite um número: "))

if n >= 0:
    a = math.sqrt(n)
    print(a)
else:
    b =(n**2)
    print(b)
"""



#4) Desenvolva uma App em Python para determinar se um número A é divisível por
#outro número B. Esses valores devem ser fornecidos pelo usuário.
"""
a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
n = a%b
if n == 0:
    print("O número é divisível")
else:
    print("O número não é divisível")
"""



#5) Desenvolva uma App em Python que imprima a soma do menor com o maior valor de
#um conjunto de N números lidos do teclado. N deve ser fornecido antes da entrada do
#conjunto.
"""
n = int(input("insert the number of values: "))
valor= int(input("Insert a value: "))
maior = valor
menor = valor
cont = 1

while n > cont:
    valor = int(input("Insert a value:"))
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    cont += 1
print (maior + menor)
"""



#6) Desenvolva uma App em Python que leia um número e informe se ele é divisível por 3 e por 7.
"""
n = int(input("Digite um número: "))
a = n % 7
b = n % 3

if b == 0:
    if a == 0:
        print("é divisivel por 3 e por 7")
    else:
        print("não é divisivel por 3 e por 7")
else:
    print("não é divisivel")
"""



#7) Desenvolva uma App em Python que indique se um número digitado está compreendido entre
#20 e 90 ou não (20 e 90 não estão na faixa de valores).
"""
n = int(input("DIgite um número: "))

if 20 < n < 90:
    print("O número está entre 20 e 90")
else:
    print("O número não está entre 20 e 90")
"""



#8) Dado três valores, A, B e C, Desenvolva uma App em Python para verificar se estes valores
#podem ser valores dos lados de um triângulo.
"""
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b:
    print("Esse valores podem ser lados de um triângulo")
else:
    print("Não podem ser um triângulo")
"""



#9) Desenvolva uma App em Python que leia um número e informe se ele é divisível por 10, por 5
#ou por 2 ou se não é divisível por nenhum deles.
"""
n = int(input("Digite um número: "))
a = n % 2
b = n % 5
c = n % 10

if a == 0 & b == 0 & c == 0:
    print("O número é divisível por 2, 5, 10")
else:
    print("Não é divisível por 2, 5, 10")
"""



#10) Desenvolva uma App em Python que leia um número e imprima se ele é igual a 5, a 200, a
#400, se está no intervalo entre 500 e 1000, inclusive, ou se ela está fora dos escopos anteriores.
"""
n =int(input("Digite um número: "))
if n == 5:
    print("O numero é igual a 5")
elif n == 200:
    print("O número é igual a 200")
elif n == 400:
    print("O número é igual a 400")
elif 500<n<1000:
    print("O número está no intervalo entre 500 e 1000")
else:
    print("O número não está nos escopos anteriores")
"""



#11) Desenvolva uma App em Python que leia dois números e imprimir o quadrado do menor
#número e raiz quadrada do maior número, se for possível.
"""
import math

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

if a > b:
    print(b**2, math.sqrt(a))
if b > a:
    print(a**2, math.sqrt(b))
"""



#12) Desenvolva uma App em Python que receba três valores, A, B e C, e armazene-os em três
#variáveis com os seguintes nomes: MAIOR, INTER e MENOR (os nomes correspondem aos
#valores ordenados).

"""
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
maior = max(a, b, c)
menor = min(a, b, c)
inter = 0

if a != maior and a != menor:
    inter = a
    print("MAIOR:",maior, "INTER:",a, "MENOR:",menor)
elif b != maior and b != menor:
    inter = b
    print("MAIOR:",maior, "INTER:",b, "MENOR:",menor)
elif c != maior and c != menor:
    inter = c
    print("MAIOR:",maior, "INTER:",c, "MENOR:",menor)
"""
