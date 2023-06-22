
from lstAgenda import *
from clsPessoa import Pessoa
import os


menu_principal = """

MENU
========================
1- Adicionar / Excluir
2- Visualizar agenda
 Escolha: """

menu_secudario = """

MENU
============================
1- Adicionar novo Número
2- Excluir a Pessoa
3- Excluir Número existente
 Escolha: """

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    clear()
    escolha = input(menu_principal)
    if escolha == "1":
        adicionar_excluir()
    if escolha == "2":
        mostrar_agenda()
    menu()

def sub_menu():
    return input(menu_secudario)


def ler_nome():
    return input(
    """===============================
    | Nome: """)

def ler_telefone(nome):
    return input(
    f"""    | Telefone: """)
    # return input(
    # f"""===============================
    # | Nome: {nome}
    # | Telefone: """)

def adicionar_novo_numero(pessoa, telefone):
    pessoa.adicionar_telefone(telefone)

def alterar_agenda(nome):
    pessoa = get_pessoa_agenda(nome)
    print(pessoa)
    escolha = sub_menu()
    if escolha == "1":
        novo_numero = ler_telefone(nome)
        adicionar_novo_numero(pessoa, novo_numero)
    elif escolha == "2":
        if input(f"Confirma exclusão de {pessoa.get_nome()} s/n? ").upper() == "S":
            excluir_pessoa_agenda(pessoa)
            input("Ok. Excluido. Enter.")
        else:
            input("Exclusão cancelada. Enter.")
    elif escolha == "3":
        numero_ser_exluido = ler_telefone(nome)
        if input(f"Confirma exclusão do número: {numero_ser_exluido} de {nome}").upper() == "S":
            pessoa.excluir_numero(numero_ser_exluido)
            print("Número excluido. Enter.")
        else:
            print("Número cancelado. Enter.")

def adicionar_excluir():
    print("\n"*2)
    print("Adicionar / Excluir da Agenda: ")
    nome = ler_nome()
    if agenda_existe(nome):
        alterar_agenda(nome)
    else:
        telefone = ler_telefone(nome)
        agenda_adicionar_novo(Pessoa(nome, telefone))



if __name__ == "__main__":
    menu()










