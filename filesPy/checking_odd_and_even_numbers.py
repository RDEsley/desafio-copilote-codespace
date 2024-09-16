def verificar_paridade(numero):
    """Função que verifica se um número é par ou ímpar."""
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

def solicitar_numero():
    """Solicita um número inteiro ao usuário e valida a entrada."""
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    numero = solicitar_numero()
    resultado = verificar_paridade(numero)
    print(resultado)
