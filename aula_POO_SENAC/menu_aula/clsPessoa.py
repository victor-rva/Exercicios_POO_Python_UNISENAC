class Pessoa:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefones = [telefone]

    def get_nome(self):
        return self.__nome

    def adicionar_telefone(self, telefone):
        self.__telefones.append(telefone)

    def excluir_numero(self, numero_ser_exluido):
        if numero_ser_exluido in self.__telefones:
            self.__telefones.remove(numero_ser_exluido)
        else:
            print("Número não localizado. ")
            input("Enter")

    def __str__(self):
        return f"Nome: {self.__nome} - {self.__telefones}"

