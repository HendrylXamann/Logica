
# Aqui é um trecho de código que envolve o variáveis do tipo 
#string, float, int, booleano e também tupla (além de também ter uma condicional);

#Parte 1, usada no arquivo VariavelWithPython00:
variavel1 = "Python não é KamelKaze, logo não precisa letras Maiúsculas."
print(variavel1)

variavel_2 = "A forma mais prática de fazer separações no corpo da variável é usando underline.\n"
print(variavel_2)

variavel_3 = "Podemos colocar valores numéricos separados por ponto tranquilamente:"
variavel_4 = 7.4 
print(variavel_3, variavel_4)

variavel_5 = "\nmas é bom ressaltar que quando usamos virgula o valor irá ser expresso dentro de parênteses pois a linguagem entende que são dados separados:"
variavel_6 = 7,4
print(variavel_5, variavel_6)

#Parte 2:
varjoker = "---------------------\n" 
print(varjoker)

variavel_7 = 10
print("\nMinha meta é %s, 9,5 nem rola" % (variavel_7)) # Saída de dados alternativa;

variavel_8 = True
if variavel_8 == False:
    print("Não irá mostrar")
else:
    print("Aqui, assim como na maioria absoluta das linguagens, podemos ter dados do tipo booleano")

print("\n---------- Tipos de todas as variáveis usadas até aqui --------------------------\n")
print(type(variavel1))
print(type(variavel_2))
print(type(variavel_3))
print(type(variavel_4))
print(type(variavel_5))
print(type(variavel_6))
print(type(variavel_7))
print(type(variavel_8))