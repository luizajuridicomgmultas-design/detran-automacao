# Sistema Automação Consulta Detran MG

Este sistema automatiza consultas de multas e AITs no site do Detran Minas Gerais.

## Funcionalidades

- Login automático via Gov.br
- Consulta de veículos pelo número da placa, chassi e renavam
- Verificação se um AIT específico virou multa
- Extração da data limite de recurso
- Exportação dos resultados em CSV
- Suporte a execução local e cloud (Railway)

## Como usar

1. Configure as credenciais no `.env` ou variáveis de ambiente
2. Rode o `login_govbr.py` para salvar cookies
3. Prepare o `input.csv` com dados
4. Execute `processar_lote.py`
5. Veja resultados no `output.csv`

## Configuração para Railway

- Configure variáveis de ambiente GOVBR_CPF e GOVBR_PASSWORD_ENCRYPTED
- Agende tarefas para rodar em periodicidade desejada

---
