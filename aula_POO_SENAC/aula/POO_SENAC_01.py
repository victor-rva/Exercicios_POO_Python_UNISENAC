"""
-Faça uma função que retorne o nome lido
de um aluno. Nome da função: ler_nome()
    (o nome deve ter no mínimo 3 caracteres)
    (não pode aceitar números)
"""
def ler_nome():
    while True:
        nome = input("Digite o nome do aluno:")
        if len(nome) < 3:
            print("Nome com 3 caracteres no mínimo.")
            continue
        if not nome.replace(" ", " ").isalpha():
            print("Somente caracteres alfanuméricos")
            continue
        break
    return nome

print(ler_nome())


