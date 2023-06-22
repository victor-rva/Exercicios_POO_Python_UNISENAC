#DICIONARIOS EM PYTHON
"""
#Sintaxe
#d = {key : value, key : value, key : value}

#Declarando o objeto (variável)
#dicionário = {}

agenda = {"Pedro": ["519382940", "519328204"], "Maria": ["519424256", "519302124"], "Ana": "519242035"}
#para poder adicionar mais de um número de telefone os números foram incluidos dentro de uma lista

#Como tratar/manipular um dicionário
#imprimir um dicionário
# print(agenda)
# print(agenda["Maria"])
# print("="*20)


# for pessoa in agenda:
#     print(pessoa)
#
# for pessoa in agenda.values():
#     print(pessoa)
#
# for pessoa, valor in agenda.items():
#     print(pessoa, valor)
#
# for pessoa in agenda.keys():
#     print(pessoa)

# Como adicionar novos elementos no dicionário?
agenda["Carlos"] = ["51342910"]
#Adiconar um novo elemento a lista de um value
agenda["Pedro"].append("519234077")

for pessoa, valor in agenda.items():
    print(pessoa, valor)

#Alterar o value de uma chave
# agenda["Pedro"] = ["51920423"]

#Como excluir algum elemento de um dicionário
agenda.pop("")
del(agenda["Pedro"])

for x in range(5):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone


# Utilizando a estrutura de dicionários, implemente uma agenda, onde a chave será o nome e o value será uma lista de telefones para cada pessoa.
# exemplo:
# agenda = {"Ana" : [999956788, 987875628] }

agenda = {}
telefone = []
for x in range(5):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone

print(agenda)
"""

menu = """
 MENU
 ======================
 1- Adicionar pessoa
 2- Mostrar agenda
 Escolha: """

menu2 = """
 -----MENU
 ======================
 1- Adicionar novo número
 2- Excluir número
 3- Excluir nome
 4- Retorna menu anterior
 Escolha: """

agenda ={}

def get_numeros(lst_fones):
    fones = ""
    for telefone in lst_fones:
        fones += " - " + telefone
    return fones

def novo_numero(nome):
    print(f"Nome: {nome} - {get_numeros(agenda[nome])}")
    novo_numero = input("Novo número: ")
    agenda[nome].append(novo_numero)

def excluir_numero(nome):
    ind = 1
    for telefone in agenda[nome]:
        print(f" {ind} {telefone}")
        ind += 1
    escolha = int(input("Escolha pelo indicie: "))

    numero_excluir = input("Número para excluir: ")
    agenda[nome].pop(escolha - 1)
    #  A posição sempre começa em 0
    #agenda[nome].remove(numero_excluir)

def excluir_nome(nome):
    del(agenda[nome])

def isAgenda():
    if not agenda:
        input ("AGENDA VAZIA!")
        return False
    return True

def mostrar_agenda():
    if isAgenda():
        for nome, numeros in agenda.items():
            print(f"""
        Nome: {nome}
        Fones: {numeros}
        """)

def continuar():
     while True:
         op = input("Adicionar alguem? s/n: ") == 'n'.lower()
         if op == "s": return True
         if op == "n": return False

         input("Resposta incorreta")

def visualizar_agenda():
    if isAgenda():
        print("Agenda: ")
        for pessoa in agenda:
            print(pessoa)

def adicionar_agenda():
    while True:
        if not continuar():
            break
        nome = input("Nome: ")

        if nome not in agenda:
            telefone = input("Telefone: ")
            agenda[nome] = [telefone]
            continue

        escolha = input(menu2)
        if escolha == '1': novo_numero(nome)
        if escolha == '2': excluir_numero(nome)
        if escolha == '3': excluir_nome(nome)
        if escolha == '4': break

#===============================
def main():
    while True:
        escolha = input(menu)
        if escolha == '1': adicionar_agenda()
        if escolha == '2': mostrar_agenda()


if __name__ == '__main__':
    main()