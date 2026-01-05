# Ler em reais e transformar em dólares
d1 = float(input("Quantos reais deseja converter? "))
conv = d1 * 5.52 #cotação 18/12/25
print("Você possui {} reais e pode comprar {:.2f} dólares.".format(d1, conv))