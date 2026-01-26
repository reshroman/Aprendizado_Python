# Ler se o nome da cidade possui "SANTO"

cidade = str(input('Digite o nome da sua cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')