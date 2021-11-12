from no import *

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
            print(f"{no.get_valor()} -->", end = '')
            no = no.get_proximo()

    def anterior(self):
        if self.estavazia():
            pass
            

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

            

if __name__ == "__main__":
    p = PilhaEncadeada()
    endereços = ["ab", "cd", "ef", "#back" , "#sair", "#showlist"]

    
    sair = False
    while sair == False:

        #ln 76-85 interface que aparecerá para o usuário
        print()
        print(f"Historico de navegação: [", end = " ")
        p.imprimir()
        print("]")
        try:
            print(f"Home: [{p.topo()}]")
        except PilhaException:
            print("Home: []")
        print("Digite a url ou #back para retornar ao endereço anterior: ")

        #ln 88-104 consulta a lista com as urls e códigos pre-estabelecidos
        url = input("URL: ")
        if url in endereços:
            if url[0] != "#":
                p.empilhar(url)
                print("Página encontrada")
            else:
                if url[1:] == "back":
                    try:
                        p.desempilhar()
                    except PilhaException as pe:
                        print(pe)
                if url[1:] == "sair":
                    sair = True            
        if url not in endereços:
            if url[0]== "#":
                print("Comando inválido")
            else:
                print("Endereço não encontrado")
        


       
            #pagina invalida vai usar a logica de rastrear

    print("Operação finalizada!")

        

