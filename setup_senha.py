from crypto_config import criptografar

def main():
    cpf = input("02187146618: ")
    senha = input("Fopoqen1@: ")
    senha_cript = criptografar(senha)
    print(f"Coloque este valor no Railway como GOVBR_PASSWORD_ENCRYPTED:\n{senha_cript}")

if __name__ == "__main__":
    main()
