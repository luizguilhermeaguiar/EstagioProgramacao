'''def exibir_resumo_venda():
    print(" ")
    print("--- RESUMO DA VENDA ---")
    print(f"Produto: {nome}")
    print(f"Preço unitário: R$ {preco:.2f}")
    print(f"Quantidade vendida: {quantidade}")
    print(f"Subtotal da venda: R$ {subtotal:.2f}")
    print(f"Percentual de desconto aplicado: 0%")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Total da venda com desconto: R$ {total:.2f}")'''

porcentagem = 0.10

n1 = int(input("digite um numero ")) 
n2 = int(input("digite outro"))

subtotal = n1 + n2

desconto = subtotal * porcentagem

total = subtotal - desconto

print(f"valor com desconto de 10%: {total}")

print(f"porcentagem: {porcentagem*100:.0f}")


