#MATRIX ON PYTHON



#EXEMPLE

#read matrix from user
def ler_matriz_key(linhas,colunas):

   matriz = []
   for i in range(linhas):
       linha = []
       for j in range(colunas):
          print("Valor[", i, "][", j, "]: ")
          linha.append(int(input()))
       matriz.append(linha)
   return matriz
#end



#create matrix
def cria_matriz(linhas,colunas,valor):
    matriz = []
    for i in range(linhas):
        matriz.append([valor] * colunas)
    return matriz
#end


#prints the matrix
def imprima_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end="")
        print('\n')
#end



#define the length of the matrices
A = ler_matriz_key(2,2)
B = ler_matriz_key(2,2)
C = cria_matriz(2,2,0)





#pluses the matrices
for i in range(len(A)):
    for j in range(len(B)):
        C[i][j] = A[i][j] + B[i][j]





#print
imprima_matriz(A)
imprima_matriz(B)
imprima_matriz(C)