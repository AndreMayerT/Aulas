"""
from PIL import Image

print("dados para cadastro: ")
nome = input("qual seu nome?")
idade = input("qual sua idade?")
pet = input("qual o nome do seu pet?")
banda = input("qual sua banda preferida?")

print("Olá, " + nome)
print("Você tem " + idade)
print("O nome do seu pet é " + pet)
print("O nome da sua banda preferida é " + banda)

try:
    im = Image.open("foto.jpg")
    im.show()
except:
    print("Não foi possivel carregar a imagem")
"""


"""
x, y, z= 1, 2, 0x45
print("x =", x, "\ny =", y, "\nz =", z)
print("Bem vindo\nao\ncurso de Python\n")
print("Cadeia de Caracteres\n\n")
print("Pulou!")
"""

x, y, z = 4, 2, 9
resto = x % y
divi_int = int(z // x)
divi_real = z /x
print("x =", x, "\ny =", y, "\nz =", z, "\nDivi Inteira z / x = ", divi_int, "\nDivi Real z / x", divi_real)





