def exibir_menu():
    print("=" * 25 + " SISTEMA BANCÁRIO " + "=" * 25)
    print("""
[1] - DEPOSITAR
[2] - SACAR 
[3] - EXTRATO
[4] - CADASTRAR USUÁRIO
[5] - CRIAR CONTA
[6] - LISTAR CONTAS
[7] - SAIR
""")


def realizar_deposito(saldo, extrato):
    try:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Não é possível depositar valores negativos.")
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
    return saldo, extrato


def realizar_saque(saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("Operação falhou! Valor excede o limite de R$ 500.00.")
        elif numero_saques >= limite_saques:
            print("Operação falhou! Limite diário de saques atingido.")
        elif valor <= 0:
            print("Operação falhou! Valor inválido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
    return saldo, extrato, numero_saques


def ver_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================\n")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def encontrar_usuario_por_cpf(usuarios, cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário para associar à conta: ")
    usuario = encontrar_usuario_por_cpf(usuarios, cpf)

    if usuario:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print("Conta criada com sucesso!")
        return True
    else:
        print("Usuário não encontrado. Cadastro da conta não realizado.")
        return False


def listar_contas(contas):
    print("\n===== LISTA DE CONTAS =====")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']} | CPF: {conta['usuario']['cpf']}")
    print("===========================\n")


def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    limite = 500
    usuarios = []
    contas = []
    AGENCIA_PADRAO = "0001"
    numero_conta = 1

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            saldo, extrato = realizar_deposito(saldo, extrato)

        elif opcao == 2:
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == 3:
            ver_extrato(saldo, extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            sucesso = criar_conta(AGENCIA_PADRAO, numero_conta, usuarios, contas)
            if sucesso:
                numero_conta += 1

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Execução
main()
