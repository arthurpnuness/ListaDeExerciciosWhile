'''Escreva um programa que calcula a soma de todos os números de 1 a N, onde N é um número inteiro fornecido pelo usuário.'''

# Solicita ao usuário que insira o valor de N
num = int(input('Digite um número inteiro positivo: '))

# Inicializa a variável que armazenará a soma
soma = 0

# Usa um laço for para somar todos os números de 1 até N
for numero in range(1, num + 1):
    soma += numero  # Adiciona o número atual à soma

# Exibe o resultado da soma
print(f'A soma de todos os números de 1 até {num} é {soma}.')
