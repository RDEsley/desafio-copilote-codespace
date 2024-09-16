def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def solicitar_nota(numero_nota):
    while True:
        try:
            return float(input(f"Digite a {numero_nota}ª nota: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido para a nota")

if __name__ == "__main__":
    nota1 = solicitar_nota(1)
    nota2 = solicitar_nota(2)
    nota3 = solicitar_nota(3)
    
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das três notas é: {media:.2f}")
