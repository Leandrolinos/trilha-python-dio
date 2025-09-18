usuarios = []  
contas = []  

def criar_conta_corrente():
    if not usuarios:
        print("Erro: não há usuários cadastrados. Cadastre um usuário primeiro.")
        return
    
    print("\n=== CRIAÇÃO DE CONTA CORRENTE ===")
    
    # Mostra os usuários cadastrados para escolher
    print("Usuários disponíveis:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nome']} - CPF: {usuario['cpf']}")
    
    try:
        escolha = int(input("Escolha o usuário pelo número: "))
        if escolha < 1 or escolha > len(usuarios):
            print("Erro: usuário inválido.")
            return
    except ValueError:
        print("Erro: escolha inválida.")
        return
    

    usuario_selecionado = usuarios[escolha - 1]
    numero_conta = len(contas) + 1
    agencia = "0001"

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario_selecionado
    }


    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}, Usuário: {usuario_selecionado['nome']}")


def listar_contas():
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    

    print("\n=== CONTAS CADASTRADAS ===")
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Usuário: {usuario['nome']} - CPF: {usuario['cpf']}")
    print("==========================")


def criar_usuario():
    print("\n=== CADASTRO DE USUÁRIO ===")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF (somente números): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: já existe um usuário com esse CPF.")
            return None

    endereco = input("Endereço (logradouro - bairro - cidade/sigla - estado): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


def exibir_menu():
    return """
[u] Criar usuário
[v] Ver usuários cadastrados
[c] Criar conta corrente
[x] Ver contas cadastradas
[d] Depositar
[s] Sacar
[e] Extrato
[l] Limite diário
[q] Sair
=> """


def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: o valor de depósito deve ser positivo.")
    return saldo, extrato


def sacar(saldo, extrato, valor, limite_por_saque, saques_restantes, valor_limite_restante, cota_por_saque):
    if saques_restantes <= 0:
        print("Erro: número máximo de saques diários atingido.")
    elif valor_limite_restante < cota_por_saque:
        print("Erro: limite diário de saque atingido.")
    elif valor <= 0:
        print("Erro: o valor do saque deve ser positivo.")
    elif valor > saldo:
        print("Erro: saldo insuficiente.")
    elif valor > limite_por_saque:
        print(f"Erro: o valor máximo por saque é R$ {limite_por_saque:.2f}.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_restantes -= 1
        valor_limite_restante -= cota_por_saque 
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato, saques_restantes, valor_limite_restante


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


def exibir_limite_diario(saques_restantes, valor_limite_restante):
    print("\n=========== LIMITE DIÁRIO ===========")
    print(f"Saques restantes hoje: {saques_restantes}")
    print(f"Valor restante do limite diário: R$ {valor_limite_restante:.2f}")
    print("=====================================")


def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    print("\n=== USUÁRIOS CADASTRADOS ===")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}:")
        print(f"  Nome: {usuario['nome']}")
        print(f"  Data de nascimento: {usuario['data_nascimento']}")
        print(f"  CPF: {usuario['cpf']}")
        print(f"  Endereço: {usuario['endereco']}")
    print("==============================")


saldo = 0
limite_por_saque = 500
extrato = []
LIMITE_SAQUES_DIARIOS = 3
COTA_POR_SAQUE = 500
LIMITE_VALOR_DIARIO = COTA_POR_SAQUE * LIMITE_SAQUES_DIARIOS  

saques_restantes = LIMITE_SAQUES_DIARIOS
valor_limite_restante = LIMITE_VALOR_DIARIO


while True:
    opcao = input(exibir_menu()).lower()

    if opcao == "u":
        criar_usuario()

    elif opcao == "v":
        listar_usuarios()

    elif opcao == "c":
        criar_conta_corrente()

    elif opcao == "x":
        listar_contas()

    elif opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)
        except ValueError:
            print("Erro: valor inválido. Use números, por favor.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, saques_restantes, valor_limite_restante = sacar(
                saldo, extrato, valor,
                limite_por_saque,
                saques_restantes,
                valor_limite_restante,
                COTA_POR_SAQUE
            )
        except ValueError:
            print("Erro: valor inválido. Use números, por favor.")

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "l":
        exibir_limite_diario(saques_restantes, valor_limite_restante)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")
