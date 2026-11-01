def calcular_percentual(p_vendas):
    if p_vendas < 1000:
        return 0.02

    elif p_vendas < 5000:
        return 0.05

    else: 
        return 0.08

def calcular_comissao(p_vendas, p_percentual):
    return p_vendas * p_percentual


total_vendido = float(input("Digite o total vendido: "))
percentual = calcular_percentual(total_vendido)
comissao = calcular_comissao(total_vendido, percentual)

print(f"Percentual de comissão: {percentual*100:.0f}%")
print(f"Valor da comissão: R$ {comissao:.2f}")