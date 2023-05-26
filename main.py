'''lista = [tempo desde o semeio, umidade solo, escola que cuida]'''
alface = [31, 80]
batata = [91, 70]
cebolinha = [70, 60]
cenoura = [110, 60]
tomatinho = [70, 70]

alfacepramos = [25, 80, "Escola Cidade de anjos"]
batatapramos = [91, 70, "Escola Cidade de anjos"]
cenourapramos = [100, 50, "Escola Cidade de anjos"]

cenourapsonhos = [110, 60, "Escola Nova Era"]
cebolinhapsonhos = [50, 30, "Escola Nova Era"]
alfacepsonhos = [31, 80, "Escola Nova Era"]

tomatinhopgomez = [40, 70, "Escola Estrela Guia"]
alfacepgomez = [5, 35, "Escola Estrela Guia"]
batatapgomez = [6, 80, "Escola Estrela Guia"]
'''funções'''
def check_produto(listaP,listaA):
    if listaP[0] < listaA[0]:
        print(f"O alimento não esta pronto, faltam {listaA[1]-listaP[1]} dias para a proxima colheita")
    else:
        print("Produto esta pronto")
    return


print(check_produto(alfacepgomez,alface))