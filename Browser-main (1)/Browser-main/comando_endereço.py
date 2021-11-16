from pilha import PilhaException
from fun_var import p, hist, sair, endereços
from verificar import *


class Switch:
    def __init__(self, url):
        self.__url = url

    #método que será usado no código principal para retornar as ações adequadas de acordo com o que foi solicitado pelo usuário
    def função(self):
        self.__comando = self.__url

        #bloco que determina se o input(variável "url" no código principal) é um comando. Exemplo: #back, #sair, #mostrar.
        if self.__comando[0] == "#":
            if self.__comando[1:] == "back":
                try:
                    p.desempilhar()
                    hist.pop()
                except PilhaException as pe:
                    print(pe)
                
            if self.__comando[1:] == "sair":
                sair.insert(0, self.__comando)
            
            #Caso o usuávio opte por adicionar um novo endereço, será feito o teste para saber se o modelo de endereço digitado é válido;
            #após isso, é verificado se o endereço não está no arquivo .txt, caso o endereço seja desconhecido nesse arquivo é feito a adição do endereço (tanto diretamente no arquivo .txt quando 
            #no array "endereços"). Obs.: "endereços" é explicado no arquivo "fun_var.py"
            if self.__comando[1:] == "add":
                per = input('Qual endereco deseja adicionar? ')
                if per[0:4] == "www." or per[0:7] == "http://":
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

            if self.__comando[1:] == "mostrar": 
                print(f"Endereços e comandos disponíveis: {endereços}")
        
        #Bloco que determina se o input(variável "url" no código principal) é um endereço. Exemplo: www.ifpb.edu, www.facebook.com.
        #Após a verificação inicial, irá ocorrer um teste para impossibilitar a repetição do endereço na pilha("p") e no array ("hist").
        if self.__comando[0] != "#":
            if len(hist) == 0 or self.__comando != p.topo():
                p.empilhar(self.__comando)
                hist.append(self.__comando)
                print("Página encontrada")
            else:
                print("Página atual.")    

        
        
        
        