'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

# Definindo as populações iniciais dos países
populacaoA = 80000  # População inicial do país A
populacaoB = 200000  # População inicial do país B

# Definindo as taxas de crescimento anuais (em forma decimal)
taxa_crescimento_a = 0.03  # Taxa de crescimento de 3% para o país A
taxa_crescimento_b = 0.015  # Taxa de crescimento de 1,5% para o país B

anos = 0  # Inicializa o contador de anos

# Enquanto a população do país A for menor que a do país B
while populacaoA < populacaoB:
    # A cada ano, a população aumenta de acordo com suas respectivas taxas de crescimento
    populacaoA += populacaoA * taxa_crescimento_a  # Atualiza a população de A
    populacaoB += populacaoB * taxa_crescimento_b  # Atualiza a população de B
    anos += 1  # Incrementa o contador de anos

# Exibe o número de anos necessários para a população de A ultrapassar ou igualar a de B
print(f'Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.')

