qtdatotal = 0
subtotalgeral = 0
descontogeral = 0
totalgeral = 0
qtdadevendas = 0

while True:    
    while True: # usando o while True para a verificar se o nome do produto é uma entrada valida 
        nome = input("Nome do produto: ")
        if nome.strip(): #função nativa do python que remove espações em brancos, então o teste funciona mesmo que o usuário digite apenas espaços em branco
            break
        print("Erro: o nome do produto não pode estar vazio.")
        print(" ")

    while True: # inicia o loop de teste do preço do produto, caso o usuário digite um valor inválido, o loop se repete até que seja digitado um valor válido
        try: #try e except são usados para tratar erros, nesse caso, caso o usuário digite um valor inválido, o programa não quebra e sim exibe uma mensagem de erro
            preco = float(input("Preço unitário: "))
            if preco <= 0:
                print("Erro: o preço deve ser maior que zero.")
                print(" ")

            else:
                break

        except ValueError:
            print("Erro: você precisa digitar um número válido.")
            print(" ") 

    while True: # inicia o loop de teste da quantidade do produto, caso o usuário digite um valor inválido, o loop se repete até que seja digitado um valor válido
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Erro: a quantidade deve ser maior que zero.")
                print(" ")
            else:
                break
        except ValueError:
            print("Erro: você precisa digitar um número inteiro válido.")
            print(" ")

    subtotal = preco * quantidade

    if subtotal < 100:
        porcentagem = 0
        desconto = subtotal * porcentagem
        total = subtotal - desconto
        print(" ")
        print("--- RESUMO DA VENDA ---")
        print(f"Produto: {nome}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Quantidade vendida: {quantidade}")
        print(f"Subtotal da venda: R$ {subtotal:.2f}")
        print(f"Percentual de desconto aplicado: 0%")
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total da venda com desconto: R$ {total:.2f}")

    elif subtotal < 500:
        porcentagem = 0.05
        desconto = subtotal * porcentagem
        total = subtotal - desconto
        print(" ")
        print("--- RESUMO DA VENDA ---")
        print(f"Produto: {nome}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Quantidade vendida: {quantidade}")
        print(f"Subtotal da venda: R$ {subtotal:.2f}")
        print(f"Percentual de desconto aplicado: 5%")
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total da venda com desconto: R$ {total:.2f}")

    else:
        porcentagem = 0.10
        desconto = subtotal * porcentagem
        total = subtotal - desconto
        print(" ")
        print("--- RESUMO DA VENDA ---")
        print(f"Produto: {nome}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Quantidade vendida: {quantidade}")
        print(f"Subtotal da venda: R$ {subtotal:.2f}")
        print(f"Percentual de desconto aplicado: 10%")
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total da venda com desconto: R$ {total:.2f}")


    qtdatotal = qtdatotal + quantidade
    subtotalgeral = subtotalgeral + subtotal
    descontogeral = descontogeral + desconto
    totalgeral = totalgeral + total
    qtdadevendas = qtdadevendas + 1

    print(f"DEBUG - Vendas contabilizadas: {qtdadevendas}")

    print(" ")
    continuar = input("Deseja realizar outra venda? (s/n): ")
    if continuar.lower() != 's':
        print(" ")
        print(f"Quantidade total de vendas realizadas: {qtdadevendas}")
        print(f"Quantidade total de produtos vendidos: {qtdatotal}")
        print(f"Subtotal geral das vendas: R$ {subtotalgeral:.2f}")
        print(f"Desconto geral aplicado: R$ {descontogeral:.2f}")
        print(f"Total geral das vendas com desconto: R$ {totalgeral:.2f}")
        break