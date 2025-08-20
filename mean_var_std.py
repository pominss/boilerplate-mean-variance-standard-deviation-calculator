import numpy as np

def calculate(lista):
    if len(lista) == 9:
        listanp = np.array(lista)
        matriz = listanp.reshape(3,3)
        media_x1 = np.mean(matriz, axis = 0).tolist()
        media_x2 = np.mean(matriz, axis = 1).tolist()
        media = np.mean(matriz).item()
        variante_x1 = np.var(matriz, axis = 0).tolist()
        variante_x2 = np.var(matriz, axis = 1).tolist()
        variante = np.var(matriz).item()
        desvio_padrao_x1 = np.std(matriz, axis = 0).tolist()
        desvio_padrao_x2 = np.std(matriz, axis = 1).tolist()
        desvio_padrao = np.std(matriz).item()
        maximo_x1 = np.max(matriz, axis = 0).tolist()
        maximo_x2 = np.max(matriz, axis = 1).tolist()
        maximo = np.max(matriz).item()
        minimo_x1 = np.min(matriz, axis = 0).tolist()
        minimo_x2 = np.min(matriz, axis = 1).tolist()
        minimo = np.min(matriz).item()
        soma_x1 = np.sum(matriz, axis = 0).tolist()
        soma_x2 = np.sum(matriz, axis = 1).tolist()
        soma = np.sum(matriz).item()
        calculations = { 
        'mean': [media_x1, media_x2, media],
        'variance': [variante_x1, variante_x2, variante],
        'standard deviation': [desvio_padrao_x1, desvio_padrao_x2, desvio_padrao],
        'max': [maximo_x1, maximo_x2, maximo],
        'min': [minimo_x1, minimo_x2, minimo],
        'sum': [soma_x1, soma_x2, soma]
        }
    else:
        raise ValueError("List must contain nine numbers.")


    return calculations