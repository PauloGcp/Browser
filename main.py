#funçoes e variaveis que foram realocadas para facilidade de importação:
from fun_var import *

#classes e seus métodos:
from pilha import *
from verificar import *
from comando_endereço import Switch


            

if __name__ == "__main__":
    

    #programa principal com quem o usuário irá interagir 
    while sair[0] != "#sair":
        print()
        print(f"Historico de navegação: {hist}")
        try:
            print(f"Home: [{p.topo()}]")
        except PilhaException:
            print("Home: []")
        print("Digite a url ou #back para retornar ao endereço anterior: ")
        url = input("URL: ")


        #instanciação de um objeto("verificação") com o objetivo de verificar se a url/comando digitado está no arquivo .txt
        verificaçao = Verificar(url)

        #instanciação de um objeto ("switch") que irá determinar o que será feito de acordo com o que o usuário digitar
        switch = Switch(url)
        
        #bloco determinado para o caso da url/comando estiver no arquivo txt
        if verificaçao.verifica("endereços.txt"):
            switch.função()            
        
        #bloco usado para imprimir uma mensagem ao usuário caso a url/comando não exista no arquivo .txt
        if not verificaçao.verifica("endereços.txt"):
            if url[0] == "#":
                print("Comando inválido")
            if url[0] != "#":
                print("Endereço inválido")

    print("Operação finalizada!")
