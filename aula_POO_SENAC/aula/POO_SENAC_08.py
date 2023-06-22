#Aula 06

"""
Crie uma classe chamada Pessoa com os seguintes atributos:
    -nome
    -telefone

    Os atributos são privados e do tipo string.

Utilizando o menu a baixo crie uma agenda e armazene
    os objetos de Pessoa em uma lista chamada agenda.
    agenda = []

MENU
================
1- Adicionar / Excluir
2- Visualizar agenda
 Escolha:


Descrição:
Na opção 1: Ler nome
                Caso nome não exista na agenda, ler telefone, Instanciar e
                adicionar em agenda.
            Caso o nome já exista, mostre os dados. Perguntar se quer
                adicionar outro telefone, ou se quer
                excluir o nome localizado, ou excluir um número.

Na opção 2: mostrar na tela o nome e os telefones das pessoas.
"""

"""
class Pessoa:
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

#get_ serve para retornar um atributo privado da classe.

    def set_nome(self,nome):
        self.__nome = nome

    def set_telefone(self,telefone):
        self.__telefone = telefone

#set_ serve para modificar um atributo privado da classe.

 agenda = []

def adicionar_excluir():
    nome = input("Digite o nome da pessoa:")
    pessoa_encontrada = None
    for pessoa in agenda:
        if pessoa.get_nome() == nome:
            pessoa_encontrada = pessoa
            break
# criei uma função; primeiro passo foi por um input para pode iniciar o processo solicitado na questão;
# depois criei uma outra váriavel recebendo um valor none, isso foi feito pois essa variável foi utilizada para poder
# posteriormente ver na lista se já tem uma pessoa com esse nome na lista; a variavel "pessoa" foi colocada antes do
# ".get_nome()" para pode ver se ele recebeu um valor igual ao dado a variavel "nome", caso isso aconteça a variavel
# "pessoa_encontrada" recebe o valor/nome que foi dado a variavel "pessoa".
#(não confundir a classe Pessoa com a variavel pessoa).

def visualizar_agenda()

    while True:
        print("MENU")
        print("===============")
        print("1 - Adicionar / Excluir")
        print("2 - Visualizar agenda")
        escolha = input("Escolha")
        if escolha == 1:
            adicionar_excluir()
        elif escolha == 2:
            visualizar_agenda()
        else:
            print("Opção inválida.")
"""
class Pessoa:
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone


agenda = []


def adicionar_excluir():
    nome = input("Digite o nome: ")
    pessoa_encontrada = None
    for pessoa in agenda:
        if pessoa.get_nome() == nome:
            pessoa_encontrada = pessoa
            break

    if pessoa_encontrada is None:
        telefone = input("Digite o telefone: ")
        nova_pessoa = Pessoa(nome, telefone)
        agenda.append(nova_pessoa)
    else:
        print(f"Nome: {pessoa_encontrada.get_nome()}, Telefone: {pessoa_encontrada.get_telefone()}")
        opcao = input("O que deseja fazer? Adicionar outro telefone (A), excluir nome (N) ou excluir telefone (T)? ")
        if opcao.lower() == "a":
            telefone = input("Digite o novo telefone: ")
            pessoa_encontrada = Pessoa(nome, telefone)
            agenda.append(pessoa_encontrada)
        elif opcao.lower() == "n":
            agenda.remove(pessoa_encontrada)
        elif opcao.lower() == "t":
            telefone = input("Digite o telefone a ser excluído: ")
            if pessoa_encontrada.get_telefone() == telefone:
                print("Não é possível excluir o único telefone registrado.")
            else:
                pessoa_encontrada.__telefone = None
                print("Telefone excluído com sucesso.")
        else:
            print("Opção inválida.")


def visualizar_agenda():
    print("Agenda:")
    for pessoa in agenda:
        print(f"Nome: {pessoa.get_nome()}, Telefone: {pessoa.get_telefone()}")


while True:
    print("================")
    print("MENU")
    print("1- Adicionar / Excluir")
    print("2- Visualizar agenda")
    escolha = input("Escolha: ")

    if escolha == "1":
        adicionar_excluir()
    elif escolha == "2":
        visualizar_agenda()
    else:
        print("Opção inválida.")
