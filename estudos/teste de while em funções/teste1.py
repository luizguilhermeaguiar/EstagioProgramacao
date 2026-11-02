def solicitar_nome():
    while True: # usando o while True para a verificar se o nome do produto é uma entrada valida 
            nome = input("Nome do produto: ")
            if nome.strip(): #função nativa do python que remove espações em brancos, então o teste funciona mesmo que o usuário digite apenas espaços em branco
                return nome
            print("Erro: o nome do produto não pode estar vazio.")
            print(" ")

nome = solicitar_nome()
print(nome)