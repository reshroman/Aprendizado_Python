# Fatiamento
# frase [9]
# frase [9:13] o último valor não entra na contagem
# frase [9:13:2] pulando 2
# frase [:5] do começo ao 5
# frase [15:] do 15 ao final
# frase [9::2] do 9 ao final pulando 3

# Análise
# len(frase) - comprimento da frase - lenght
# frase.count('o') - contar os caracteres (o)
# frase.count('o', 0, 13) - contar do 0 ao 13
# frase.find('deo') - indica onde começa
# frase.find('Android') - -1 (não existe na string)
# 'Curso' in frase

# Transformação
# frase.replace('Python', 'Android') - substituir Python por Android
# frase.upper() transformar em maiúsculo
# frase.lower() transformar em minúsculo
# frase.capitalize() deixar somente o primeiro caractere em maiúsculo
# frase.title() primeiro caractere de todas as palavras fica em maiúsculo
# frase.strip() remove todos os espaços do começo e final da str
# frase.rstrip() remove espaços da direita (final) da str
# frase.lstrip() remove espaços da esquerda (começo) da str

# Divisão
# frase.split() divide uma str em uma lista, onde cada elemento é separado (carácter padrão de split é o espaço)

# Junção
# '-'.join(frase) junta a str colocando - como espaçamento das palavras

frase = "Aprendizado Python"
print(frase[3:12])
print(frase[2:])
print(frase[1:12:2])
print(frase.upper())
print(frase.lower())
print(frase.strip())
print(frase.count('o'))
print(frase.upper().count('A'))
print(len(frase))
print(frase.find('ado'))
print(frase.replace('Aprendizado', 'Ensinamento'))
print('Python' in frase)
print(frase.find('Python'))
print(frase.lower().find('aprendizado'))
dividido = (frase.split())
print(dividido)
print(dividido[0])
print(dividido[1][3])