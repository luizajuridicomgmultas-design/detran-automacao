import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import time, random
from config import INPUT_CSV, OUTPUT_CSV, COOKIES_FILE, DETRAN_URL
import json

def carregar_cookies(context):
    try:
        with open(COOKIES_FILE, "r") as f:
            cookies = json.load(f)
        context.add_cookies(cookies)
    except FileNotFoundError:
        print("Arquivo de cookies não encontrado. Faça login Gov.br e gere o arquivo.")

def extrair_data_limite_de_ait(page, ait_alvo):
    try:
        tabela = page.wait_for_selector("table.multas tbody tr", timeout=5000)
    except PlaywrightTimeout:
        return None, "Não virou multa"

    linhas = page.query_selector_all("table.multas tbody tr")
    for linha in linhas:
        detalhe = linha.query_selector("button.detalhes, i.fa-list")
        if detalhe:
            detalhe.click()
            page.wait_for_selector("dd.ait", timeout=5000)
            time.sleep(random.uniform(0.5, 1.5))
            ait_text = page.locator("dd.ait").inner_text().strip()
            if ait_text == ait_alvo:
                dts = page.locator("dt.col-12.col-md-5").all_text_contents()
                dds = page.locator("dd.col-12.col-md-7").all_text_contents()
                for dt, dd in zip(dts, dds):
                    if "Data Limite de Recurso" in dt:
                        page.click("button.close, button[aria-label='Fechar']")
                        return dd.strip(), "Penalidade"
            page.click("button.close, button[aria-label='Fechar']")
            time.sleep(random.uniform(0.3, 0.8))
    return None, "Não virou multa"

def processar_lote():
    df = pd.read_csv(INPUT_CSV, dtype=str)
    resultados = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(locale="pt-BR", timezone_id="America/Sao_Paulo")
        carregar_cookies(context)
        page = context.new_page()

        for _, row in df.iterrows():
            placa, chassi, renavam, ait = [row[c].strip() for c in ["placa","chassi","renavam","ait"]]
            page.goto(DETRAN_URL)
            time.sleep(random.uniform(1, 2))

            page.fill('input[name="placa"]', placa)
            page.fill('input[name="chassi"]', chassi)
            page.fill('input[name="renavam"]', renavam)
            page.click('button:has-text("Pesquisar")')
            page.wait_for_load_state("networkidle")
            time.sleep(random.uniform(2, 4))

            data_limite, status = extrair_data_limite_de_ait(page, ait)
            resultados.append({
                "placa": placa,
                "chassi": chassi,
                "renavam": renavam,
                "ait": ait,
                "status": status,
                "data_limite_recurso": data_limite or ""
            })
        browser.close()
    pd.DataFrame(resultados).to_csv(OUTPUT_CSV, index=False)
    print(f"Resultado salvo em {OUTPUT_CSV}")

if __name__ == "__main__":
    processar_lote()
