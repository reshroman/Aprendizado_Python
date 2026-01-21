# Ler comprimento dos catetos, e calcular a hipotenusa

from math import sqrt
co = float(input("Digite o comprimento do Cateto Oposto: "))
ca = float(input("Digite o comprimento do Cateto Adjacente: "))
hip = sqrt(co**2 + ca**2)
print(f"O valor da Hipotenusa é de {hip:.3f}")