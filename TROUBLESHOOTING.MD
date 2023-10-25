# Troubleshooting


```
'pip' is not recognized as an internal or external command,
operable program or batch file.
```
ou
```
zsh: command not found: pip
```
Esse erro indica que o Python não está instalado no computador.

Para corrigir instale o [Python](https://www.python.org/downloads/release/python-390/)

---
```
'behave' is not recognized as an internal or external command,
operable program or batch file.
```
ou
```
zsh: command not found: behave
zsh: command not found: features
```
Esse erro indica que não foram instalada as dependencias do projeto. 
Para instalar as dependencias, execute o comando: 
```
pip install -r requirements.txt
```

---
```
sh: 1: google-chrome: not found
/bin/sh: 1: google-chrome-stable: not found
/bin/sh: 1: google-chrome-beta: not found
/bin/sh: 1: google-chrome-dev: not found
/bin/sh: 1: google-chrome: not found
/bin/sh: 1: google-chrome-stable: not found
/bin/sh: 1: google-chrome-beta: not found
```
Esse erro indica que o Google Chrome não está instalado no computador.
Para corrigir no windows instale o [Chrome](https://www.google.com/intl/pt-BR/chrome/)

Caso esteja rodando em ambiente Linux execute os seguintes comandos:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
google-chrome-stable --version
```

---
```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Orlan\AppData\Local\Programs\Python\Python312\Scripts\behave.exe\__main__.py", line 4, in <module>
  File "C:\Users\Orlan\AppData\Local\Programs\Python\Python312\Lib\site-packages\behave\__main__.py", line 8, in <module>
    from behave.configuration import Configuration, ConfigError
  File "C:\Users\Orlan\AppData\Local\Programs\Python\Python312\Lib\site-packages\behave\configuration.py", line 11, in <module>
    from six.moves import configparser
ModuleNotFoundError: No module named 'six.moves'
```
Esse erro indica incompatibilidade com o modulo six com as versões mais novas do python.
Certifique se que a verão do Python que você está rodando é a 3.9.  
Para baixar a versão 3.9 clique [aqui](https://www.python.org/downloads/release/python-390/).