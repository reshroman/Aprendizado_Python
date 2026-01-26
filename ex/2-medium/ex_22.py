# Complete name, upper, lower, lenght, letters in first name

name = str(input('Digite seu nome completo:')).strip()
print(f'Seu nome em maniúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')
print(f'Seu nome completo tem {len(name) - name.count(' ')} letras')
splitado = name.split()
print(f'Seu primeiro nome é {splitado[0]} e ele contém {len(splitado[0])} letras.')