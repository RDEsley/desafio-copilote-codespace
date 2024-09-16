def verificar_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

def solicitar_palavra():
    return input("Digite uma palavra ou frase: ")

if __name__ == "__main__":
    palavra = solicitar_palavra()
    if verificar_palindromo(palavra):
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' não é um palíndromo.")
