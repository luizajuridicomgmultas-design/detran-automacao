from crypto_config import criptografar

def main():
    cpf = input("Digite seu CPF (só números): ")
    senha = input("Digite sua senha Gov.br: ")
    senha_cript = criptografar(senha)
    print(f"Coloque este valor no Railway como GOVBR_PASSWORD_ENCRYPTED:\n{senha_cript}")

if __name__ == "__main__":
    main()
