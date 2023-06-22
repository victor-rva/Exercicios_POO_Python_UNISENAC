"""
Criar uma classe Porta com os atributos:
    altura
    largura
    material
    cor
    aberta
    instalada
Obs. O material deve ser um parâmetro de instância.
    Todos os atributos devem ser privados.
    Os valores default são:
        - altura = 280 - largura = 80 - cor = none
        - aberta = none - insyalda = none
"""


class Porta:

    # #Outra forma de fazer:
    # def __init__(self, material, altura=210, largura=80, cor=None, aberta=None, instalada=None):
    # #Quando um parâmetro é obrigatório na função ele vai primeiro (ele é obrigatório porque não tem valor padrão
    #     self.__altura = altura
    #     self.__largura = largura
    #     self.__material = material
    #     self.__cor = cor
    #     self.__aberta = aberta
    #     self.__instalada = instalada

    def __init__(self, material):
        self.__altura = 210
        self.__largura = 80
        self.__material = material
        self.__cor = None
        self.__aberta = None
        self.__instalada = None

    """
    ===========================================
    Criar os métodos:
    - abrir
    - fechar
    - instalar
    - pintar

    Obs. Só posso abrir ou fechar a porta se estiver instalada.
    O método pintar recebe a cor como parâmetro.
    """

    def isInstalada(self):
        return self.__instalada

    def abrir(self):
        if self.isInstalada():
            if self.__instalada:
                self.__aberta = True

    def fechar(self):
        if self.isInstalada():
            if self.__instalada:
                self.__aberta = False

    def instalar(self):
        self.__instalada = True

    def pintar(self, cor):
        self.__cor = cor

    def __str__(self):
        # return f"Porta: {self.__aberta, self.__aberta, self.__instalada, self.__cor}"
        if self.__instalada:
            return f"""
            Altura: {self.__altura}
            Largura: {self.__largura}
            Material: {self.__material}
            Cor: {self.__cor}
            Aberta: {self.__aberta}
            Instalada: {self.__instalada}
            """
        else:
            return f"Porta não instalda."


porta1 = Porta("Cobre")
print(porta1)

porta2 = Porta("Madeira")
porta2.instalar()
porta2.pintar("Vermelha")
print(porta2)

"""
===================================
-> Declare uma lista de larguras de portas aceitaveis. lst_larguras_portas = [60, 70, 80, 90, 100].
-> Crie uma função - escolher_largura_porta - que receba a lista de larguras de portas como parâmetro e retorne uma das
opções da lista.
-> Altere seu código para que receba também a largura como parâmetro para a instância de uma nova porta.    
"""

