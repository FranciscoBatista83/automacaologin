from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import openpyxl
from time import sleep
import random
from datetime import datetime



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

def verifica_campo(campo, nome_campo):
    if not campo.get_attribute('value'):
        raise ValueError(f"O campo '{nome_campo}' não foi preenchido corretamente.")

def linha_completa(row):
    return all(campo not in [None, ''] for campo in row)

def cadastrar_item(value, xpath, frase):
    item = driver.find_element(By.XPATH, xpath)
       
    if isinstance(value, datetime):
        valor_formatado = value.strftime("%d-%m-%Y")
        item.send_keys(valor_formatado)
    else:
        digitar_naturalmente(value, item)  

    verifica_campo(item, frase)
    sleep(1)


driver = iniciar_driver()

driver.get('https://sistemalogin.franciscobatista.com')
sleep(2)

driver.maximize_window()
sleep(2)


# Tela login e senha
campo_usuario = driver.find_element(By.XPATH, "//input[@id='usuario']")
sleep(1)
digitar_naturalmente('admin', campo_usuario)
sleep(2)

campo_senha = driver.find_element(By.XPATH, "//input[@id='senha']")
sleep(1)
digitar_naturalmente('1234' ,campo_senha)
sleep(2)

botao_entrar = driver.find_element(By.XPATH, "//button[@type='submit']")
sleep(1)
botao_entrar.click()
sleep(2)
#Entramos na tela login e senha



# Caminho para a planilha Excel
caminho_planilha = "C:/Users/User/Documents/Repositorio_local/automacaologin/produtos_supermercado.xlsx"

# Abrir a planilha e acessar a aba ativa
workbook = openpyxl.load_workbook(caminho_planilha)
sheet = workbook.active

# Iterar pelas linhas da planilha (excluindo o cabeçalho)
for row in sheet.iter_rows(min_row=2, values_only=True):  # Começa na linha 2
    id_value, nome_produto_value, valor_value, quantidade_value, fornecedor_value, data_value, codigo_value = row

    if not linha_completa(row):
        print(f"linha incolpleta : {row}")
        # Exibe o alerta
        print(f"Alerta, Linha {id_value} incompleta") 
        continue

    else:

        sleep(1)

        cadastrar_item(nome_produto_value, "//input[@id='nomeProduto']", "Nome produto" )
        cadastrar_item(str(valor_value), "//input[@id='valor']", "Valor" )
        cadastrar_item(str(quantidade_value), "//input[@id='quantidade']", "Quantidade" )
        cadastrar_item(fornecedor_value, "//input[@id='fornecedor']", "Fornecedor")
        cadastrar_item(data_value, "//input[@id='produtoData']", "Data")
        cadastrar_item(str(codigo_value), "//input[@id='codigo']", "Código")

        botao_cadastrar = driver.find_element(By.XPATH, "//button[@id='submitButton']").click()
        sleep(3)

driver.quit()

workbook.close()
   
    
driver.close()


