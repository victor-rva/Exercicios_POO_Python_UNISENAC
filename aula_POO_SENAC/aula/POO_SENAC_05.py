"""
- Para a opção 1 do menu crie uma função chamada
adicionar_dados() que, por sua vez, vai chamar as
funções já criadas:
adiciona_nome()
adiciona_matricula()

- Para opção 2 do menu faça a chamada afunção
imprimir_dados().

-Crie uma função chamada inicio() para executar o
menu a baixo:
"""
def adicionar_dados():
    adiciona_nome(ler_nome())
    adiciona_matricula(ler_matricula())

def inicio():
    while True:
        escolha = input('''
        Menu
        ====================
        1- Adicionar nome
        2- imprimir dados
        ====================
        Escolha: ''')

        if escolha == "1":
            adicionar_dados()
        if escolha == '2':
            imprimir_dados()

if __name__ == '__main__':
    inicio()
