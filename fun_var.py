from pilha import *


#Função utilizada para leitura de arquivo .txt
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        return arquivo.readlines()


#Variáveis realocadas devido ao fato da impossibilidade de importação mutua entre os arquivos.
sair = ["pode entrar"]  
p = PilhaEncadeada()
endereços = []
hist = []

#Varredura do arquivo .txt para adicionar à variável "endereços"
for linha in ler_arquivo("endereços.txt"):
    linha = linha.strip()
    if '/' in linha:
        linha = linha.split('/')    
        endereços.append(linha)
    else:
        endereços.append(linha)