"""
#### Exercício 3 - Comparando listas.

Receba duas listas de input do usuário. Ele digitará como um texto com os números separados por vígula. 
Para isso, pode-se utilizar o código disponibilizado que vai transformar esse texto em lista para você.

Eu quero que você me diga qual das listas tem o maior número dentro delas. 

Se a primeira lista tiver o maior número, imprima: "Primeira".
Se a segunda lista tiver o maior número, imprima: "Segunda".
Se ambas tiverem o mesmo número como maior, digite: "Ambas".

Exemplos:

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 50, 2, 40
Digite a sua segunda lista (separando os números por vírgula): 0, 2, 99, 1, 1, 3

Resposta:
Segunda

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 0, 2, 30
Digite a sua segunda lista (separando os números por vírgula): 9, 9, 9, 30

Resposta:
Ambas
"""

# Código para pegar as listas de input
primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]

# Fazer a partir daqui

maior_primeira = 0
maior_segunda = 0

for i in range(0, len(primeira_lista)):
    if i == 0:
        maior_primeira = primeira_lista[0]
    else:
        if primeira_lista[i] > maior_primeira:
            maior_primeira = primeira_lista[i]

for i in range(0, len(segunda_lista)):
    if i == 0:
        maior_segunda = segunda_lista[0]
    else:
        if segunda_lista[i] > maior_segunda:
            maior_segunda = segunda_lista[i]

if maior_primeira > maior_segunda:
    print('Primeira lista')
if maior_segunda > maior_primeira:
    print('Segunda lista')
if maior_primeira == maior_segunda:
    print('Ambas')
