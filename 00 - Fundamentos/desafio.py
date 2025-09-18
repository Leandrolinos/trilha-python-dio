def exibir_menu():
    return """
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

    if opcao == "d":
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