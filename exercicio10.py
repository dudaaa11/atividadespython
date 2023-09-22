#3! = 3.2.1 = 6

# exercicio a

def fatorial (i : int):
    if (i == 1):return 1
    else:
        return i * fatorial (i-1)
    
print (fatorial(3))
print (fatorial(5))
print (fatorial(7))

#exercicio b
from time import sleep
print ("CONTAGEM REGRESSIVA: end=")
for c in range(10,0, -1):
    print(c, end='', flush=True)
    sleep(1)
    print("lindas")

#exercicio c
def inverter_string(string):
    return string[::-1]

try:
    entrada = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(entrada)
    print(f"A string invertida é: {string_invertida}")
except:
    print("Ocorreu um erro :(")