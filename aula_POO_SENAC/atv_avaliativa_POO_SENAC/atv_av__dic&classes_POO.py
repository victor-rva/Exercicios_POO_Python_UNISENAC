class Relevancia:
    def __init__(self,desemprego, etica, seguranca, regulamentacao, potencial):
        self.__desemprego = desemprego
        self.__etica = etica
        self.__seguranca = seguranca
        self.__regulamentacao = regulamentacao
        self.__potencial = potencial

    def desemprego(self, desemrpego):
        self.__desemprego = None

pesquisa = {}
lista_estados = ["AC", "AL", "AP", "AM",
                 "BA", "CE", "DF", "ES",
                 "GO", "MA", "MT", "MS",
                 "MG", "PA", "PB", "PR",
                 "PE", "PI", "RJ", "RS",
                 "RO", "RR", "SC", "SP",
                 "SE", "TO"]

for estados in lista_estados:
    pesquisa[estados] = Relevancia()


def realizar_avaliacao():
    estado = input("Qual estado você reside? ").upper

    desemprego = int(input("Qual o grau de relevância para Desemprego e desigualdade (1-5)? "))
    etica = int(input("Qual o grau de relevância para Questões éticas e morais (1-5)? "))
    seguranca = int(input("Qual o grau de relevância para Segurança cibernética e privacidade (1-5)? "))
    regulamentacao = int(input("Qual o grau de relevância para Controle e regulamentação (1-5)? "))
    potencial = int(input("Qual o grau de relevância para Potencial desenvolvimento de IA superinteligente (1-5)? "))
    pesquisa[estados] = Relevancia(desemprego, etica, seguranca, regulamentacao, potencial)


def relatorio():
    estado = input("Você deseja saber a média da pesquisa sobre qual estado?")
    for estado, r in pesquisa.items():
        if estado == pesquisa[tupla]:
            print(f"Estado: {estado}")
            # for estado, relevancia in pesquisa.items():
            #     if estado ==
            print(f"Desemprego e desigualdade: {r._Relevancia__desemprego}")
            print(f"Questões éticas e morais: {r._Relevancia__etica}")
            print(f"Segurança cibernética e privacidade: {r._Relevancia__seguranca}")
            print(f"Controle e regulamentação: {r._Relevancia__regulamentacao}")
            print(f"Potencial desenvolvimento de IA superinteligente: {r._Relevancia__potencial}")


menu = """Menu
        0- Finalizar o Programa
        1- Realizar avaliação
        2- Relatório
        Escolha:"""

def main():
    while True:
        escolha = input(menu)
        if escolha == "0": break
        if escolha == "1": realizar_avaliacao()
        if escolha == "2": relatorio()

if __name__ == "__main__":
    main()


