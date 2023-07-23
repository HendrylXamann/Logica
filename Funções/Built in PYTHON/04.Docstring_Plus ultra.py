#Uma docstring serve para criar uma pequena documentação/manual de uma função;
#Primeiro precisamos criar ela, é só colocar aspas duplas 3 vezes abaixo do def e na última linha da função;
#Em seguida descrevo exatamente o que cada elemento faz;
#Quando eu ou outra pessoa quiser verificar o manual dessa função vai ser só usar o help(nome da função);

#Ex:
def soma(a,b):
    """
    parâmetro a: recebe valor inserido por quem evoca a função
    parâmetro b: recebe valor inserido por quem evoca a função
    return: retorna a funcionalidade da função que é uma soma
    """
    soma = a + b
    return soma
    
help(soma)