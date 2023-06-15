# Variáveis são espaços que alocamos na memória ram temporariamente;
# No Python não temos a exigência de tipar para guardar algum dado, elas são tipadas dinamicamente;

# Aqui irei declarar algumas variáveis e também irei exprimir elas de formas distintas (apenas print e usando %s)

variavel1 = "Python não é KamelKaze, logo não precisa letras Maiúsculas"
print(variavel1)

variavel_2 = "A forma mais prática de fazer separações no corpo da variável é usando underline"
print(variavel_2)

variavel_3 = 7.4
variavel_4 = "Podemos colocar valores números, separados por ponto tranquilamente"
print(variavel_3, variavel_4)

variavel_5 = 7, 5
variavel_6 = "mas é bom ressaltar que quando usamos virgula o valor irá ser expresso dentro de parênteses pois a linguagem entende que são dados separados"
print(variavel_5, variavel_6)

variavel_7 = 10
# alternativa ao clássico print + Texto direto
print("Minha meta é %s, 9,5 nem rola" % (variavel_7))

variavel_8 = True

if variavel_8 == False:
    print("Não irá mostrar")
else:
    print("Aqui, assim como na maioria absoluta das linguagens, podemos ter dados do tipo booleano")

print("---------- Tipos de todas as variáveis usadas até aqui --------------------------")
print(type(variavel1))
print(type(variavel_2))
print(type(variavel_3))
print(type(variavel_4))
print(type(variavel_5))
print(type(variavel_6))
print(type(variavel_7))
print(type(variavel_8))

#obs: Python permite que usemos apenas o print, mas temos escolha de usar o fantes do texto com variável no meio;
#separada por {} e também com a função format(); 