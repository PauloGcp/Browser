
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
        
class PilhaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class PilhaEncadeada:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def estavazia(self):
        return self.__tamanho == 0


    def empilhar(self, valor):
        if self.estavazia():
            self.__topo= No(valor)
        else:
            topo_antigo = self.__topo
            topo_novo = No(valor)
            topo_novo.set_proximo(topo_antigo)
            self.__topo = topo_novo
        self.__tamanho +=1
    
    def get_posiçao(self, indice):
        contador = 0
        no = self.__topo
        while no:
            if contador == indice:
                return no.get_valor()
            no = no.get_proximo()
            contador += 1 

    

    def tamanho(self): 
        return self.__tamanho


    def imprimir(self):
        no = self.__topo
        while no:
            print(f"{no.get_valor()} <--", end = '')
            no = no.get_proximo()
            

    def desempilhar(self):
        if not self.estavazia():
            topo = self.__topo
            self.__topo = topo.get_proximo()
            self.__tamanho -= 1
            return topo.get_valor()
        raise PilhaException("Histórico já vazio")

    def topo(self):
        if not self.estavazia():
            return self.__topo.get_valor()
        raise PilhaException("Histórico já vazio")