alunos = []
notas = []

#essa é a variavel de controe do laço de repetição 
# se esse valor for alterado
#  o código a partir da linha 9até a linha 23
#não sera exercutado
concluir = False

while (not concluir):
    #solicitando que digite o nome do aluno 
    print("digite o nome  do aluno:")
    nomeAluno = input()

    #solicitando que digite a nota do aluno
    print("digite a nota do aluno")
    notaAluno =  int(input())

    if(notaAluno < 5): print("misericórdia")
    elif(notaAluno < 7): print("tá quase")
    else: print("passouuuuu")

    alunos.append(nomeAluno)
    notas.append(notaAluno)

    print("deseja inserir outra nota?(s/n)")
    concluir = input() == "n"

print("segue abaixo todas as notas digitadas:")
print("aluno : nota")
for i in range(len(alunos)):
    print(f"{alunos[i]} : {notas[i]}")

input("pressione enter pra terminar...")