#Uma função serve majoritariamente para fazer com que ganhemos tempo;
#Criamos uma função para reutilizar ela várias vezes no mesmo código ou em outros;

#Função simples começa com def + nome da variável seguido por parenteses e dois pontos;
def lembrete():
    print("Você será um grande desenvolvedor, continue sempre estudando") #Dentro da identação fica o conteúdo da função, seja ele qual for
#Em seguida só utilizar ela "evocando" pelo nome
lembrete()

#Função mais completa segue o mesmo norte da simples mas com inserção de parâmetros:
def withparametros(parametro):
    print(parametro)
    lembrete()

withparametros('Deu para entender como funciona uma função?') #Sempre que evocar uma função com parametros, digite o nome dela e dentro do paranteses
#você insere os dados e estes vão ser armazenados dentro do parâmetro; 

#Observação: Nem sempre o nome do paramtro será usado fora da função, perceba no último exemplo, eu criei a função mas na hora de evocar só utilzei o nome dela
#e dei o valor dela;

