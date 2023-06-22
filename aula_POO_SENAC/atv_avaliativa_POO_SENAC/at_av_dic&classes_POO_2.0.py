class Relevancia:
    def __init__(self):
        self.__desemprego = None
        self.__etica = None
        self.__seguranca = None
        self.__regulamentacao = None
        self.__potencial = None

    def desemprego(self, desemprego):
        self.__desemprego = desemprego

    def etica(self, etica):
        self.__etica = etica

    def seguranca(self, seguranca):
        self.__seguranca = seguranca

    def regulamentaca(self, regulamentacao):
        self.__regulamentacao = regulamentacao

    def potencial(self, potencial):
        self.__potencial = potencial


menu = """Menu
        0- Finalizar o Programa
        1- Realizar avaliação
        2- Relatório
        Escolha:"""



pesquisa = {"AC", "AL", "AP", "AM",\
                 "BA", "CE", "DF", "ES",\
                 "GO", "MA", "MT", "MS",\
                 "MG", "PA", "PB", "PR",\
                 "PE", "PI", "RJ", "RS",\
                 "RO", "RR", "SC", "SP",\
                 "SE", "TO"}
lista_relevancia = []

# for estados in lista_estados:
#     pesquisa[estados] = None

def realizar_avaliacao():
    # while True:
    sigla = input("Qual estado você reside?(SIGLA): ").upper
    for sigla in pesquisa:
        # if sigla not in lista_estados:
        #     break
        # else:
        #     print("Esse estado não existe no Brasil. Tente novamente")
        objRelevancia = Relevancia()
        objRelevancia.desemprego = int(input("Qual o grau de relevância para Desemprego e desigualdade (1-5)? "))
        objRelevancia.etica = int(input("Qual o grau de relevância para Questões éticas e morais (1-5)? "))
        objRelevancia.seguranca = int(input("Qual o grau de relevância para Segurança cibernética e privacidade (1-5)? "))
        objRelevancia.regulamentacao = int(input("Qual o grau de relevância para Controle e regulamentação (1-5)? "))
        objRelevancia.potencial = int(input("Qual o grau de relevância para Potencial desenvolvimento de IA superinteligente (1-5)? "))
        lista_relevancia.append(objRelevancia)
        indice_chave = pesquisa
        pesquisa[] = lista_relevancia
        print(pesquisa)


def relatorio():
    estado = input("Você deseja saber a média da pesquisa sobre qual estado? ").upper
    if estado in pesquisa:
        print(f"Estado: {estado}")
        for estado, relevancia in pesquisa[estados:Relevancia()]:
            print(f"Desemprego e desigualdade: {relevancia._Relevancia__desemprego}")
            print(f"Questões éticas e morais: {relevancia._Relevancia__etica}")
            print(f"Segurança cibernética e privacidade: {relevancia._Relevancia__seguranca}")
            print(f"Controle e regulamentação: {relevancia._Relevancia__regulamentacao}")
            print(f"Potencial desenvolvimento de IA superinteligente: {relevancia._Relevancia__potencial}")


def main():
    while True:
        escolha = input(menu)
        if escolha == "0": break
        if escolha == "1": realizar_avaliacao()
        if escolha == "2": relatorio()


if __name__ == "__main__":
    main()
