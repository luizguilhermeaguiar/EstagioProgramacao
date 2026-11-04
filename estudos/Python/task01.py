def somar(p_n1, p_n2):
    return p_n1 + p_n2

def subtrair(p_n1, p_n2):
    return p_n1 - p_n2

def multiplicar(p_n1, p_n2):
    return p_n1 * p_n2


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = somar(n1, n2)
subtração = subtrair(n1, n2)
multiplicação = multiplicar(n1, n2)

print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
print(f"Multiplicação: {multiplicação}")