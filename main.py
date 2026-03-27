
def cadastrar_pet(raca, nome, idade):
    return {"raca": raca, "nome": nome, "idade": idade}

def cadastrar_funcionario(nome, endereco, salario):
    return {"nome": nome, "endereco": endereco, "salario": salario}

def cadastrar_cliente(nome, endereco, lista_de_pets):
    return {"nome": nome, "endereco": endereco, "pets": lista_de_pets}

def cadastrar_produto(nome, valor, descricao):
    return {"nome": nome, "valor": valor, "descricao": descricao}

lista_pets = []
lista_clientes = []
lista_funcionarios = []
estoque_produtos = []

def realizar_atividade_funcionario(nome_func, papel):
    if papel.lower() == "veterinario":
        print(f"O veterinário {nome_func} está realizando uma cirurgia.")
    elif papel.lower() == "gestor":
        print(f"O gestor {nome_func} está fechando o caixa do dia.")

def realizar_acao_pet(nome_pet, tipo_pet):
    if tipo_pet.lower() == "Viralata":
        print(f"O Cachorro {nome_pet} saiu para caminhar.")
    elif tipo_pet.lower() == "peixe":
        print(f"O peixe {nome_pet} está recebendo ração no aquário.")

def buscar_pet_por_raca(raca_alvo):
    print(f"\n Busca por raça: {raca_alvo} ")
    for pet in lista_pets:
        if pet["raca"].lower() == raca_alvo.lower():
            print(f"Encontrado: {pet['nome']}")

def buscar_endereco_cliente(nome_cliente):
    for c in lista_clientes:
        if c["nome"].lower() == nome_cliente.lower():
            print(f"\nEndereço do cliente {nome_cliente}: {c['endereco']}")

def buscar_salario_funcionario(nome_func):
    for f in lista_funcionarios:
        if f["nome"].lower() == nome_func.lower():
            print(f"\nSalário de {nome_func}: R$ {f['salario']}")

def excluir_informacao(lista, nome_para_remover):
    for item in lista:
        if item["nome"].lower() == nome_para_remover.lower():
            lista.remove(item)
            print(f"\n{nome_para_remover} foi excluído com sucesso.")
            return

p1 = cadastrar_pet("Poodle", "Bolinha", 2)
p2 = cadastrar_pet("Beta", "Azul", 1)
p3 = cadastrar_pet("Calopsita", "Louro", 3)
p4 = cadastrar_pet("Viralata", "Pipoca", 5)


lista_pets.extend([p1, p2, p3, p4])


eduardo = cadastrar_cliente("Eduardo", "Rua Unisinos, 100", [p1, p2, p3, p4])
lista_clientes.append(eduardo)

veterinario = cadastrar_funcionario("Dr. Arnaldo", "Rua Centro", 5000)
gestor = cadastrar_funcionario("Ana Maria", "Rua Norte", 7000)
lista_funcionarios.extend([veterinario, gestor])


buscar_pet_por_raca("Poodle")
buscar_endereco_cliente("Eduardo")
buscar_salario_funcionario("Dr. Arnaldo")

print("\nAções do Dia")
realizar_atividade_funcionario("Dr. Arnaldo", "veterinario Fábio")
realizar_acao_pet("Azul", "peixe")
realizar_acao_pet("Pipoca", "Viralata")

excluir_informacao(lista_pets, "Azul")
excluir_informacao(lista_pets, "Pipoca")