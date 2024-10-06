''' Programa que calcula a média de idades de 15 pessoas e classifica como jovem, adulta ou idosa'''

# Inicializa variáveis
somaIdades = 0
quantidadePessoas = 15

# Solicita as idades para 15 pessoas
for i in range(quantidadePessoas):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    somaIdades += idade  # Acumula as idades

# Calcula a média
mediaIdade = somaIdades / quantidadePessoas

# Classifica a turma com base na média de idade
if 0 <= mediaIdade <= 25:
    print("A turma é jovem.")
elif 26 <= mediaIdade <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")
