# Ler em reais e transformar em dólares
d1 = float(input("Quantos reais deseja converter? R$"))
dolar = d1 / 5.52 #cotação 18/12/25
euro = d1 / 6.27
iene = d1 / 0.034
print(f"Você possui {d1} reais e pode comprar {dolar:.2f} dólares; {euro:.2f} euros; {iene:.2f} ienes.")