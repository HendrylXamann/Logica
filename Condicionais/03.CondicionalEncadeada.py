#Segue exemplo, simples e prático, de condicional a fim de demonstrar meus conhecimentos no tema:

# Condicional encadeada (IF, ELIF E ELSE)
avaliar1 = input("Você já assistiu Shingeki no kyojin e/ou Mirai nikki?")
avaliar2 = input("E você gosta de anime?")

if avaliar1.lower() == "sim":
    print("Gostei de você")
elif avaliar2.lower() == "sim":
    print("Legal, recomendo assistir um desses 2 anteriores")
else:
    print("Moça(o), nem fala comigo não, por favor")