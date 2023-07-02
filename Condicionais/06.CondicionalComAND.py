#Segue exemplo, simples e prático, de condicional a fim de demonstrar meus conhecimentos no tema:

# Condicional com AND 1:
var1 = int(input("digite um valor maior que zero e menor que 3:"))
if var1 > 0 and var1 < 3:
    print("o valor digitado foi", var1, "e está dentro do solicitado.")
else:
    print("Valor inválido, releia a solicitação.")

# Condicional com AND 2:
print("Levantamento de motoqueiros:")
var1 = input("Qual a cilindrada da sua moto?")
var1 = int(var1)
var2 = input("Pilota há quantos anos?")
var2 = int(var2)

if var1 >= 500 and var2 >= 2:
    print("Você é motoqueiro, parabéns, recomendo procurar um MC.")
else:
    print("Você é apenas um aspirante a piloto, lhe falta brio querido(a)")