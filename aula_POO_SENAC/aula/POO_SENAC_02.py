"""
-Faça uma função que retorne a matrícula
lida de um aluno. Nome da função: ler_matricula()
    (somente dígitos alfanuméricos)
    (Não precisa verificar a quantidade de dígitos)
"""

def ler_matricula():
    while True:
        matricula = input("Digite a matrícula do aluno: ")
        if not matricula.isnumeric():
            #for c in matricula
            #if c not in "0123456789"
            print("Matrícula deve ser númerica.")
            continue
        break
    return matricula
