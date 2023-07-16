#Aqui é um trecho de código que trata de função para servir de exemplo;

#Formatar o texto em maiuscula e retirar espaços:
def ajustar_(argumento): #def é o comando para criar função, seguido do nome da mesma e entre os parenteses fica o argumento; 
    argumento = argumento.upper() #Upper transforma o texto todo em letra maiuscula;
    argumento = argumento.strip() #Strip tira todos os espaços que tiver no texto, antes e depois dele;
    return argumento #return é o que eu quero devolver, o que a função inteira da como resposta / Nesse caso ela ta me dando o texto ajustado; 

exemplo1 = "   EsTa frASE vAi Se AJUStar CoM a FunÇÃO"
usando_a_def = ajustar_(exemplo1)
print(usando_a_def)

exemplo2 = [" boston","Miami Heat", "LAKeRS", "CLeVELanD"]
for i, times in enumerate(exemplo2):
    exemplo2[i] = ajustar_(times)
print(exemplo2)