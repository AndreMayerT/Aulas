"""
#if;elif;else

resp1 = "opção escolhida foi a 1"
resp2 = "opção escolhida foi a 2"
resp3 = "opção escolhida foi a 3"
resp4 = "opção escolhida foi a default"

ch = input("Entre com um número <1, 2 ou 3>:")

if ch == '1':
    print(resp1)
elif ch == '2':
    print(resp2)
elif ch == '3':
    print(resp3)
else: print(resp4)
"""

"""
#range

for x in range(0, 10):
    print("Estamos no passo %d" % (x))
"""

"""

l = ['hello', 'world', 'hi', 'earth']
i = 0

while i < len(l):
    print(l[i])
    i = i + 1

string = "Hello world"
for x in string:
    print(x)
    
"""

"""
#break

for x in range(10):
    print(x)
    if x == 5:
        break

"""

"""
#loop aninhados

for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))

"""

"""
for letter in 'Python':
    print('Current letter:', letter)

fruits = ["Apple, Banana, Strawberry"]
for fruit in fruits:
    print("Current fruit:", fruit)

colors = ["Blue, Yellow, Red"]
for index in range(len(colors)):
    print("Current color:", colors[index])
"""

R = ["A", "B", "C", "D", "E", "F"]
S = ["A", "B", "G", "E", "P", "K"]
Z = [0, 1, 2]

k = 0
for i in range(0, 6, 1):
    comum = 0
    for j in range(0, 6, 1):
        if R[i] == S[j]:
            comum = 1
    if comum == 0:
        Z[k] = R[i]
        k = k + 1
print(Z)




