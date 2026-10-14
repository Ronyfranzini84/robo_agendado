# Robô Agendado de Relatórios Logísticos

Projeto de estudo em Python que automatiza a geração de um relatório logístico em Excel e o seu envio por e-mail, podendo ser executado uma única vez ou agendado para rodar periodicamente. O repositório também reúne pequenos scripts de estudo sobre `threading` em Python.

## Funcionalidades

- **Geração de relatório** (`report.py`): cria uma planilha `.xlsx` com dados de exemplo (depósitos, transportadoras, cargas e volumes) usando `pandas`/`openpyxl`, salva em `~/Downloads/robo_relatorios`.
- **Envio por e-mail** (`email_sender.py`): envia o relatório gerado como anexo via SMTP (Gmail), com credenciais lidas de variáveis de ambiente (`python-dotenv`).
- **Execução única** (`main.py`): gera o relatório, envia o e-mail e grava um registro da execução em `logs/execucoes.txt`.
- **Agendamento** (`config.json` + `schedule`): permite rodar o robô a cada N minutos/horas ou diariamente em um horário fixo.
  - `scheduler.py`: agendador simples, executa o robô de forma sequencial.
  - `scheduler_threading.py`: agendador que executa o robô em uma thread separada, usando um `threading.Lock` para ignorar novas execuções enquanto a anterior ainda estiver em andamento (evita sobreposição).
- **Scripts de estudo sobre threading**:
  - `threading_test.py`: duas threads executando tarefas em paralelo.
  - `threading_lock_test.py`: uso de `threading.Lock` para proteger uma variável compartilhada entre threads.
- **Testes manuais**:
  - `test_config.py`: valida se as variáveis de ambiente de e-mail foram carregadas corretamente.
  - `test_email.py`: executa o fluxo completo de geração do relatório e envio por e-mail.

## Estrutura do projeto

```
robo_agendado/
├── main.py                  # Ponto de entrada: gera relatório + envia e-mail + grava log
├── report.py                 # Geração do relatório Excel (dados de exemplo)
├── email_sender.py           # Envio do relatório por e-mail via SMTP
├── scheduler.py               # Agendador simples (execução sequencial)
├── scheduler_threading.py    # Agendador com threading + lock (evita execuções sobrepostas)
├── threading_test.py          # Estudo: threads básicas
├── threading_lock_test.py    # Estudo: threads + lock
├── test_config.py             # Teste manual: variáveis de ambiente de e-mail
├── test_email.py               # Teste manual: geração + envio do relatório
├── config.json                # Configuração de agendamento (intervalo/frequência/horário)
├── requirements.txt            # Dependências do projeto
├── logs/                        # Logs gerados em tempo de execução
│   ├── execucoes.txt           # Histórico de execuções do robô
│   ├── scheduler.log            # Log do scheduler.py
│   └── scheduler_threading.log # Log do scheduler_threading.py
└── .env                         # Variáveis de ambiente (não versionado)
```

## Pré-requisitos

- Python 3.13+ (desenvolvido/testado com Python 3.13.3)
- Uma conta de e-mail (ex.: Gmail) com uma **senha de app** para autenticação SMTP

## Instalação

1. Clone o repositório e acesse a pasta do projeto.
2. (Recomendado) Crie e ative um ambiente virtual:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```

## Configuração

### Variáveis de ambiente (`.env`)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
EMAIL_RECIPIENT=destinatario@exemplo.com
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
```

> ⚠️ O `.env` contém credenciais sensíveis e já está listado no `.gitignore` — nunca o adicione ao controle de versão.

### Agendamento (`config.json`)

```json
{
    "interval": "minutes",
    "frequency": 1,
    "daily_time": "08:00"
}
```

| Campo | Descrição |
|---|---|
| `interval` | `"minutes"`, `"hours"` ou `"days"` |
| `frequency` | A cada quantas unidades o robô deve rodar (usado para `minutes`/`hours`) |
| `daily_time` | Horário `HH:MM` usado quando `interval` é `"days"` |

## Como usar

### Executar uma única vez

```powershell
python main.py
```

Gera o relatório, envia por e-mail e registra a execução em `logs/execucoes.txt`.

### Executar com agendamento (versão simples)

```powershell
python scheduler.py
```

Executa o robô repetidamente conforme `config.json`. Pressione `Ctrl+C` para parar. Logs em `logs/scheduler.log`.

### Executar com agendamento (versão com threading)

```powershell
python scheduler_threading.py
```

Mesma lógica de agendamento, porém cada execução roda em uma thread separada. Um `Lock` garante que uma nova execução seja ignorada caso a anterior ainda esteja em andamento. Logs em `logs/scheduler_threading.log`.

## Testes manuais

```powershell
python test_config.py   # verifica se as variáveis de e-mail foram carregadas
python test_email.py    # gera um relatório e o envia por e-mail, de ponta a ponta
```

## Dependências principais

| Pacote | Uso |
|---|---|
| `pandas` | Manipulação de dados e geração do relatório |
| `openpyxl` | Exportação do relatório para `.xlsx` |
| `schedule` | Agendamento das execuções |
| `python-dotenv` | Carregamento das variáveis de ambiente do `.env` |

## Observações

- Este é um **projeto de estudo**, com foco em automação (RPA), agendamento de tarefas e `threading` em Python.
- Os dados do relatório em `report.py` são fictícios, usados apenas para fins de demonstração.
- Os relatórios gerados são salvos em `~/Downloads/robo_relatorios`.
