from pilha import PilhaException
from fun_var import p, hist, sair

class Switch:
    def __init__(self,url):
        self.__url= url

    def função(self):
        self.__comando = self.__url
        
        if self.__comando[0] == "#":
            if self.__comando[1:] == "back":
                try:
                    p.desempilhar()
                    hist.pop()
                except PilhaException as pe:
                    print(pe)
            
            if self.__comando[1:] == "sair":
                sair.insert(0, self.__comando)

            if self.__comando[1:] == "add <url>":
                per = str(input('Qual endereco deseja adicionar? '))
                if per not in endereços:
                    with open('trabalho/endereços.txt', 'a') as arquivo:
                        arquivo.write(str(per) + '\n')
                    print('Página adicionada com sucesso!')
                else:
                    print('A página não foi adicionada, pois já existe.')
            if self.__comando[1:] == "showhist":
                print(f"Histórico de navegação: {hist}")   

        if self.__comando[0] != "#":
                if len(hist) == 0 or self.__comando != p.topo():
                    p.empilhar(self.__comando)
                    hist.append(self.__comando)
                    print("Página encontrada")
                else:
                    print("Página atual.")     
        
        
        
