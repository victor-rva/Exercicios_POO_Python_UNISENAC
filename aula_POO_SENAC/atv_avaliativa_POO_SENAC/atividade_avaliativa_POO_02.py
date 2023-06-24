import json
"""
 Tarefa 3
 Competências avaliadas:
 - Desenvolver uma solução viável para o problema;
 - Saber utilizar classes e objetos;  
 - Saber utilizar dicionários e listas;  
 - Saber manipular arquivos de texto;
 - Códigos iguais == D;
 

'''
Faça um algoritmo que controle o acesso de pessoas a um estabelecimento comercial.
Para isso você deverá utilizar as seguintes classes:

Crie uma classe Profissional com os atributos:
- nome
- especialidade
- sala
Todos atributos devem ser privados e string.
Crie uma classe Visitante com os atributos:
- nome
- documento
Todos atributos devem ser privados e string.

Crie a classe Visita com os atributos:
- visitante
- profissional
- data_entrada
O atributo visitante deverá ser um objeto da classe Visitante escolhido de l_visitantes.
O atributo profissional deverá ser um objeto da classe Profissional escolhido de l_profissionais.
Crie os métodos que forem necessários para acessar os atributos das classes.


Desenvolva seu código a partir do menu abaixo:

======================
MENU
======================
1- Cadastrar Profissional
2- Cadastrar Visitante
3- Localizar Profissional
4- Registrar Visita
5- Relatório de Conferência
6- Gerar arquivo de Registros do dia
7- Ler arquivos profissionais / visitantes
Escolha:


Na opção 1 do menu cadastre o nome, especialidade e sala onde o profissional atende.
                      Armazene esses dados na lista l_profissionais (como objetos).

Na opção 2 do menu será cadastrado o visitante com nome, documento.
                      Armazene esses dados na lista l_visitantes (como objetos).

Na opção 3 do menu é possível localizar um profissional pelo nome ou pela profissão.
                      Serve para o caso do visitante não saber a sala do profissional.
                      (Apenas mostrar na tela o nome, profissão e a sala do profissional)

Na opção 4 do menu será registrado a visita.
                      Escolha o visitante (da lista de visitantes) e o profissional (da lista_profissionais),
                           busque a data do computador e armazene a visita em um dicionário 'dict_visitas'.
     { visitante :
          { nome_profissional : "" ,
            hora_entrada : "",
            sala : ""
          }
     }

Na opção 5 do menu apenas crie um relatório de conferência.
                      Selecione o profissional e mostre todos os visitantes e a data da visita.

Na opção 6 do menu, gere um arquivo JSON com os registros do dia.
     { numero_documento_visitante :
          { nome_profissional : "" ,
            hora_entrada : "",
            sala : ""
          }
     }

Na opção 7 do menu, ler os arquivos em TXT 'profissionais.txt' e 'visitantes.txt' para iniciar o programa.


Obs. Em todas as listas serão armazenados as instâncias de suas classes.
               


==============================================
Arquivo profissionais.txt

João Batista:DENTISTA:1001
Carlos Augusto:CLINICO:1002
Alvaro Correa da Silva:DENTISTA:2001
Carolina Klinks:OBSTETRA:2002
Joana Augusta da Silva:DENTISTA:2004
Antonio Machado:ADVOGADO:4001
Ana Marques:PSICOLOGA:4002



Arquivo visitantes.txt
Silvio Antônio:1122334455
Maria Eugênia Moura:2233445566
Carla Antônia Kling:3344556677
Amanda Corlola:4455667788
Claudio de Moraes Locco:5566778899
Ricardo Santos de Souza:6677889911
Neusa Maria de Britto:1112223334444
Creusa Antunes:2223334445555
Marcio Pinto Cabritto:3334445556666
Jonas Machado:4445556667777

'''
"""

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala
        
    def get_nome(self):
        return self.__nome
    
    def get_especialidade(self):
        return self.__especialidade
    
    def get_sala(self):
        return self.__sala    
        
class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento
        
    def get_nome(self):
        return self.__nome
    
    def get_documento(self):
        return self.__documento
         
class Visita:
    def __init__(self, visitante, profissional, entrada):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__entrada = entrada
        
    def get_visitante(self):
        return self.__visitante
        
    def get_profissional(self):
        return self.__profissional
    
    def get_entrada(self):
        return self.__entrada        
        
        
l_profissionais = []
l_visitantes = []

dicionario_visitas = {}

def cadastrar_profissional():
    nome = input("Digite o nome do profissional: ")
    especialidade = input("Digite a especialidade do profissional: ")
    sala = input("Digite a sala do profissional: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)
    print("Profissional cadastrado com sucesso!")

def cadastrar_visitante():
    nome = input("Digite o nome do visitante: ")
    documento = input("Digite o documento do visitante: ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)
    print("Visitante cadastrado com sucesso!")

def localizar_profissional():
    pass

def registrar_visita():
    pass

def relatorio_conferencia():
    pass

def gerar_arquivo_registros():
    pass

def ler_arquivos():
    pass
    

menu = """======================
MENU
======================
1- Cadastrar Profissional
2- Cadastrar Visitante
3- Localizar Profissional
4- Registrar Visita
5- Relatório de Conferência
6- Gerar arquivo de Registros do dia
7- Ler arquivos profissionais / visitantes
Escolha:"""


def main():
    while True:
        escolha = input(menu)
        if escolha == "0": break
        if escolha == "1": cadastrar_profissional()
        if escolha == "2": cadastrar_visitante()
        if escolha == "3": localizar_profissional()
        if escolha == "4": registrar_visita()
        if escolha == "5": relatorio_conferencia()
        if escolha == "6": gerar_arquivo_registros()
        if escolha == "7": ler_arquivos()
            

if __name__ == "__main__":
    main()

