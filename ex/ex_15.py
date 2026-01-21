# Calcular preço de diária e km de um carro alugado
vlr_diaria = 60
vlr_km = 0.15
dias = int(input("Durante quantos dias o carro foi utilizado? "))
km = float(input("Quantos KM foram percorridos? "))
total_diaria = dias * vlr_diaria
total_km = km * vlr_km
total = total_diaria + total_km
print(f" O valor total será de R${total:.2f}, sendo R${total_diaria:.2f} o valor da diária e {total_km:.2f} o valor pelos KM percorridos.")

# pago = ( dias * 60 ) + (km * 0.15)