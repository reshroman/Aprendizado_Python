# Sortear um dos 4 alunos, ler os nomes e escrevendo o escolhido

import random

nome1 = str(input("Digite o nome do primeiro aluno para sortear: "))
nome2 = str(input("Digite o nome do segundo aluno para sortear: "))
nome3 = str(input("Digite o nome do terceiro aluno para sortear: "))
nome4 = str(input("Digite o nome do quarto aluno para sortear: "))

alunos = [nome1, nome2, nome3, nome4]

aluno_escolhido = random.choice(alunos)

print(f"O Aluno escolhido é {aluno_escolhido}")