usuarios = []  
contas = []  

def criar_conta_corrente():
    if not usuarios:
        print("Erro: não há usuários cadastrados. Cadastre um usuário primeiro.")
        return
    
    print("\n=== CRIAÇÃO DE CONTA CORRENTE ===")
    
    # Mostra os usuários cadastrados para escolher
    print("Usuários disponíveis:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nome']} - CPF: {usuario['cpf']}")
    
    try:
        escolha = int(input("Escolha o usuário pelo número: "))
        if escolha < 1 or escolha > len(usuarios):
            print("Erro: usuário inválido.")
            return
    except ValueError:
        print("Erro: escolha inválida.")
        return
    

    usuario_selecionado = usuarios[escolha - 1]
    numero_conta = len(contas) + 1
    agencia = "0001"

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario_selecionado
    }


    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}, Usuário: {usuario_selecionado['nome']}")


def listar_contas():
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    

    print("\n=== CONTAS CADASTRADAS ===")
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Usuário: {usuario['nome']} - CPF: {usuario['cpf']}")
    print("==========================")


def criar_usuario():
    print("\n=== CADASTRO DE USUÁRIO ===")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF (somente números): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: já existe um usuário com esse CPF.")
            return None

    endereco = input("Endereço (logradouro - bairro - cidade/sigla - estado): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


def exibir_menu():
    return """
[u] Criar usuário
[v] Ver usuários cadastrados
[c] Criar conta corrente
[x] Ver contas cadastradas
[d] Depositar
[s] Sacar
[e] Extrato
[l] Limite diário
[q] Sair
=> """


def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: o valor de depósito deve ser positivo.")
    return saldo, extrato


def sacar(saldo, extrato, valor, limite_por_saque, saques_restantes, valor_limite_restante, cota_por_saque):
    if saques_restantes <= 0:
        print("Erro: número máximo de saques diários atingido.")
    elif valor_limite_restante < cota_por_saque:
        print("Erro: limite diário de saque atingido.")
    elif valor <= 0:
        print("Erro: o valor do saque deve ser positivo.")
    elif valor > saldo:
        print("Erro: saldo insuficiente.")
    elif valor > limite_por_saque:
        print(f"Erro: o valor máximo por saque é R$ {limite_por_saque:.2f}.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_restantes -= 1
        valor_limite_restante -= cota_por_saque 
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato, saques_restantes, valor_limite_restante


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


def exibir_limite_diario(saques_restantes, valor_limite_restante):
    print("\n=========== LIMITE DIÁRIO ===========")
    print(f"Saques restantes hoje: {saques_restantes}")
    print(f"Valor restante do limite diário: R$ {valor_limite_restante:.2f}")
    print("=====================================")


def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    print("\n=== USUÁRIOS CADASTRADOS ===")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}:")
        print(f"  Nome: {usuario['nome']}")
        print(f"  Data de nascimento: {usuario['data_nascimento']}")
        print(f"  CPF: {usuario['cpf']}")
        print(f"  Endereço: {usuario['endereco']}")
    print("==============================")


saldo = 0
limite_por_saque = 500
extrato = []
LIMITE_SAQUES_DIARIOS = 3
COTA_POR_SAQUE = 500
LIMITE_VALOR_DIARIO = COTA_POR_SAQUE * LIMITE_SAQUES_DIARIOS  

saques_restantes = LIMITE_SAQUES_DIARIOS
valor_limite_restante = LIMITE_VALOR_DIARIO


while True:
    opcao = input(exibir_menu()).lower()

    if opcao == "u":
        criar_usuario()

    elif opcao == "v":
        listar_usuarios()

    elif opcao == "c":
        criar_conta_corrente()

    elif opcao == "x":
        listar_contas()

    elif opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)
        except ValueError:
            print("Erro: valor inválido. Use números, por favor.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, saques_restantes, valor_limite_restante = sacar(
                saldo, extrato, valor,
                limite_por_saque,
                saques_restantes,
                valor_limite_restante,
                COTA_POR_SAQUE
            )
        except ValueError:
            print("Erro: valor inválido. Use números, por favor.")

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "l":
        exibir_limite_diario(saques_restantes, valor_limite_restante)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")
