"""
1) Uma P. G. (progressão geométrica) é determinada pela sua razão (q) e pelo primeiro termo (a1). Desenvolva
uma App em Python que seja capaz de determinar qualquer termo de uma P. G., dado a razão e o primeiro termo
(lidos do teclado).
"""
"""
q = int(input("insira a razao: "))
a = int(input("insira o primeiro termo: "))
n = int(input("insira o termo: "))


x = a * q ** (n - 1)
print(x)
"""


"""
2) Considere que o número de uma placa de veículo é composto por quatro algarismos. Desenvolva uma App em
Python que leia este número e apresente o algarismo correspondente à casa das unidades. 
"""
"""
placa = int(input("digite a placa: "))
n = placa % 10
print(n)
"""


"""
3) Considere que o número de uma placa de veículo é composto por quatro algarismos. Desenvolva uma App em
Python que leia este número e apresente o algarismo correspondente à casa das centenas. 
"""
"""
placa = int(input("insira a placa: "))
a = placa // 100
n = a % 10

print(n)
"""


"""
4) Considere que o número de uma placa de veículo é composto por quatro algarismos. Desenvolva uma App em
Python que leia este número e apresente o algarismo correspondente à casa das milhares. 
"""
"""
placa = int(input("Insira a placa: "))
n = placa // 1000
print(n)
"""


"""
5) Desenvolva uma App em Python que leia dois números reais e imprima a média aritmética entre esses dois
valores com a seguinte mensagem “MEDIA” antes do resultado. 
"""
"""
a = float(input("Insira um numero: "))
b = float(input("Insira o segundo numero: "))
n = (a + b) / 2
print("MEDIA: ", n)
"""


"""
6) Desenvolva uma App em Python para realizar a soma de uma P.A. de N termos, com o primeiro a1 e o último an.
"""
"""
a = int(input("Insira o primeiro termo: "))
an = int(input("Insira o ultimo termo: "))
n = int(input("Insira o numero de termos:"))

s = ((a + an)*n)/2
print(s)
"""


"""
7) Seja uma sequência A,B,C, ... determinando um Progressão Geométrica (P.G.), o termo médio (B) de uma P.G.
é determinado pela média geométrica de seus termos, sucessor (C) e antecessor (B). Com base neste enunciado
desenvolva uma App em Python que calcule o termo médio (B) através de A, C. 
"""
"""
import math

a = int(input("digite o primeiro termo: "))
c = int(input("digite o ultimo termo: "))
d = math.sqrt(a + c)
print(d)
"""


"""
8) Agora, Desenvolva uma App em Python para determinar o produto dos n primeiros termos de uma P.G. 
"""
"""
a = int(input("Insira o primeiro termo: "))
q = int(input("Insira a razao: "))
n = int(input("Insira o numero de termos: "))

p = (a**n)*(q**(n*(n - 1)/2))
print(p)
"""


"""
9) Desenvolva uma App em Python que leia um número e imprima se ele é igual a 5, a 200, a 400, se está no intervalo entre 500 e
1000, inclusive, ou se ela está fora dos escopos anteriores. 
"""
"""
n = int(input("Insira um numero: "))

if n == 5:
    print("Esse numero e igual a 5")
elif n == 200:
    print("Esse numero e igual a 200")
elif n == 400:
    print("Esse numero e igual a 400")
elif 500 <= n <= 1000:
    print("Esse numero esta entre 500 e 1000")
else:
    print("Esse numero esta fora dos escopos anteriores")
"""


"""
10) Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo
desconto. Desenvolva uma App em Python que possa entrar com o valor de um produto e imprima o novo valor
tendo em vista que o desconto foi de 9%. Além disso, imprima o valor do desconto. 
"""
"""
valor = float(input("Insira o valor do produto:"))
d = valor * 0.09
n = valor * 0.91
print("Valor com desconto:", n)
print("Valor do desconto", d)
"""


"""
11) Desenvolva uma App em Python para calcular e apresentar o valor do volume de uma lata de óleo, utilizando a
fórmula:
"""
"""
r = float(input("Insira o raio: "))
h = float(input("Insira a altura: "))
v = 3.14159 * ((r ** 2) * h)
print(v)
"""


"""
12) Desenvolva uma App em Python que leia uma temperatura em graus centígrados e apresente a temperatura
convertida em graus Fahrenheit
"""
"""
c = int(input("Insira a temperatura em graus centigrados: "))
f = ((9 * c)+160)/5
print(f)
"""


"""
13) Criar um Algoritmo que leia um valor de hora (hora:minutos) e informe (calcule) o total de minutos se passaram
desde o início do dia (0:00h).
"""
"""
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
h = hora * 60

total = h + minuto
print(total)
"""


"""
14) Desenvolva uma App em Python que leia dois valores para as variáveis A e B, que efetue a troca dos valores
de forma que a variável A passe a ter o valor da variável B e que a variável B passe a ter o valor da variável A.
Apresente os valores trocados. 
"""
"""
a = int(input("A: "))
b = int(input("B: "))
c = a
d = b
a = d
b = c

print("A: ", a)
print("B: ", b)
"""
