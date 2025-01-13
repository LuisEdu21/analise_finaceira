import banco as bc

def run ():

    with open("config/configuracoes.txt", "r") as arquivo:
        resultado = arquivo.read()

    if resultado == 'N':
        bc.criar_tabelas()

    return