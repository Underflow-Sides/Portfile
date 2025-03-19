import os
os.system("cls")

# Layout inicial
print("=" * 59)
print("Calculatroco (versão 1.0)".center(59))
print("=" * 59)

# Loop principal do programa
while True:

    # Espaço vazio para organização
    print()

    #  Entrada para sair do programa
    sair = input("Digite: (sair) para encerrar o calculatroco, ou precione qualquer atalho para continuar.  ").strip().lower()
    if sair == "sair":
        print("=" * 59)
        print("Programa encerrado! Obrigado por usar o Calculatroco v1.0".center(59))
        print("=" * 59)
        break

    # Se não optar por parar, vamos começar o programa, pegando os valores da compra e do pagamento
    try:
        valor_compra = float(input("Digite aqui, o valor da compra do cliente: R$"))
        valor_pago = float(input("Digite aqui, o valor recebido pelo cliente: R$"))
        
        #Fazer a regra de, não pode ter números negativos.
        if valor_compra < 0 or valor_pago < 0:
            print("Os valores não podem ser negativos, por favor, tente novamente.")
            continue
        
        # Verificar diferença entre valor da compra e valor pago, para calcular quanto falta receber
        elif valor_compra > valor_pago:
            falta = valor_compra - valor_pago
            print(f"Falta receber do cliente, o total de R${falta:.2f}")

            #relação do valor recebido, com a compra, para calcular o troco
        elif valor_pago > valor_compra:
            troco = valor_pago - valor_compra
            print(f"Precisa dar R${troco:.2f} de troco ao cliente.")

            #Se ambos valores forem iguais, não precisa de troco
        else:
            print("Tudo certo por aqui, não precisa dar troco.")

    #Para corrigir a tela de erro por strings
    except ValueError:
        print("Entrada inválida. Por favor, digite NÚMEROS validos.")
