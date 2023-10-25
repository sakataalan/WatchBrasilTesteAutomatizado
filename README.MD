<h1 align="center">
    Watch Brasil Teste automatizados em Python
</h1>
<p align="center">
    <img src="https://img.shields.io/badge/Selenium-Behave-black">
</p>

Testes automatizados para os cenários de login, seleção de perfil, seleção de conteúdo, reprodução de conteúdo e logout da plataforma [Watch](https://play.watch.tv.br/login)

# Sumário

- [Tecnologias](#Tecnologias)
- [Como executar](#Como_executar)
    - [Requisitos](#requisitos)
    - [Instalando](#instalando)
    - [Executando](#executando)
    - [Executando no docker](#executando-no-docker)
    - [Troubleshooting](#troubleshooting)
- [Artefatos](#Artefatos)
    - [Resumo de execução](#resumo-de-execução)
    - [Evidências](#Evidências)
    - [Exportar](#Exportar)
- [Estrutura do projeto](#Estrutura-do-projeto)
    - [Configuration](#Configuration)
    - [Evidences](#evidences)
    - [Features](#features)
    - [Helpers](#helpers)
    - [Pages](#pages)
    - [Reports](#reports)

## Tecnologias

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Behave](https://behave.readthedocs.io/)
- [allure-behave](https://github.com/allure-framework/allure-python/tree/master)
- [pytest](https://docs.pytest.org/en/7.4.x/)

## Como executar

### Requisitos
- [Python 3.9](https://www.python.org/downloads/release/python-390/) 
- [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)

### Instalando
Para clonar o respositório, execute o seguinte comando e em seguida acesse o diretorio:
```
git clone https://github.com/sakataalan/WatchBrasilTesteAutomatizado.git
cd WatchBrasilTesteAutomatizado
```
Antes de executar, certifique-se que todas as dependencias foram instaladas rodando o comando:
```
pip install -r requirements.txt
```
### Executando
Para executar os testes automatizados, execute o seguinte comando:
```
behave features/login.feature
```

O processo pode ser acompanhado tanto pelo navegador quanto pelo terminal.

### Executando no docker
Para executar no docker é necessário alterar a linha 16 do arquivo [loginsteps](./features/steps/loginsteps.py) para:
```
options = webdriver.ChromeOptions()
options.add_argument("start-maximized") 
options.add_argument("--disable-extensions")
options.add_argument('--window-size=1920,1080')
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument('--headless')
options.add_argument("--remote-debugging-port=9222")
context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
```
Para executar use os comandos:
```
docker build -t watch-tests .
docker run  watch-tests
```

### Troubleshooting
Qualquer problema ao executar esse projeto consulte o arquivo de [Troubleshooting](TROUBLESHOOTING.MD)


## Artefatos
### Resumo de execução

Ao terminar a execução dos testes automatizados um resumo da execução sera exibido no terminal.


Exemplo:

```
1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
53 steps passed, 0 failed, 0 skipped, 0 undefined
```

### Evidências
As evidências de cada passo dos cenários são salva na pasta evidences, com uma subpasta para cada cenário.

### Exportar
Para exportar o resultado da execução dos testes em formato json, execute o comando:
```
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature
```

## Estrutura do projeto
### Configuration
Responsável por definir as váriaveis de ambiente como Username, Password e tempo de espera para carregar elementos.

### Evidences
Responsável por armazenar capturas de telas das execuções dos cenários

### Features
A pasta features é divida entre arquivos .feature e steps. 
- **.feature:** É responsável por definir os passos de cada cenário na estrutura BDD.
- **steps:** É responsável por definir o que cada passo executará.

### Helpers
É responsável por armazenar funções que podem ser reutilizadas em diversos contextos

### Pages
É responsável por ser a abstração de cada página html que os testes automatizados irão interagir.

### Reports
É responsável por armazenar o resultado da execução dos testes no formato JSON.


