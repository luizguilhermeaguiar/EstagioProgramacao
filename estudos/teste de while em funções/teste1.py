'''def solicitar_nome():
    while True: # usando o while True para a verificar se o nome do produto é uma entrada valida 
            nome = input("Nome do produto: ")
            if nome.strip(): #função nativa do python que remove espações em brancos, então o teste funciona mesmo que o usuário digite apenas espaços em branco
                return nome
            print("Erro: o nome do produto não pode estar vazio.")
            print(" ")

nome = solicitar_nome()
print(nome)


def calcular_operacao(a, b):
    soma = a + b
    multiplicacao = a * b
    return soma, multiplicacao

resultado_soma, resultado_mult = calcular_operacao(5, 3)
print(resultado_soma, resultado_mult)'''

def realizar_venda():
    nome = solicitar_nome()
    preco = solicitar_preco()
    quantidade = solicitar_quantidade()

    subtotal = preco * quantidade 
    porcentagem = calcular_desconto(subtotal)

    desconto = subtotal * porcentagem
    total = subtotal - desconto

    exibir_resumo_venda(nome, preco, quantidade, subtotal, porcentagem, desconto, total)

    return quantidade, subtotal, desconto, total