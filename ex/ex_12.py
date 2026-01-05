# Mostrar o preço com 5% de desconto
preco = float(input("Qual o valor que deseja saber o desconto? "))
desconto = 0.05
vlr_dc = preco * desconto
resultado = preco - vlr_dc

print("O desconto de 5% equivale a R${}, e o valor com desconto é de R${}.".format(vlr_dc, resultado))