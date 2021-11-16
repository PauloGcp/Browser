#*classe documentada no código principal*
class Verificar:
    def __init__(self,entrada):
        self.__entrada = entrada
        self.__verificar = False

    def verifica(self, arq):
        with open(arq) as arquivo:
            for links in arquivo:
                links = links.strip("\n")
                if links == self.__entrada:
                    self.__verificar = True
                    return self.__verificar
            
