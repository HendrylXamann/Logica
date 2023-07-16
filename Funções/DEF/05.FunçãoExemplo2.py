#Aqui é outro trecho de código que trata de função utilizando método replace para servir de exemplo;

#Trocar palavra júnior por uma referência de The Big Bang theory:
def trocap():
    string = "Vaga Desenvolvedor Júnior - Requisitos 15 anos de experiência + Mestrado em Paologia Clínica"
    string = string.replace("Júnior", "I'm not crazy. My mother had me tested." )
    print(string)

trocap()
