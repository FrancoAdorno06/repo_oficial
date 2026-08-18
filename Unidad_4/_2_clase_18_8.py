# Declarar e Inicializar
# matriz = [
#     [1, 3, 2],
#     [3, 5, 1]
# ]
# matriz = []
# fila1 = [1, 3, 2]
# fila2 = [3, 5, 1, 5]
# matriz.append(fila1)
# matriz.append(fila2)
# print(matriz)

fila1 = [1, 3, 2]
# for i in range(len(fila1)):
#     print(fila1[i])
# for f in fila1:
#     print(f)
for i, f in enumerate(fila1):
    print(f"Indice: {i+1}: Valor: {f}")