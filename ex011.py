'''Programa que lê a idade de 25 alunos e mostra a maior, menor e a média das idades'''

# Inicializa variáveis
somaIdades = 0
maiorIdade = 0
menorIdade = 150  # Um valor suficientemente grande para comparar com as idades reais

# Solicita a idade de 25 alunos
for i in range(25):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    somaIdades += idade  # Acumula a soma das idades

    # Verifica se é a maior idade
    if idade > maiorIdade:
        maiorIdade = idade

    # Verifica se é a menor idade
    if idade < menorIdade:
        menorIdade = idade

# Calcula a média
mediaIdade = somaIdades / 25

# Exibe os resultados
print(f"A maior idade é: {maiorIdade}")
print(f"A menor idade é: {menorIdade}")
print(f"A média das idades é: {mediaIdade:.2f}")
