qtdatotal = 0
subtotalgeral = 0
descontogeral = 0
totalgeral = 0
qtdadevendas = 0
maiortotal = 0
movimento = " "

#exibe o resumo de cada venda 
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

#exibe o fechamento de caixa ao finalizar o programa
def exibir_fechamento(p_qtdadevendas, p_qtdatotal, p_subtotalgeral, p_descontogeral, p_totalgeral, p_movimento, p_maiortotal, p_ticketmedio):
    print(" ")
    print(f"Quantidade total de vendas realizadas: {p_qtdadevendas}")
    print(f"Quantidade total de produtos vendidos: {p_qtdatotal}")
    print(f"Subtotal geral das vendas: R$ {p_subtotalgeral:.2f}")
    print(f"Desconto geral aplicado: R$ {p_descontogeral:.2f}")
    print(f"Total geral das vendas com desconto: R$ {p_totalgeral:.2f}")
    print(f"Movimento de caixa da empresa: {p_movimento}")
    print(f"Maior valor de venda com desconto: R$ {p_maiortotal:.2f}")
    print(f"Ticket médio das vendas: R$ {p_ticketmedio:.2f}")

#função responsavel por decidir e retornar o parcentual que sera usado para o desconto
def calcular_desconto(p_subtotal):
    if p_subtotal < 100:
        return 0
        
    elif p_subtotal < 500:
        return 0.05

    else:
        return 0.10

#Responsavel por validar a entrada do nome
def solicitar_nome():
    while True: # usando o while True para a verificar se o nome do produto é uma entrada valida 
        nome = input("Nome do produto: ")#Variavel local da função 
        if nome.strip(): #função nativa do python que remove espações em brancos, então o teste funciona mesmo que o usuário digite apenas espaços em branco
            return nome
        print("Erro: o nome do produto não pode estar vazio.")
        print(" ")

#Responsavel por validar a entrada do preço
def solicitar_preco():
    while True: # inicia o loop de teste do preço do produto, caso o usuário digite um valor inválido, o loop se repete até que seja digitado um valor válido
        try: #try e except são usados para tratar erros, nesse caso, caso o usuário digite um valor inválido, o programa não quebra e sim exibe uma mensagem de erro
            preco = float(input("Preço unitário: "))
            if preco <= 0:
                print("Erro: o preço deve ser maior que zero.")
                print(" ")

            else:
                return preco

        except ValueError:
            print("Erro: você precisa digitar um número válido.")
            print(" ") 

#Responsavel por validar a entrada da quantidade
def solicitar_quantidade():
    while True: # inicia o loop de teste da quantidade do produto, caso o usuário digite um valor inválido, o loop se repete até que seja digitado um valor válido
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Erro: a quantidade deve ser maior que zero.")
                print(" ")
            else:
                return quantidade
        except ValueError:
            print("Erro: você precisa digitar um número inteiro válido.")
            print(" ")

#Todo o calculo da venda esta nessa função, de uma unica venda, para mais de uma venda ainda é no while principal
def realizar_venda():
    nome = solicitar_nome() #Chama a função de validação do nome 
    preco = solicitar_preco()#Chama a função de validação do preço
    quantidade = solicitar_quantidade()#Chama a função de validação da quantidade

    subtotal = preco * quantidade 
    porcentagem = calcular_desconto(subtotal)

    desconto = subtotal * porcentagem
    total = subtotal - desconto

    exibir_resumo_venda(nome, preco, quantidade, subtotal, porcentagem, desconto, total)

    return quantidade, subtotal, desconto, total

def classificar_movimento(p_totalgeral):
    if p_totalgeral < 500:
        return "Movimento baixo"
    elif p_totalgeral < 1500:
        return "Movimento moderado"
    else:
        return "Movimento alto"

while True:    
    quantidade, subtotal, desconto, total = realizar_venda() 

    if maiortotal < total:
        maiortotal = total

    qtdatotal = qtdatotal + quantidade
    subtotalgeral = subtotalgeral + subtotal
    descontogeral = descontogeral + desconto
    totalgeral = totalgeral + total
    qtdadevendas = qtdadevendas + 1

    movimento = classificar_movimento(totalgeral)

    print(" ")
    continuar = input("Deseja realizar outra venda? (s/n): ")
    if continuar.lower() != 's':
        ticketmedio = totalgeral / qtdadevendas
        exibir_fechamento(qtdadevendas, qtdatotal, subtotalgeral, descontogeral, totalgeral, movimento, maiortotal, ticketmedio)
        break