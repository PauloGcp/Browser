from pilha import *
#função utilizada para leitura de arquivo .txt

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        return arquivo.readlines()


#Essas variáveis estão nessa parte do codigo devido ao fato da impossibilidade de importação mutua entre os arquivos


sair = ["pode entrar"]  
p = PilhaEncadeada()
endereços = []
hist = []
for linha in ler_arquivo("endereços.txt"):
    linha = linha.strip()
    if '/' in linha:
        linha = linha.split('/')    
        endereços.append(linha)
    else:
        endereços.append(linha)