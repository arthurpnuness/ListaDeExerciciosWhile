'''Caixa registradora rudimentar para uma loja de conveniências'''

while True:
    total = 0
    contador = 1

    print("Lojas Tabajara")

    # Laço para registrar os produtos
    while True:
        preco = float(input(f"Produto {contador}: R$ "))
        if preco == 0:  # Finaliza a compra quando o valor inserido for 0
            break
        total += preco
        contador += 1

    # Exibe o total da compra
    print(f"Total: R$ {total:.2f}")

    # Solicita o valor em dinheiro e calcula o troco
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total
    print(f"Troco: R$ {troco:.2f}")

    # Pergunta se deseja registrar outra compra
    resposta = input("Deseja registrar outra compra? (s/n): ").lower()
    if resposta == 'n':
        break
