# Programa para ler número e mostre sua porção inteira

from math import trunc
num = float(input("Digite um número para saber a sua porção inteira: "))
int = trunc(num)

print(f"O número {num} tem a parte inteira {int}")

# print(f"O valor digitado é {num} e sua porção inteira é {trunc(num)}")
