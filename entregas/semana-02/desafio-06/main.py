qtdatotal = 0
subtotalgeral = 0
descontogeral = 0
totalgeral = 0
qtdadevendas = 0
mtotal = 0
movimento = " "

def exibir_resumo_venda(p_nome, p_preco, p_quantidade, p_subtotal, p_porcentagem, p_desconto, p_total):
    print(" ")
    print("--- RESUMO DA VENDA ---")
    print(f"Produto: {p_nome}")
    print(f"Preço unitário: R$ {p_preco:.2f}")
    print(f"Quantidade vendida: {p_quantidade}")
    print(f"Subtotal da venda: R$ {p_subtotal:.2f}")
    print(f"Percentual de desconto aplicado: {p_porcentagem*100:.0f}%")
    print(f"Desconto aplicado: R$ {p_desconto:.2f}")
    print(f"Total da venda com desconto: R$ {p_total:.2f}")

def exibir_fechamento(p_qtdadevendas, p_qtdatotal, p_subtotalgeral, p_descontogeral, p_totalgeral, p_movimento, p_mtotal, p_ticketmedio):
    print(" ")
    print(f"Quantidade total de vendas realizadas: {p_qtdadevendas}")
    print(f"Quantidade total de produtos vendidos: {p_qtdatotal}")
    print(f"Subtotal geral das vendas: R$ {p_subtotalgeral:.2f}")
    print(f"Desconto geral aplicado: R$ {p_descontogeral:.2f}")
    print(f"Total geral das vendas com desconto: R$ {p_totalgeral:.2f}")
    print(f"Movimento de caixa da empresa: {p_movimento}")
    print(f"Maior valor de venda com desconto: R$ {p_mtotal:.2f}")
    print(f"Ticket médio das vendas: R$ {p_ticketmedio:.2f}")

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
        exibir_resumo_venda(nome, preco, quantidade, subtotal, porcentagem, desconto, total)

    elif subtotal < 500:
        porcentagem = 0.05
        desconto = subtotal * porcentagem
        total = subtotal - desconto
        exibir_resumo_venda(nome, preco, quantidade, subtotal, porcentagem, desconto, total)

    else:
        porcentagem = 0.10
        desconto = subtotal * porcentagem
        total = subtotal - desconto
        exibir_resumo_venda(nome, preco, quantidade, subtotal, porcentagem, desconto, total)

    if mtotal < total:
        mtotal = total

    qtdatotal = qtdatotal + quantidade
    subtotalgeral = subtotalgeral + subtotal
    descontogeral = descontogeral + desconto
    totalgeral = totalgeral + total
    qtdadevendas = qtdadevendas + 1
    ticketmedio = totalgeral / qtdadevendas

    if totalgeral < 500:
        movimento = "Movimento baixo"
    elif totalgeral < 1500:
        movimento = "Movimento moderado"
    else:
        movimento = "Movimento alto"

    print(" ")
    continuar = input("Deseja realizar outra venda? (s/n): ")
    if continuar.lower() != 's':
        exibir_fechamento(qtdadevendas, qtdatotal, subtotalgeral, descontogeral, totalgeral, movimento, mtotal, ticketmedio)
        break