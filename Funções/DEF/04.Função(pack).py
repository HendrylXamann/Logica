#Dentro de função, no python, temos o empacotamento que é basicamente ler a quantidade de parametros que o usuario inserir
#Sem uma pré difinição
#Função avaliação
def mediafinal(*notas): #este asterisco serve para desempacotar, ele lê quantos parametros vão ser inseridos e joga dentro de um
    resultado = sum(notas) / len(notas)
    print(resultado)
mediafinal(4,9,7)
print('--'*10)

#Função contar dados (com tupla)
def descreva(*valor):
    tamanho = len(valor)
    print(f'Você inseriiu este(s) valores: {valor} e no total são {tamanho} números')
descreva(6,4,10)
print('--'*10)

#Função para ordenação (com lista)
def descreva2(*qtd):
    ordenacao = sorted(qtd) #sorted serve para ordenar listas, tuplas e conjuntos
    print('Você inseriu os valores assim:',qtd, "mas a ordem crescente é",ordenacao)

lista = [98, 4, 58, 1, 3, 68]
descreva2(*lista) #Usar o * para desempacotar a lista