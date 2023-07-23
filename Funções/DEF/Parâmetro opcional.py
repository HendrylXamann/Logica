#Parâmetro opcional é um valor pré definido que colocamos em um parâmetro na criação da função;
#Se quem evocar não colocar todos os devidos valores, esse parâmetro pré-definido irá aparecer;
#EX 1:
def timesNBA(a,b,c="Boston"):
    print(a,b,c)

timesNBA("Cleveland","Miami") #Foi inserido apenas 2 valores no parâmetro, mas como tem um pré definido a função vai ser executada sem problema;

#EX 2:
def media(a,b,c, d = 3):
    soma = a + b + c
    media = soma / d 
    return media
print(media(5,6,3)) #Foi inserido apenas 3 valores no parâmetro, mas como tem um pré definido a função vai ser executada sem problema;

#Obs: Posso por um valor pré denifido para todos os parâmetros e mesmo que a função seja chamada sem inserir nenhum valor irá funcionar tranquilamente;
