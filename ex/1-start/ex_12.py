# Mostrar o preço com 5% de desconto
preco = float(input("Qual o valor que deseja saber o desconto? R$"))
desconto = 0.05
vlr_dc = preco * desconto
resultado = preco - vlr_dc

# cálculo para porcentagens = valor*porcentagem/100
# preco - (preco * 5 /100)

print(f"O desconto de 5% equivale a R${vlr_dc:.2f}, e o valor com desconto é de R${resultado:.2f}.")