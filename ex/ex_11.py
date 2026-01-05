# Altura e Largura da parede, área e tinta para pintar
altura = float(input("Qual a altura de sua parede? "))
largura = float(input("Qual a largura de sua parede? "))
area = altura * largura
litros = area / 2 # Cada litro cobre 2m²
print("A área da sua parede é de {}m² e os litros de tinta necessários para pintá-la é de {}l".format(area, litros))