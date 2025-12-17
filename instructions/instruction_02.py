nome = input ("Qual é o seu nome?")
print ("Olá," , nome, "seja bem-vindo ao freddy's pizza!")
idade = input ("Qual sua idade?")
print ("Nossa,", nome, "que legal, eu também tenho", idade, "anos!")
dia = input ("Que dia você nasceu?")
mes = input ("Em que mês você nasceu?")
ano = input ("E em que ano você nasceu?")
print ("Você nasceu no dia", dia, "de", mes, "de", ano, ".", "Correto?")
print ("Vamos fazer uma soma agora")
#int = numeros inteiros, sem virgula
#float = numeros com virgula
#bool = ( True ou False ) 
#str =  "texto" sempre em strings
numero1 = int(input ("Me diga um número:"))
numero2 = int(input ("Me diga outro número:"))
soma = numero1 + numero2
print ("Seu resultado é {}".format(soma))
#print ("Seu resultado é:", soma)