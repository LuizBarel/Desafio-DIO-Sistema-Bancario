# Menu de opções para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

# Inicialização das variáveis
saldo = 0 
limite = 500  
extrato = ""  
numero_saques = 0  
LIMITE_SAQUES = 3  

# Loop infinito para manter o programa em execução
while True:
    opcao = input(menu)

    # Opção de depósito
    if opcao == "d":
        print("Você escolheu a opção Depósito! Caso queira cancelar a operação, digite [0]")
        deposito = float(input("Digite o valor a ser depositado:\n"))

        # Verifica se o usuário deseja cancelar a operação
        if deposito == 0:
            continue

        # Verifica se o valor é positivo
        if deposito > 0:
            # Adiciona o valor ao saldo e atualiza o extrato
            saldo += deposito
            extrato += f"+ R${deposito:.2f}\n"

            print(f"Depósito feito com sucesso! Seu saldo é atual é: {saldo}")
        else:
            print("Você não pode depositar um valor negativo!")

    # Opção de saque
    elif opcao == "s":
        print("Você escolheu a opção Saque! Caso queira cancelar a operação, digite [0]")
        print(f"Você já fez {numero_saques} hoje, seu limite é {LIMITE_SAQUES} por dia!")
        saque = float(input(f"Digite o valor a ser sacado (Máximo por saque: R${limite})"))

        # Verifica se o usuário deseja cancelar a operação
        if saque == 0:
            continue

        # Verifica se o usuário ainda tem saques disponíveis
        possui_saques = True if numero_saques != 3 else False
        # Verifica se o valor está dentro do limite
        saque_dentro_limite = True if saque <= limite else False
        # Verifica se o usuário tem saldo suficiente
        saque_possivel = True if saque <= saldo else False

        # Verifica se o saque é possível
        if possui_saques and saque_dentro_limite and saque_possivel and saque > 0:
            # Realiza o saque e atualiza o extrato
            saldo -= saque
            extrato += f"- R${saque:.2f}\n"
            numero_saques += 1

            print(f"Saque feito com sucesso! Seu saldo é atual é: {saldo}")
        elif not possui_saques:
            print("Você já atingiu o limite de saques hoje!")
        elif not saque_dentro_limite:
            print(f"Você não pode sacar mais do que o limite estabelecido de {limite}!")
        elif not saque_possivel:
            print(f"Você não tem saldo suficiente para realizar o saque! (Saldo: {saldo})")
        else:
            print("Você não pode sacar com um valor inválido!")

    # Opção de extrato
    elif opcao == "e":
        # Exibe o extrato
        print("===========================================================")
        print(f"Você escolheu a opção Extrato! Veja seu extrato abaixo:")
        print(f"{extrato if extrato else "Você não movimentou sua conta"}")
        print(f"Saldo atual: {saldo:.2f}")
        print("===========================================================")

    # Opção de sair
    elif opcao == "q":
        break

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")