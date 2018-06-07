#EXEMPLE 1
"""
pedro = ["Pedro da Silva", "12/04/1957", "12345"]
maria = ["Maria da Silva", "07/12/1973", "54321"]
pessoa = [pedro,maria]
for registro in pessoa:
    print(registro)

"""


#EXEMPLE 2

"""
def mostra_pessoa(dados):
    print("Nome: ", dados[0])
    print("Nascimento: ", dados[1])
    print ("ID: ", dados[2])
    print("Salario: ", dados[3])

pedro = ["Pedro da Silva", "24/09/1991", "12345", "2000"]
maria = ["Maria da Silva", "04/03/1992", "54321", "1500"]

pessoa = [pedro,maria]

for registro in pessoa:
    mostra_pessoa(registro)
    
"""


#EXEMPLE 3

"""
from typing import NamedTuple

class person(NamedTuple):
    nome: str
    nascimento: str
    id: int
    salario: float

def input_data():
    nome_in = str(input("Entre com o Nome: "))
    nasc_in = str(input("Entre com a Data: "))
    id_in = int(input("Entre com a ID: "))
    sal_in = float(input("Entre com o salario: "))
    record = person(nome = nome_in, nascimento=nasc_in,id=id_in, salario=sal_in)
    return record

person_list = []
sair = 's'

while ((sair != 'n') and (sair != 'N')):
    person_list.append(input_data())
    sair = str(input("Continua (s ou n)?"))
for i in (range(len(person_list))):
    record = person_list[i]
    if record.id == 2:
        print("Id: ", record.id)
        print("Nome: ", record.nome)
        print("Nascimento: ", record.nascimento)
        print("Sálario: ", record.salario)
        
"""


#EXEMPLE 4

"""
from typing import NamedTuple

class data(NamedTuple):
    dia : int
    mes : int
    ano : int
#end-class

class person(NamedTuple):
    nome : str
    nascimento : data
    id : int
    salario : float
#end-class

def input_data():
    nome_in = str(input("Entre com o Nome: "))
    nasc_dia_in = int(input("Entre com o dia: "))
    nasc_mes_in = int(input("Entre com o mês: "))
    nasc_ano_in = int(input("Entre com o ano: "))
    id_in = int(input("Entre com a ID: "))
    sal_in = float(input("Entre com a Salario: "))
    record = person(nome=nome_in, nascimento=data(dia=nasc_dia_in,
mes=nasc_mes_in, ano=nasc_ano_in),id=id_in,salario=sal_in)
    return record
#end input-data

person_list = []
sair = 's'

while ((sair != 'n') and (sair != 'N' )):
    person_list.append(input_data())
    sair = str(input("Continua (s ou n)?"))
for i in (range(len(person_list))):
    record = person_list[i]
    if record.id == 2:
        print("Id: ", record.id)
        print("Nome: ", record.nome)
        print("Nascimento: ", record.nascimento.dia, "/",record.nascimento.mes,"/",
record.nascimento.ano)
        print("Sálario: ", record.salario)
        
"""

from typing import NamedTuple

class notas(NamedTuple):
    nota_1: float
    nota_2: float
    nota_3: float

class estudante(NamedTuple):
    codigo: int
    nome: str
    avaliacao: notas
    media: float


def input_data():
    codigo_in = int(input("Entre ccom o codigo: "))
    nome_in = str(input("Entre com o Nome: "))
    notas_nota1_in = float(input("Entre com a primeira nota: "))
    notas_nota2_in = float(input("Entre com a segunda nota: "))
    notas_nota3_in = float(input("Emtre com a terceira nota: "))
    record = estudante(codigo=codigo_in, nome=nome_in, avaliacao=notas(notas1=notas_nota1_in, notas2=notas_nota2_in, notas3=notas_nota3_in))
    return record

def media(record):
    media = (record.notas.nota_1 + record.notas.nota_2 + record.notas.nota_3 / 3)
    record2 = registro


