'''Programa que calcula a base elevada ao expoente sem usar a função de potência'''

# Solicita ao usuário que insira os valores da base e do expoente
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Inicializa o resultado como 1 (qualquer número elevado a 0 é 1)
resultado = 1

# Usa um laço para multiplicar a base por ela mesma 'expoente' vezes
for i in range(expoente):
    resultado *= base

# Exibe o resultado da potenciação
print(f"{base} elevado a {expoente} é {resultado}")
