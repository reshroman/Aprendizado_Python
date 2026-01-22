# Ler 4 nomes e colocar em ordem aleatoria para apresentação

from random import shuffle

nome1 = str(input("Digite o nome do primeiro aluno para sortear: "))
nome2 = str(input("Digite o nome do segundo aluno para sortear: "))
nome3 = str(input("Digite o nome do terceiro aluno para sortear: "))
nome4 = str(input("Digite o nome do quarto aluno para sortear: "))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print("A ordem para apresentação será:")
print(lista)