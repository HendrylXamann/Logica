#Dentro de uma função ou quando vamos evocar podemos estabelecer exatamente o valor dos parametros
#Função subtração 1
def subtracao(a,b):
    resultado = a / b
    print(int(resultado))

subtracao(b=2,a=6)#Independente da ordem que eu colocar dentro dos parâmetros ao evocar, a função vai seguir O SEU padrão de ordem de precedência

#Função subtração 2
def subtracao(a,b):
    resultado = a / b
    print(int(resultado))

subtracao(a=6,b=2)