# Ler 4 nomes e colocar em ordem aleatoria para apresentação

import random

nome1 = input("Digite o nome do primeiro aluno para sortear: ")
nome2 = input("Digite o nome do segundo aluno para sortear: ")
nome3 = input("Digite o nome do terceiro aluno para sortear: ")
nome4 = input("Digite o nome do quarto aluno para sortear: ")

alunos = [nome1, nome2, nome3, nome4]

aluno_escolhido1 = random.choice(alunos)
aluno_escolhido2 = random.choice(alunos)
aluno_escolhido3 = random.choice(alunos)
aluno_escolhido4 = random.choice(alunos)

print(f"A ordem para apresentação é {aluno_escolhido1}, {aluno_escolhido2}, {aluno_escolhido3}, {aluno_escolhido4}")