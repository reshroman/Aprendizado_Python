# Ler nome e diga se tem SILVA

name = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem Silva? {'silva' in name.lower()}')