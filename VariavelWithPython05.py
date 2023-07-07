#Aqui é o último arquivo sobre variáveis, farei um exemplo de cada TIPO possível;
#Variáveis existem em todas as linguagens de programação, entendo a lógica e posso aplicar para toda e qualquer uma;
#Trabalhamos com acesso a internet e em contato com outros seres humanos, no século 21 ninguém é uma ilha, tudo se aprende;
#Logo, me dê a meta e um prazo que você terá seu resultado!

#Tipo texto (String):
me = "contrata"
por = 'favor'
print(type(me))
print(type(por))

#Tipo numérico (Int, Float e Complex):
MinhaMetaE = 10
nem_rola = 9.5
outravar = 3j #Lembrando que o j é padrão do python para representar o i da unidade imaginária
print(type(MinhaMetaE))
print(type(nem_rola))
print(type(outravar))

#Tipo sequencial (List, Tuple e Range):
lista = [3,2,1]
tupla = (1,5,7)
print(type(lista))
print(type(tupla))
#Range merece uma breve explicação além dos exemplos, ele serve para fazer uma sequencia ordenada de valores; 
for haha in range(3): #ele vai de 0 - índice inicial - até o 3 em uma sequencia ordenada
    print(haha)
range = range(5)
print(type(range))

#Tipo de mapeamento (Dict) / Dicionário:
Autores_e_uma_Obra = {"Kant" : "Fundamentação da metafísica dos costumes", "Platão" : "O Banquete"}
print(Autores_e_uma_Obra)
print(type(Autores_e_uma_Obra))

#Tipo de coleção (Set e Frozenset):
gostoDe = {"Harry Potter", "One Piece", "Programação"} #Set armazena um conjunto de elementos únicos, mas não tem uma ordem exclusiva
print(gostoDe) #Serve para várias coisas inclusive verificações de elementos, operações de conjunto(união, diferença e interseção)
print(type(gostoDe))
naoeconstant = frozenset({"Louco", "Né", "vei"}) #Enquanto no set posso adicionar ou remover elementos, no frozenset não, ele é uma
print(naoeconstant) #estrutura de dados imutável
print(type(naoeconstant))

# Tipo booleano (bool):
aA = 2
bB = 1
Cc = bB>=aA
print(Cc)
print(type(Cc)) 

#Tipo binário (Bytes, Bytearray e memoryview):
ff = b"espero usar isso um dia" #o B é um prefixo de bytes para deixer que a string deve ser tratada como uma sequência de bytes 
gg = bytearray(5) #uma sequencia mutável de bytes que é criada com zeros
jj = memoryview(bytes(5)) #Útil para uma enorme quantidade de dados, pois evita a necessidade de copiar os dados em outro objeto
print(ff,gg,jj)
print(type(ff))
print(type(gg))
print(type(jj))

#Tipo none:
simples = None
print(type(simples))
