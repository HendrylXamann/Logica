# Segue alguns exemplos, práticos, de condicionais com suas diferentes variações a fim de demonstrar meus;
#conhecimentos no tema:

# Condicional simples (1 IF)
print("A liberdade é uma útopia, mas andar de moto nos traz um vestígio do que poderia ser ela..")
question = str(input("você anda de moto?"))
if question.lower() == "sim":
    print("Boa, você sabe o que é viver!")

# Condicional composta (IF + else)
idade = int(input("Qual é a sua idade? "))
if idade >= 18:
    print("Você tem idade para pilotar uma moto, vá tirar CNH e ser feliz!")
else:
    print("Desculpe, você não tem idade para pilotar uma moto.")
# Condicional composta (IF DENTRO DE IF)
idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Você tem idade para pilotar uma moto!")
    moto_esportiva = input("Você tem uma moto esportiva? (sim/não) ")
    if moto_esportiva.lower() == "sim":
        print("Excelente, favor só andar acima de 90km/h!")
    else:
        print("Que pena, recomendo comprar uma ou uma custom!")
else:
    print("Desculpe, você não tem idade para pilotar uma moto esportiva.")

# Condicional encadeada (IF, ELIF E ELSE)
avaliar1 = input("Você já assistiu Shingeki no kyojin e/ou Mirai nikki?")
avaliar2 = input("E você gosta de anime?")

if avaliar1.lower() == "sim":
    print("Gostei de você")
elif avaliar2.lower() == "sim":
    print("Legal, recomendo assistir um desses 2 anteriores")
else:
    print("Moça(o), nem fala comigo não, por favor")

# Condicional com OR
orcamento = float(
    input("Quanto, em reais, você tem disponívél para comprar um novo veículo?"))
classes = input("Seu papai é rico e te ama?")
if orcamento >= 14.000 or classes.lower() == "sim":
    print("Que bom, você terá um veículo!")
else:
    print("É filho(a), você tem que estudar e trabalhar um pouco mais")


# Condicional com NOT
varia111 = float(
    input("Quanto é a diferença do dobro de quatro e o triplo de 1,5?"))
if not varia111 == 3.5:
    print("Pense mais um pouco. Dica: Lembre-se que em python usamos ponto ao invés de uma virgula")
else:
    print("Boa, ae sim")

# Condicional com AND 1:
var1 = int(input("digite um valor maior que zero e menor que 3:"))
if var1 > 0 and var1 < 3:
    print("o valor digitado foi", var1, "e está dentro do solicitado.")
else:
    print("Valor inválido, releia a solicitação.")

# Condicional com AND 2:
var1 = input("Qual a cilindrada da sua moto?")
var1 = int(var1)
var2 = input("Pilota há quantos anos?")
var2 = int(var2)

if var1 >= 500 and var2 >= 2:
    print("Você é motoqueiro, parabéns, recomendo procurar um MC.")
else:
    print("Você é apenas um aspirante à piloto, lhe falta brio querido(a)")
