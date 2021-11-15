'''from r_w import *


endereços = []

for linha in ler_arquivo("trabalho/endereços.txt"):
    linha = linha.strip()
    if '/' in linha:
        linha_simples = linha
        linha_composta = linha.split('/')
        for i in linha_composta:
            endereços.append(i)
    else:
        endereços.append(linha)

print(linha_simples)
print(linha_composta)
print(endereços)

url = input("Informe a url: ")

if url == linha_composta[0]:
    print(linha_composta[0])
    print(linha_composta[1:])

if url == f"/{linha_composta[1:]}":
    print(url)







#from os import execlp
from fun_var import *
from pilha import *


            

if __name__ == "__main__":
    p = PilhaEncadeada()
    print(endereços)
    print(linha)


    sair = False
    while sair == False:
        
        print()
        print(f"Historico de navegação: {hist}")
        try:
            print(f"Home: [{p.topo()}]")
        except PilhaException:
            print("Home: []")
        print("Digite a url ou #back para retornar ao endereço anterior: ")

        
        url = input("URL: ")
        if url in endereços:


            if url[0] == "#":
                if url == "#back":
                    try:
                        p.desempilhar()
                        hist.pop()
                    except PilhaException() as pe:
                        print(pe)
                if url == "#sair":
                    sair = True
                if url == "#add <url>":
                    pass
                if url == "#showlist":
                    print(f"Histórico de navegação: {hist}")

            if url[0] != "#":
                if len(hist) == 0 or url != p.topo():
                    p.empilhar(url)
                    hist.append(url)
                    print("Página encontrada")
                else:
                    print("Página atual.")

                    

                
        if url not in endereços:
            if url[0]== "#":
                print("Comando inválido")
            else:
                print("Endereço não encontrado")
        print(p.imprimir())
        try:
            print(p.topo())
        except PilhaException as pe:
            print(pe)
        

    print("Operação finalizada!")'''