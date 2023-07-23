#Como pode ver eu usei um return no arquivo "02.FunçãoExemplo", ele literalmente serve para RETORNAR algo;

#Exemplo:
def projecaovendasmes(diasmes, diastrabalhados,vendidototal):
    calculo1 = vendidototal / diastrabalhados * diasmes
    exato = round(calculo1)
    return exato #Aqui a função irá fazer todo o calculo mas irá retornar apenas o valor da variável exato
    

a = int(input("Quantos dias tem no mês?"))
b = int(input("Já se passaram quantos dias?"))
c = float(input("Quanto você já vendeu?"))
print(f"A sua projeção de vendas daqui pro fim do mês é de: {projecaovendasmes(a,b,c)}.")