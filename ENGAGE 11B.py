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

