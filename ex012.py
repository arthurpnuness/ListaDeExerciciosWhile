'''Programa que calcula o fatorial de um número'''

# Solicita um número do usuário
numero = int(input("Digite um número: "))

# Inicializa a variável fatorial com 1
fatorial = 1

# Calcula o fatorial utilizando um laço for
for i in range(1, numero + 1):
    fatorial *= i  # Multiplica a variável fatorial pelos números até 'numero'

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}")
