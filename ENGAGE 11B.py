#1
""""
matriz = [[1.5, 2.5,  3.5,  4.5,  5.5],[5.5,  4.5,  3.5,  2.5, 1.5]]
def imprima_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end="")
        print('\n')
imprima_matriz(matriz)
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        soma += matriz[i][j]
print(soma)
"""



#2
"""
def ler_matriz_key(linhas,colunas):
   matriz = []
   for i in range(linhas):
       linha = []
       for j in range(colunas):
          print("Valor[", i, "][", j, "]: ")
          linha.append(int(input()))
       matriz.append(linha)
   return matriz
a = ler_matriz_key(5,5)
def imprima_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end="")
        print('\n')
imprima_matriz(a)
"""



#3
"""
m1 = [['O', 'Q', '*', 'I'], ['E', 'R', 'E', 'S'], ['R', 'E', 'U', 'T'], ['A', '*', 'A', 'S']]
aux = 0
for i in range(0,3,1):
    for j in range(i+1, 3, 1):
        aux = m1[i][j]
        m1[i][j] = m1[j][i]
        m1[j][i] = aux
aux = m1[0][0]
m1[0][0] = m1[3][3]
m1[3][3] = aux
aux = m1[1][1]
m1[1][1] = m1[2][2]
m1[2][2] = aux
print(m1)
"""



#4
"""
def ler_matriz_key(linhas,colunas):

   matriz = []
   for i in range(linhas):
       linha = []
       for j in range(colunas):
          print("Valor[", i, "][", j, "]: ")
          linha.append(int(input()))
       matriz.append(linha)
   return matriz

def imprima_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end="")
        print('\n')

matriz = ler_matriz_key(10,10)


for i in range(len(matriz)):
    for j in range((len(matriz[0]) -1), -1, -1):
        if i == ((len(matriz[0]) -1) -j):
            print(matriz[i][j])

"""



#5
"""
def ler_matriz_key(linhas,colunas):

   matriz = []
   for i in range(linhas):
       linha = []
       for j in range(colunas):
          print("Valor[", i, "][", j, "]: ")
          linha.append(float(input()))
       matriz.append(linha)
   return matriz



def imprima_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end="")
        print('\n')


matriz = ler_matriz_key(5,5)
imprima_matriz(matriz)
soma = 0

for i in range(len(matriz)):
    for j in range((len(matriz[0]) -5), +5, +1):
        if i == ((len(matriz[0]) -5) +j):
            soma += matriz[i][j]

print(soma)
"""



#6
"""
def ler_matriz_key(linhas,colunas):

   matriz = []
   for i in range(linhas):
       linha = []
       for j in range(colunas):
          print("Valor[", i, "][", j, "]: ")
          linha.append(int(input()))
       matriz.append(linha)
   return matriz


def imprima_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end="")
        print('\n')

m = ler_matriz_key(5,7)
imprima_matriz(m)

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

imprima_matriz(rez)
"""



#7
"""
matriz = [[3,  4,  6,  7,  8,  2 , 1 ], [6,  6,  4,  2,  4,  3,  6], [5,  6,  9,  3,  3,  4,  6], [1,  2,  3,  4,  5,  6,  7], [9,  8,  7,  6, 5,  4,  3]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], ' ', end="")
    print('\n')
vetor = []
a = 0
for i in range(5):
    soma = sum(matriz[a])
    vetor.append(soma)
    a += 1
print('Soma de cada linha, respectivamente:', vetor)
somafinal = sum(vetor)
print('Total:', somafinal)
"""
