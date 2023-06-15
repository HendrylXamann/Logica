#Segue uma demonstração básica de operações aritméticas no python visando demonstrar meus conhecimentos no tema;

#Soma
#Versão extensa/arcaica
v1 = 7
v2 = 4
soma = v1+v2
print(soma)
#Versão otimizada/prática
v1, v2 = 7,4
print(v1 + v2)

#Subtração
#Versão extensa/arcaica
v11 = 7
v22 = 4
sub = v11-v22
print(sub)
#Versão otimizada/prática
v11, v22 = 7,4
print(v11 - v22)

#Multiplicação
#Versão extensa/arcaica
v111 = 7
v222 = 4
mult = v111 * v222
print(mult)
#Versão otimizada/prática
v111, v222 = 7,4
print(v111 * v222)

#Divisão
#Divisão inteira
#Versão extensa/arcaica
di1 = 27
di2 = 2
divi = di1 // di2
print(divi)
#Versão otimizada/prática
di1, di2  = 27, 2
print(di1 // di2)
#Divisão real
#Versão extensa/arcaica
di1 = 27
di2 = 2
divi = di1 / di2
print(divi)
#Versão otimizada/prática
di1, di2  = 27, 2
print(di1 / di2)

#Resto de divisão
#Versão extensa/arcaica
di1 = 27
di2 = 2
divi = di1 % di2
print(divi)
#Versão otimizada/prática
di1, di2  = 27, 2
print(di1 % di2)

#Potenciação/Exponenciação
#Versão 1 extensa/arcaica
exp = 36
exp2 = 27
result = exp ** exp2
print(result)
#Versão 2 extensa/arcaica
exp = 36
exp2 = 27
print(pow(exp,exp2))
#Versão otimizada/prática
exp, exp2 = 36,27
print(pow(exp,exp2))

#Lembrando que python respeita as ordens de precedência (Parenteses e/ou chaves, colchetes, multiplicação e/ ou divisão, adição e/ou subtração;
#Mas vale ressaltar que {} e [] tem outras finalidades dentro da linguagem, então se a equação tiver esses itens é preciso substituir por ()
#forma manual:
print("A resposta para a equação ((2 + 3) * [4 - {6 / 2}]) é")
d1 = 2 + 3
d2 = 6 // 2 
d3 = 4 - d2
d4 = 5 * d3
print(d4)
#Forma automatica:
print("A resposta para a equação ((2 + 3) * [4 - {6 / 2}]) é")
d11 = ((2 + 3) * (4 - (6 / 2)))
print(d11)
