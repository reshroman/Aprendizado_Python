

n = str(input('Digite seu nome completo: ')).strip()
name = n.split()
print(f'Seu nome completo é {n}')
print(f'Seu primeiro nome é {name[0]}')
print(f'Seu último nome é {name[len(name) - 1]}')