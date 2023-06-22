#aula05

# Crie uma classe Aluno com os seguintes
# atributos de instância:
# - nome
# - matricula
# - data_nascimento
#
# Crie uma lista com instâncias desta classe
#   - crie uma função para adicionar alunos na lista
#   - crie uma função para verificar se um aluno existe
#       ou não na lista. Esta função deve retornar os
#       dados de aluno, mas caso o aluno não conste na
#       lista, retorne a mensagem "ALUNO NÃO MATRICULADO"
#       > consulte pela matrícula ou nome
#   - crie uma função para mostrar todos os alunos da
#       lista, com nome e matricula.


class Aluno:
    idade = 0 #atributo de classe porque está fora das funções. Podem ser visiveis para todos os objetos, diferente dos
              #atributos de instância.

    def __init__(self, nome, matricula, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento

    def __str__(self):
         return f"Aluno: {self.nome} {self.matricula}{self.data_nascimento}"

    def mostrar_dados(self):
        return f"Aluno: {self.nome} {self.matricula}{self.data_nascimento}"

    def nome_matricula(self):
        return f"Aluno: {self.nome} {self.matricula}"

"""    
a = Aluno("Victor", 12325, "03/02/2003")
print(a.matricula)
print(a)
print(a.nome_matricula())
"""

#__init__ tem a função de inicializar os atributos
#self define o endereço de memória onde os objetos ficarão
#objeto é uma variavel que eu criei com as caracteristicas que eu quis

lista_alunos = []

a = Aluno("Victor", 1111, "03/02/2003")
a2 = Aluno("Ana", 2222, "15/06/2001")
a3 = Aluno("Ned", 3333, "07/04/2000")

lista_alunos.append(a)
lista_alunos.append(a2)
lista_alunos.append(a3)

for alu in lista_alunos:
    print(alu)
    print(alu.nome)
    print(alu.mostrar_dados())
    #print(alu.__str__()) é a mesma coisa que print(alu)

"""
Visibilidade de metodos e atributos -> está ligada aos metodos e aos atributos de uma classe
- pública -> é o padrão do python
- restrita -> (é um jeito de indicar para outros desenvolvedores não mexerem na variavel; se usa o underline (_). ex:self._nome;
só que isso muda o nome da variavel/não existe no python)
- privada -> se usa dois underline na frente da variavel (__). ex:self.__nome, 
os atributos e variaveis só podem ser acessados dentro da classe que eles existem,só que isso muda o nome da variavel
"""