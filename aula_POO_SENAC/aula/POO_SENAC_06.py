lista_nomes = ["victor", "vitão"]
lista_matriculas = ["12345", "67890"]
lista_alunos = []

class Aluno():
    nome = None
    matricula = None

a1 = Aluno()
a1.nome = "Pedro"
a1.matricula = "13590"

a2 = Aluno()
a2.nome = "Ana"
a2.matricula = "49240"

a3 = Aluno()
a3.nome = "João"
a3.matricula = "50352"

a4 = Aluno()
a4.nome = "Victor"
a4.matricula = "94873"

lista_alunos.append(a1)
lista_alunos.append(a2)
lista_alunos.append(a3)
lista_alunos.append(a4)

for Aluno in lista_alunos:
    print(Aluno.nome)
    print(Aluno.matricula)

#classes começam com letra maiúscula,variáveis começam com letra minúscula
