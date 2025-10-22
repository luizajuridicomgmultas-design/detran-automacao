import os
from dotenv import load_dotenv

load_dotenv()

GOVBR_CPF = os.getenv("GOVBR_CPF", "")
GOVBR_PASSWORD_ENCRYPTED = os.getenv("GOVBR_PASSWORD_ENCRYPTED", "")

INPUT_CSV = os.getenv("INPUT_CSV", "input.csv")
OUTPUT_CSV = os.getenv("OUTPUT_CSV", "output.csv")
COOKIES_FILE = os.getenv("COOKIES_FILE", "govbr_cookies.json")

DETRAN_URL = "https://transito.mg.gov.br/veiculos/situacao-do-veiculo/consulta-de-situacao-do-veiculo"

MAX_REQUESTS_PER_HOUR = 15
DELAY_MIN = 2
DELAY_MAX = 5
