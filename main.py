
def menu():
    menus = ("""
        ========== MENU ==========
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuario
    [q] Sair
    """)
    return input(menus)

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite
    exedeu_saque = numero_saques > limite_saques

    if exedeu_saldo:
        print("sem saldo")
    elif exedeu_limite:
        print("valor do saque é maior do que o limite permitido")
    elif exedeu_saque:
        print("voce exedeu o numero de saques por hoje")
    elif valor > 0:
        saldo -= valor
        extrato += f"valor sacado é R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("erro na transação...")

    return saldo, extrato, numero_saques

def  deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"valor depositado é R${valor:.2f}\n"
    else:
        print("erro no deposito...")

    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("digte seu CPF(ATENÇAÕ; APENAS NUMEROS: )")


    if filtra_usuario(cpf, usuarios):
        print("ja existe usuario com esse cpf")
        return

    nome = input("digite seu nome: ")
    data_nascimento = input("digite sua data de nascimento -> (dd-mm-aaaa): ")
    endereco = input("digite seu endereço. desse jeito -> (logradouro, bairro - numero - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("USUARIO CADASTRADO COM SUCESSO!!!")

def filtra_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("digite seu CPF(ATENÇAÕ; APENAS NUMEROS: )")
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("===conta criada com sucesso!!!===")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuarios":usuarios}

    print("usuario não encontrado...")
    return None


def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    print(extrato if extrato else "nemhum extrato")
    print(f"seu saldo é R${saldo:.2f}")
    print("====================\n")


def main():
    limite_saques = 2
    numero_saques = 0
    agencia = "0001"

    saldo = 500
    limite = 500
    extrato = ""
    usuarios = []
    contas = []
    numero_contas = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("digite o valor do deposito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("digite o valor do sacar: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            conta = criar_conta(agencia, numero_contas, usuarios)
            if conta:
                contas.append(conta)
                numero_contas += 1
        elif opcao == "q":
            print("Saindo do sistema, até logo...")
            break

main()