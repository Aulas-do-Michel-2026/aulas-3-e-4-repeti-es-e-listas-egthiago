"""
#### Exercício 1

Receba um número e calcule a soma de todos os números de 1 até ele.

Exemplo:

Digite um número:
5

A soma de 1 até 5 é 15.
--------
Digite um número:
3

A soma de 1 até 3 é 6.

Dica: Use o comando "for" junto com "range()" para percorrer os números,
e uma variável para ir acumulando a soma.
"""

numero = int(input('Digite um número: '))

soma = 0

for i in range(1, numero + 1):
    soma += i

print(f'A soma de 1 até {numero} é {soma}')
