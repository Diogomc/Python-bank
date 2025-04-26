options = """
1-Consultar Saldo
2-Depositar
3-Sacar
4-Sair
"""
saldo = 0
while True :
    print(options)
    opt = int(input("Digite um número: "))
    
    
    if opt == 1:
        saldo == saldo
        print(f"Seu saldo atual: {saldo}")
    elif opt == 2:
        print("Digite o valor a ser depositado: ")
        deposito = int(input())
        saldo += deposito
        print(f"Seu saldo atualizado: {saldo}")
    elif opt == 3:
        print("Digite o valor do saque: ")
        saque = int(input())
        saldo -= saque
        print(f"Seu saldo atualizado: {saldo}")
    elif opt == 4:
        print("Obrigado por utilizar nosso caixa 24 horas...")
        break
    else: 
        print("Número inválido. Tente novamente")