# Navegador Automático com Selenium e Tkinter

Este projeto tem como objetivo criar um navegador automático que abre várias URLs em abas diferentes, alterna entre elas em tela cheia e, opcionalmente, realiza login em algumas delas. Foi desenvolvido utilizando Python, Selenium para automação de navegador, e Tkinter para a interface gráfica.

## Funcionalidades

- Abre um conjunto de URLs em abas do navegador Chrome.
- Alterna automaticamente entre as abas em intervalos de tempo definidos.
- Suporte a login automático para URLs específicas.
- Interface gráfica para adicionar novas URLs, tempo de espera e credenciais de login.
- Conversão do script Python em um executável usando `auto-py-to-exe`.

## URLs Padrão

- [Google](http://www.google.com)
- [Facebook](http://www.facebook.com)
- [Instagram](http://www.instagram.com)

## Requisitos

- Python 3.7 ou superior
- Google Chrome
- ChromeDriver correspondente à versão do seu Google Chrome

## Instalação

### Passos para Instalar o ChromeDriver

1. **Verificar a versão do Google Chrome instalada**:
    - Abra o Google Chrome e vá até `chrome://settings/help` para ver a versão do Chrome instalada.

2. **Baixar a versão correspondente do ChromeDriver**:
    - Visite o site oficial do ChromeDriver: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - Encontre e baixe a versão do ChromeDriver que corresponde à versão do seu Google Chrome.

3. **Instalar o ChromeDriver**:
    ```bash
    # Baixe o ChromeDriver
    wget https://chromedriver.storage.googleapis.com/XX.YY.ZZ/chromedriver_linux64.zip  # substitua XX.YY.ZZ pela versão apropriada

    # Descompacte o arquivo baixado
    unzip chromedriver_linux64.zip

    # Torne o ChromeDriver executável
    chmod +x chromedriver

    # Mova o ChromeDriver para um diretório incluído no PATH
    sudo mv chromedriver /usr/local/bin/
    ```

### Instalar Dependências

```bash
pip install -r requirements.txt


