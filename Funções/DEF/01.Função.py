#Função com vários parâmetros são necessárias e seguem a mesma lógica, porém ela exige que seja inserida todos os valores a fim de ocupar 
#Todos os paramentros, ou seja, se eu colocar 3 parâmetros na função então tenho que dar 3 valores quando eu chamar ela;
#Função times de basquete (3 Parâmetros)
def timesNBA(top1,top2,top3):
    print(top1)
    print(top2)
    print(top3)
timesNBA('Boston','Cleveland','GSW') #Aqui só deu certo pq coloquei três valores, caso eu tivesse colocado apenas 2 ou só 1 teria dado erro;
print('--'*10)
#Função multiplicação (2 Parâmetros)
def multi(valor1,valor2):
    resultado = valor1 * valor2
    print(resultado)

multi(7,4)
print('--'*10)



