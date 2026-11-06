from app import app

cliente = app.test_client()

def testar_venda(dados, mensagem_esperada):
    resposta = cliente.post("/registrar-venda", data=dados)
    assert mensagem_esperada in resposta.get_data(as_text=True),  'A mensagem esperada não foi encontrada!'
    print("Teste aprovado!")

testar_venda(
    {"produto": "Mouse", "preco": "abc", "quantidade": "2"},
    "Preço inválido!"
)

testar_venda(
    {"produto": "Mouse", "preco": "150", "quantidade": "asdf"},
    "Quantidade inválida!"
)

testar_venda(
    {"produto": "   ", "preco": "56", "quantidade": "2"},
    "Erro: o nome do produto não pode estar vazio!"
)

testar_venda(
    {"produto": "Teclado Gamer", "preco": "150", "quantidade": "2"},
    "Subtotal: R$ 300.00"
)

testar_venda(
    {"produto": "Teclado Gamer", "preco": "19.90", "quantidade": "3"},
    "Subtotal: R$ 59.70"
)

testar_venda(
    {"produto": "Teclado Gamer", "preco": "200", "quantidade": "1"},
    "Subtotal: R$ 200.00"
)