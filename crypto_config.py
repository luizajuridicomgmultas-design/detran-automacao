from cryptography.fernet import Fernet
import os

KEY_FILE = "chave_secreta.key"

def gerar_chave():
    if not os.path.exists(KEY_FILE):
        chave = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(chave)
    else:
        with open(KEY_FILE, "rb") as f:
            chave = f.read()
    return chave

def criptografar(texto):
    chave = gerar_chave()
    f = Fernet(chave)
    return f.encrypt(texto.encode()).decode()

def descriptografar(token):
    chave = gerar_chave()
    f = Fernet(chave)
    return f.decrypt(token.encode()).decode()
