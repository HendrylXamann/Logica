#Segue exemplo, simples e prático, de condicional a fim de demonstrar meus conhecimentos no tema:

# Condicional com OR
orcamento = float(input("Quanto, em reais, você tem disponívél para comprar um novo veículo(digite apenas números)?"))
classes = input("Seu papai é rico e te ama?")

if orcamento >= 14000 or classes.lower() == "sim":
    print("Que bom, você terá um veículo!")
else:
    print("É filho(a), você tem que estudar e trabalhar um pouco mais para ter um veículo.")