#Segue uma demonstração básica de operações aritméticas no python visando demonstrar meus conhecimentos no tema;
#O python respeita as ordens de precedência (Parenteses e/ou chaves, colchetes, multiplicação e/ ou divisão, adição e/ou subtração;
#Mas vale ressaltar que {} e [] tem outras finalidades dentro da linguagem, então se a equação tiver esses itens é preciso substituir por ()
#Forma manual:
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