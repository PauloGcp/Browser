from pilha import PilhaException
from fun_var import p, hist, sair, endereços
from verificar import *


class Switch:
    def __init__(self, url):
        self.__url = url

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
                per = input('Qual endereco deseja adicionar? ')
                if per[0:4] == "www.":
                    if per not in endereços:
                        with open('endereços.txt', 'a') as arquivo:
                            arquivo.write(str(per) + '\n')
                            endereços.append(per)
                        print('Página adicionada com sucesso!')
                
                    else:
                        print('A página não foi adicionada, pois já existe.')

                else:
                    print("A página não foi adicionada pois está em um formato inválido.")
                    
            if self.__comando[1:] == "showhist":
                print(f"Histórico de navegação: {hist}")   

        if self.__comando[0] != "#":
            if len(hist) == 0 or self.__comando != p.topo():
                p.empilhar(self.__comando)
                hist.append(self.__comando)
                print("Página encontrada")
            else:
                print("Página atual.")    

        
        
        
        