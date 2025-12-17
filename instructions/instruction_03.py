# 5+2 # + Adição
# 5-2 # - Subtração
# 5*2 # * Multiplicação
# 5/2 # / Divisão
# 5**2 # ** Potência ( ao quadrado / ao cubo )
# 5//2 # // Divisão inteira
# 5%2 # % Resto da Divisão ( Módulo )

## Ordem de precedência ##
# () - Parentêses
# ** - Potência
#  * / // %
# + -

# Função da Potência - pow(x,x)
# Para fazer raiz quadrada - x**(1/2)
# Para fazer raiz cúbica - x**(1/3)

## Replicar informações ##
# print("=" * 5)
# nome = input("Qual o seu nome? ")
# print("Prazer em te conhecer {:>20}!".format(nome)) 
# Aplicar caracteres : e alinhamento > e centralizado ^
# {:=^x} para colocar o caractere nos espaços vazios

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("Seu resultado dos números somados é {}, multiplicados {} e divididos {:.3f}".format(s, m, d), end=" ") # :.3f para diminuir as casas
print("Em divisão inteira é {} e potência {}".format(di, e))