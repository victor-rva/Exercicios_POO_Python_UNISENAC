import json
import os
from datetime import datetime
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

dict_visitas = {}

def cadastrar_profissional():
    """
    Cadastra um profissional com nome, especialidade e sala e armazena na lista l_profissionais.
    """
    nome = input("Digite o nome do profissional: ")
    especialidade = input("Digite a especialidade do profissional: ")
    sala = input("Digite a sala do profissional: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)
    print("Profissional cadastrado com sucesso!")

def cadastrar_visitante():
    """
    Cadastra um visitante com nome e documento e armazena na lista l_visitantes.
    """
    nome = input("Digite o nome do visitante: ")
    documento = input("Digite o documento do visitante: ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)
    print("Visitante cadastrado com sucesso!")

def localizar_profissional():
    """
    Localiza um profissional pelo nome ou pela especialidade e exibe seu nome, especialidade e sala.
    """
    opcao = input("Digite 1 para localizar pelo nome ou 2 para localizar pela especialidade: ")
    if opcao == "1":
        nome = input("Digite o nome do profissional: ")
        for profissional in l_profissionais:
            if profissional.get_nome().lower() == nome.lower():
                print("Nome:", profissional.get_nome())
                print("Especialidade:", profissional.get_especialidade())
                print("Sala:", profissional.get_sala())
                return
        print("Profissional não encontrado.")
    elif opcao == "2":
        especialidade = input("Digite a especialidade do profissional: ")
        for profissional in l_profissionais:
            if profissional.get_especialidade().lower() == especialidade.lower():
                print("Nome:", profissional.get_nome())
                print("Especialidade:", profissional.get_especialidade())
                print("Sala:", profissional.get_sala())
                return
        print("Profissional não encontrado.")
    else:
        print("Opção inválida.")

def registrar_visita():
    """
    Registra uma visita associando um visitante e um profissional, e armazena os dados da visita no dicionário dict_visitas.
    """
    documento = input("Digite o documento do visitante: ")
    for i, visitante in enumerate(l_visitantes):
        if visitante.get_documento() == documento:
            print(i + 1, ". Visitante:", visitante.get_nome())
            for j, profissional in enumerate(l_profissionais):
                print(j + 1,". Profissional:", profissional.get_nome(), "- Especialidade:", profissional.get_especialidade())
            opcao_profissional = int(input("Digite o número correspondente ao profissional visitado: "))
            if opcao_profissional >= 1 and opcao_profissional <= len(l_profissionais):
                profissional = l_profissionais[opcao_profissional - 1]
                data_entrada = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
                dict_visitas[documento] = {
                    "nome_profissional": profissional.get_nome(),
                    "hora_entrada": data_entrada,
                    "sala": profissional.get_sala()
                }
                print("Visita registrada com sucesso!")
            else:
                print("Opção inválida. Tente novamente.")
            break
    else:
        print("Visitante não encontrado.")

def relatorio_conferencia():
    """
    Gera um relatório de conferência mostrando todos os visitantes de um profissional e a data da visita.
    """
    print("Lista de profissionais:")
    for i, profissional in enumerate(l_profissionais):
        print(f"{i+1}. Nome: {profissional.get_nome()}, Especialidade: {profissional.get_especialidade()}, Sala: {profissional.get_sala()}")
    
    profissional_index = int(input("Selecione o número do profissional: ")) - 1
    
    if profissional_index < 0 or profissional_index >= len(l_profissionais):
        print("Índice inválido!")
        return
    
    profissional = l_profissionais[profissional_index]
    
    print(f"Relatório de conferência para o profissional {profissional.get_nome()}:")
    for documento, visita in dict_visitas.items():
        if visita["nome_profissional"] == profissional.get_nome():
            visitante_documento = documento
            visitante_nome = ""
            for visitante in l_visitantes:
                if visitante.get_documento() == visitante_documento:
                    visitante_nome = visitante.get_nome()
                    break
            print(f"Visitante: {visitante_nome}")
            print(f"Data da Visita: {visita['hora_entrada']}")
            print()
        
def gerar_arquivo_registros():
    """
    Gera um arquivo JSON com os registros das visitas do dia.
    """
    registros = {}

    for documento, visita_data in dict_visitas.items():
        profissional_nome = visita_data["nome_profissional"]
        hora_entrada = visita_data["hora_entrada"]
        sala = visita_data["sala"]

        registros[documento] = {
            "nome_profissional": profissional_nome,
            "hora_entrada": hora_entrada,
            "sala": sala
        }

    file_path = "registros_dia.json"

    try:
        with open(file_path, "w") as file:
            #as file garante que o objeto de arquivo seja fechado após a conclusão do bloco with.
            json.dump(registros, file, indent=4)
            #A função json.dump()é utilizada para serializar o dicionário no formato JSON e gravá-lo no arquivo.
            #O parâmetro indent=4é usado ao chamar a função json.dump()para especificar a quantidade de espaços a serem usados ​​na formatação do arquivo JSON
        print(f"Arquivo {file_path} gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao gerar arquivo: {str(e)}")
        # a mensagem de erro será exibida utilizando a expressão {str(e)}, onde e é a variável que contém a exceção capturada.

def ler_arquivos():
    """
    Lê os arquivos de texto "profissionais.txt" e "visitantes.txt" e converte os dados para JSON.
    """
          
    try:
        with open('profissionais.txt', 'r') as file:
            for line in file:
                nome, especialidade, sala = line.strip().split(':')
                profissional = Profissional(nome, especialidade, sala)
                l_profissionais.append(profissional)

        with open('visitantes.txt', 'r') as file:
            for line in file:
                nome, documento = line.strip().split(':')
                visitante = Visitante(nome, documento)
                l_visitantes.append(visitante)
    except FileNotFoundError:
        print("Arquivo não encontrado.")


menu = """======================
MENU
======================
0- Encerrar Programa
1- Cadastrar Profissional
2- Cadastrar Visitante
3- Localizar Profissional
4- Registrar Visita
5- Relatório de Conferência
6- Gerar arquivo de Registros do dia
Escolha:"""


def main():
    while True:
        ler_arquivos()
        escolha = input(menu)
        if escolha == "0": break
        if escolha == "1": cadastrar_profissional()
        if escolha == "2": cadastrar_visitante()
        if escolha == "3": localizar_profissional()
        if escolha == "4": registrar_visita()
        if escolha == "5": relatorio_conferencia()
        if escolha == "6": gerar_arquivo_registros()   


if __name__ == "__main__":
    main()

