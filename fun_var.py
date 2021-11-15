from pilha import *

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        return arquivo.readlines()


#Essas variáveis estão nessa parte do codigo devido ao fato da impossibilidade de importação de
#         
sair = ["pode entrar"]  
p = PilhaEncadeada()
endereços = []
hist = []
for linha in ler_arquivo("trabalho/endereços.txt"):
    linha = linha.strip()
    if '/' in linha:
        linha = linha.split('/')    
        endereços.append(linha)
    else:
        endereços.append(linha)