#1 - Variáveis de escopo global são aquelas que estando definida 1 vez e pode ser utilizada tanto dentro como fora da mesma, ou seja:

def exemplo(a):
    print(f'Aqui dentro não tem variável b, mas lá fora tem e seu valor é {b}')

b = 1
exemplo(b)

print("-"*10)

#2 - Variáveis com valores diferentes irão depender do seu escopo para ter seu valor expresso, exemplo:

def exemplo2():
    aa = 7
    print(f'Dentro da função aa vale {aa}')

aa = 4
exemplo2()
print(f"Fora da função aa vale {aa}")

print("-"*10)
#3 - Comando global, esse comando anula o item anterior. Quando colocamos ele independente do que seja inserido depois não será levado em consideração e o 
#python só vai valorizar a global. Exemplo:

def exemplo3(h):
    global c
    c = 9
    print(f'Dentro da função aa vale {c}')

c = 3
exemplo3(c)
print(f"Fora da função aa vale {c}")
#Logo, o valor de C=3 não vai ser expresso pois usamos global c dentro da função e o valor sempre será 9 para c. 