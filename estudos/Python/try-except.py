while True: # usando o while True para a verificar se o nome do produto é uma entrada valida 
    nome = input("Nome do produto: ")
    if nome.strip(): #função nativa do python que remove espações em brancos, então o teste funciona mesmo que o usuário digite apenas espaços em branco
        break
    print("Erro: o nome do produto não pode estar vazio.")

while True: # inicia o loop de teste do preço do produto, caso o usuário digite um valor inválido, o loop se repete até que seja digitado um valor válido
    try: #try e except são usados para tratar erros, nesse caso, caso o usuário digite um valor inválido, o programa não quebra e sim exibe uma mensagem de erro
        preco = float(input("Preço unitário: "))
        if preco < 0:
            print("Erro: o preço não pode ser negativo.")

        else:
            break

    except ValueError:
        print("Erro: você precisa digitar um número válido.")    

while True: # inicia o loop de teste da quantidade do produto, caso o usuário digite um valor inválido, o loop se repete até que seja digitado um valor válido
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
        else:
            break
    except ValueError:
        print("Erro: você precisa digitar um número inteiro válido.")

total = preco * quantidade

print("--- RESUMO DA VENDA ---")
print(f"Produto: {nome}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade vendida: {quantidade}")
print(f"Total da venda: R$ {total:.2f}")