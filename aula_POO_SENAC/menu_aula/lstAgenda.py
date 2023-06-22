
agenda = list()

def agenda_existe(nome):

    for pessoa in agenda:
        if pessoa.get_nome() == nome:
            return True
    return False

def agenda_adicionar_novo(pessoa):
    agenda.append(pessoa)

def get_pessoa_agenda(nome):
    for pessoa in agenda:
        if pessoa.get_nome() == nome:
            return pessoa

def excluir_pessoa_agenda(pessoa):
    agenda.remove(pessoa)

def mostrar_agenda():
    print("\n"*5)
    print("Visualizando agenda:")
    print("====================")
    for pessoa in agenda:
        print(pessoa)
    input("Fim Agenda. Enter.")


