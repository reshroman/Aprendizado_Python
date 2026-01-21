# Ler um ãngulo e mostrar o seno, cosseno e tangente

from math import radians, sin, cos, tan

a = float(input("Digite o ângulo para calcular o seno, cosse e tangente: "))
seno = sin(radians(a))
print(f"O ãngulo de {a} tem o SENO de {seno:.2f}")
cosseno = cos(radians(a))
print(f"O ângulo de {a} tem o COSSENO de {cosseno:.2f}")
tangente = tan(radians(a))
print(f"O ângulo de {a} tem a TANGENTE de {tangente:.2f}")