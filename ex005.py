'''Faça um programa que leia e valide as seguintes informações.:
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Caso o usuário digite algo diferente das opções, o algoritmo deve solicitar novamente.
'''

while True:
    # Coletando e validando as informações
    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade > 150:
        print('Digite uma idade entre 0 e 150.')
        continue  # Volta ao início do laço para pedir os dados novamente

    salario = float(input('Digite seu salário: '))
    if salario <= 0:
        print('Digite um salário maior que zero.')
        continue

    sexo = input('Com qual gênero você se identifica? (F / M): ').upper()  # Corrigido .upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite um gênero válido (F/M).')
        continue

    estadoCivil = input('Qual é o seu estado civil (s, c, v, d): ').lower()  # Corrigido .lower()
    if estadoCivil not in ['s', 'c', 'v', 'd']:
        print('Digite um estado civil válido (s, c, v, d).')
        continue

    # Se todas as informações estiverem corretas, sair do laço
    print('Informações válidas inseridas com sucesso!')
    break
