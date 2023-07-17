# Aqui está apenas um trecho de código para mostrar a ordem de precedência ao 'evocar' variáveis:

#Podemos dar outros valores a uma variável ao longo do código, ela não é uma constante
#Mas o python irá respeitar uma ordem de execução, o que eu mando executar primeiro acontece, no exemplo a seguir elucido essa ideia
#Aqui eu chamo a função_exemplo antes do print e ela irá printar o valor que está DENTRO da função para depois executar o resto
a = "Fora da função"

def funcao_exemplo():
  a = "Dentro da função"
  print("Este estava " + a)

funcao_exemplo()

print("Este estava " + a)

#Variável/ Palavra-chave Global é uma possibilidade, ela quando utilizada se torna um tipo de constante (está mais detalhado em escopo global -Dentro de funções)
#Lembrando que se as variáveis tiverem valores diferentes (global diferente da local) serão duas variáveis distintas:
x = "Boston deveria ter ganhado do miami nessa temporada de 2023"

def nba2023():
  global x
  x = "O Miami foi pra final só ser massacrado pelo joker"

nba2023()

print("Apenas uma revolta:" + x)

#Mas isso é anulado com o comando global que fixa o primeiro valor atribuido.
