#funçoes e variaveis que foram realocadas para facilidade de importação:
from fun_var import *

#classes e seus métodos:
from pilha import *
from verificar import *
from comando_endereço import Switch


            

if __name__ == "__main__":
    print(endereços)
    print(linha)


    
    while sair[0] != "#sair":
        
        print()
        print(f"Historico de navegação: {hist}")
        try:
            print(f"Home: [{p.topo()}]")
        except PilhaException:
            print("Home: []")
        print("Digite a url ou #back para retornar ao endereço anterior: ")

        
        url = input("URL: ")
        verificaçao = Verificar(url)
        switch = Switch(url)
        
        
        if verificaçao.verifica("trabalho/endereços.txt"):
            switch.função()            
               
        if not verificaçao.verifica("trabalho/endereços.txt"):
            if url[0] == "#":
                print("Comando inválido")
            if url[0] != "#":
                print("Endereço inválido")

            
            

        

    print("Operação finalizada!")
