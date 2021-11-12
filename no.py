class No:
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None
    
    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor
    
    def get_proximo(self):
        return self.__proximo
    
    def set_proximo(self, proximo):
        self.__proximo = proximo