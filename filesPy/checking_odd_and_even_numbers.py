def verificar_paridade(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

def solicitar_numero():
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    numero = solicitar_numero()
    resultado = verificar_paridade(numero)
    print(resultado)
