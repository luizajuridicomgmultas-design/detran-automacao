# Guia Completo para Executar na Nuvem com Railway

## Passo 1 - Preparar Repositório
- Coloque todos os arquivos no diretório `detran-automacao`
- Faça commit e push para GitHub

## Passo 2 - Configurar Railway
- Crie uma conta em railway.app
- Crie projeto novo conectando GitHub ao repositório
- Defina variáveis de ambiente necessárias:
  - GOVBR_CPF
  - GOVBR_PASSWORD_ENCRYPTED
  - INPUT_CSV
  - OUTPUT_CSV
  - COOKIES_FILE

## Passo 3 - Agendamento
- Configure cron job para rodar script em horários desejados

## Passo 4 - Monitoramento
- Verifique logs e status pelo painel Railway
- Baixe o arquivo `output.csv` para consultar resultados

## Segurança
- Nunca coloque senha plain em variáveis de ambiente, use criptografia
- Não compartilhe chave secreta e cookies

---
