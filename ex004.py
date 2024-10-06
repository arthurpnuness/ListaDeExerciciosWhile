'''Faça um algoritmo onde uma variável que contenha um número definido por você entre 1 e 100. Posteriormente solicite ao usuário números entre 1 e 100 (um número por vez) até que usuário acerte o número na variável inicial. Se o usuário digitar um valor menor que valor apresente: “Tente um número maior” e se o usuário digitar um valor maior que o valor apresente: “Tente um valor menor”. Quando o usuário acertar o número apresente: “Parabéns!”.'''

numero = 98

while True:

    num = int(input('Digite um numero inteiro positivo de 1 a 100: '))

    if num <= 0:
        print('Digite um numero maior que zero')
    elif num < 98:
        print('Tente um numero maior')
    elif num > 98:
        print('Tente um numero menor')
    else:
        print('Parabens!!!')
        break




    