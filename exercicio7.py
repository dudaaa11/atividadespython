#criem um sistema, que receba uma quantidade indefinida de produtos, quantidades de estoque desses produtos, e preços desses produtos...
#e então, grave todos eles em um arquivo de texto....
produtos = []
preços = []
quantidadeEstoque = []

concluir = False

while (not concluir):
    print("digite o nome do produto: ")
    nomeProdutos = input()
    print("digite o valor do produto: ")
    nomePreços = int(input())
    print("digite a quantidade no estoque: ")
    nomeQuantidadeestoque = int(input())

    produtos.append(nomeProdutos)
    preços.append(nomePreços)
    quantidadeEstoque.append(nomeQuantidadeestoque)

    print("deseja inserir outro produto?(s/n)")
    concluir = input() == "n"

print("seguem abaixo todos os produtos digitados:")
print("acessorios: preço [quantidadeEstoque]")
for i in range(len(produtos)):
    print(f"{produtos[i]} : {preços[i]} {[quantidadeEstoque[i]]}")

input("pressione Enter pra terminar...")

import os

names = [f"{produtos[i]} : {preços[i]} {[quantidadeEstoque[i]]}"]

filename = "produtos.txt"
file = open(filename, 'w')
for i in range(len(produtos)):
    outputline = f"produto;  {produtos[i]} : {preços[i]} : {quantidadeEstoque[i]}\n"
    file.write(outputline)

file.close()

os.system(f"notepad {filename}")