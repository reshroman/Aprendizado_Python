

name = str(input('Digite uma frase: ')).strip().lower()
print(f'Na sua frase aparecem {name.count('a')} letras A')
print(f'A letra A aparece pela primeira vez na casa {name.find('a') + 1}')
print(f'A letra A aparece pela última vez na casa {name.rfind('a') + 1}')