menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso")

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo #Verifica se o valor de saque é maior que o saldo

        excedeu_limite = valor_saque > limite #Verifica se o valor de saque é maior que o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES #Verifica se excedeu o limite de saque diário

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1 #Adiciona o número de saque diário
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso")

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":
        print("\n ================== EXTRATO BANCÁRIO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n =====================================================")


    elif opcao == "0":
        print("Agradecemos por usar o nosso banco. Volte sempre!")
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")