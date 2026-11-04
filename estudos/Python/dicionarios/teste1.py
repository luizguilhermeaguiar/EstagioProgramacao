nome = input("digite um nome: ")
preco = input("Digite o preçodo produto: ")
quantidade = input("Digite a quantidade: ")

produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

print(produto["nome"])       # Teclado
print(produto["preco"])      # 150.0
print(produto["quantidade"]) # 2