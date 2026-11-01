def verificar_situacao(p_nota):
    if p_nota < 0 or p_nota > 10:
        return "Nota inválida!"

    elif p_nota < 5:
        return "Reprovado"

    elif p_nota < 7:
        return "Recuperação"

    else:
        return "Aprovado"

nota = float(input("Digite a nota do aluno: ")) 
situação = verificar_situacao(nota)

print(f"Situação do aluno: {situação}")