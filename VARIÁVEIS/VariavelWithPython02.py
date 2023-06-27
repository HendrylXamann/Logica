#Aqui é um trecho de código que envolve o variáveis do tipo 
#string e int além de usar a função "len":
print('Iae')
print('Qual seu nome?') 
nome = str(input())
print('Satisfação Sr(a) ' + nome)
lenn = len(nome)
print('Você já reparou que eu nome tem ' + str(int(lenn)) + ' letras?')#STR(INT(LENN)) pois o python não concatena string com inteiro e vice versa, para fazer isso usamos essa "conversão"
#print(lenn)
print('Mas mudando de assunto, fala ae, qual sua idade?') 
idade = input()
print('Massa, ano que vem você terá ' + str(int(idade) + 1) + ' anos.')
