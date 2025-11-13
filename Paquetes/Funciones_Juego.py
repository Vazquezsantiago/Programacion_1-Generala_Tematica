import random
def jugar():
    pass
def tirar_dados():
    lista_dados=[]
    for i in range (5):
        lista_dados.append(random.randint(1, 6))
    print(lista_dados)
    return(lista_dados)


def guardar_dados(lista_dados):
    dados_mano=[]
    while len(dados_mano) <2:
        
        posicion=int(input("elija un dado a guardar(1-5 por su posicion)"))
        borrado = lista_dados[(posicion-1)]
        dados_mano.append(borrado)
        lista_dados.remove(borrado)    
        print(dados_mano)
        print(lista_dados)   
dados=tirar_dados()
guardar_dados(dados)
