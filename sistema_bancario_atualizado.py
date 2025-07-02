def main():
    print("=" * 25 + " SISTEMA BANCÁRIO " + "=" * 25)
    print("""
[1] - DEPOSITAR
[2] - SACAR 
[3] - EXTRATO
[4] - CADASTRAR USUÁRIO
[5] - CRIAR CONTA
[6] - SAIR
""")

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500
usuarios = []
contas = []
AGENCIA_PADRAO = "0001"
numero_conta = 1

def realizar_deposito(saldo, extrato, deposito):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("Não é possível depositar valores negativos.")
    return saldo, extrato

def realizar_saque(valor_saque, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):    
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite de R$500.00.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    else:
        saldo -= valor_saque
        extrato += f"Saque: R${valor_saque:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques

def ver_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if extrato:
        print(extrato)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===================\n")

def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\nJá existe usuário com esse CPF!")
            return False

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("=== Usuário criado com sucesso! ===")
    return True

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário para associar a conta: ")

    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if usuario is None:
        print("\nUsuário não encontrado, cadastro de conta não realizado!")
        return False

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")
    return True

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | CPF: {conta['usuario']['cpf']}")

while True:
    main()
    try:
        op = int(input("Bem-vindo! Qual operação deseja realizar? "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    if op == 1:
        try:
            valor_deposito = float(input("Digite o valor a ser depositado:"))
            saldo, extrato = realizar_deposito(saldo, extrato, valor_deposito)
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    elif op == 2:
        try:
            valor_saque = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato, numero_saques = realizar_saque(
                valor_saque, saldo, extrato, limite, numero_saques, LIMITE_SAQUES
            )
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    elif op == 3:
        ver_extrato(saldo, extrato)

    elif op == 4:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

    elif op == 5:
        sucesso = criar_conta(AGENCIA_PADRAO, numero_conta, usuarios, contas)
        if sucesso:
            numero_conta += 1

    elif op == 6:
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")
