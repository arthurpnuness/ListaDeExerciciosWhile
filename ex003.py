
numero = int(input('Digite um numero: '))

if numero <= 1:
    print('Não é possivel calcular se é primo ou não.')
elif numero == 2:
    print('É primo')
else:
    divisor = 2
    ehprimo = 0
    while divisor <= ((numero + 1) / 2):
        if numero % divisor == 0:
            naoehprimo = 1      
            break
        divisor += 1
    if naoehprimo == 0:
        print(f'O numero {numero} é primo')
    else:
        print('O numero nao é primo')
