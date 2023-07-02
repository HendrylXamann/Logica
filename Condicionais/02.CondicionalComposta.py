#Segue exemplo, simples e prático, de condicional a fim de demonstrar meus conhecimentos no tema:

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
    print("Desculpe, você não tem idade para pilotar uma moto.")