'''Programa que monta uma tabela de preços para uma loja com produtos de R$ 1,99 (até 50 itens)'''

# Exibe a tabela de preços para 1 a 50 produtos
print("Lojas Quase Dois - Tabela de preços")
for quantidade in range(1, 51):
    preco = quantidade * 1.99  # Calcula o preço multiplicando a quantidade por 1,99
    print(f"{quantidade} produto(s) - R$ {preco:.2f}")
