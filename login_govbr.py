from playwright.sync_api import sync_playwright
import pandas as pd
from config import GOVBR_CPF, GOVBR_PASSWORD_ENCRYPTED
from crypto_config import descriptografar

def main():
    senha = descriptografar(GOVBR_PASSWORD_ENCRYPTED)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://transito.mg.gov.br/veiculos/situacao-do-veiculo/consulta-de-situacao-do-veiculo")
        print("Faça login manualmente no Gov.br. Após login, aperte Enter aqui.")
        input()
        cookies = context.cookies()
        pd.DataFrame(cookies).to_json("govbr_cookies.json", orient="records")
        browser.close()

if __name__=="__main__":
    main()
