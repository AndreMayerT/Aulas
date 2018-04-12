"""
#exercicio1

ve = [0, 0, 1, 1, 4, 5]
ca = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB"]

for i in ca:
    print(i)
for i in ve:
    print (i)
i = 0
while i < len(ve):
    print(ca[ve[i]])
    i += 2
print(ca[ve[ve[2]]])
"""

"""
#exercicio2

crr = ['!', 'U', 'O', 'T', 'R', 'E', 'C', 'A']
i = 1

while i <= 3:
    aux = crr[i]
    crr[i] = crr[7-i]
    crr[7-i] = aux
    i += 1
aux = crr[0]
crr[0] = crr[7]
crr[7] = aux
i = 0
while i < len(crr):
    print(crr[i])
    i += 1
"""

"""
#exercise3

for x in range(0, 100, 1):
    print(x)
    if x == 50:
        break
"""

"""
#exercise4

soma = 0

for i in range(0, 20 , 1):
    soma += i
media = soma / 20
print(media)
"""

"""
#exercise5

for i in range(100, 0, -1):
    print(i)
"""

"""
#exercise6

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
soma = [0] * 10

for i in range(10):
    soma[i] = A[i] + B[i]

for item in soma:
    print(item, end=' ')
"""