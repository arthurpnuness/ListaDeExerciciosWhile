
'''Faça um programa que verifica se um número fornecido pelo usuário é primo ou não. Obs. para um número ser primo ele deve ser divisível apenas por 1 e por ele mesmo.'''



while True:  # Laço infinito para garantir que o usuário digite um número válido
    numero = int(input('Digite um numero: '))  # Solicita ao usuário um número inteiro

    # Verifica se o número é menor ou igual a 1, pois não faz sentido verificar números <= 1 para primos
    if numero <= 1:
        print('Não é possivel calcular se é primo ou não.')  # Mensagem de erro para números <= 1
    else: 
        break  # Sai do laço quando um número maior que 1 for digitado

# Verifica se o número é 2, que é o único número primo par
if numero == 2:
    print('É primo')
else:
    divisor = 2  # Inicializa o divisor como 2
    naoehprimo = 0  # Variável para indicar se o número não é primo, inicialmente 0 (assumimos que é primo)
    
    # Enquanto o divisor for menor ou igual a metade do número (otimização para evitar divisões desnecessárias)
    while divisor <= ((numero + 1) / 2):
        # Verifica se o número é divisível pelo divisor (não é primo se for divisível)
        if numero % divisor == 0:
            naoehprimo = 1  # Marca como não primo
            break  # Sai do laço se encontrar um divisor
        divisor += 1  # Incrementa o divisor para testar o próximo número
    
    # Se 'naoehprimo' ainda for 0, significa que nenhum divisor foi encontrado
    if naoehprimo == 0:
        print(f'O numero {numero} é primo')  # Confirma que o número é primo
    else:
        print(f'O numero {numero} nao é primo')  # Caso contrário, o número não é primo



