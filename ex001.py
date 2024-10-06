''''Faça um algoritmo utilizando While para mostrar todos os valores pares entre 0 e 500.'''

numero = 0  # Inicializa a variável 'numero' com o valor 0

# Enquanto 'numero' for menor ou igual a 500, o laço será executado
while numero <= 500:  
    # Verifica se o número é par. Um número é par se o resto da divisão por 2 for igual a 0
    if numero % 2 == 0:
        print(numero)  # Se o número for par, ele será impresso na tela
    # Incrementa o valor de 'numero' em 1 após cada iteração
    numero += 1

