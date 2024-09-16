def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida!"

def calculadora():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"Resultado: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opção inválida!")

calculadora()
