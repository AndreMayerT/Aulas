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
