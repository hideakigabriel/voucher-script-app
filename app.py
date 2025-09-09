from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

# --- CONFIGURAÇÕES ---
URL_LOGIN = "https://dashboard.com/login"
USUARIO = "seu_usuario"
SENHA = "sua_senha"

URL_CUPOM = "https://seudashboard.com/cupom/novo"

# Dados do cupom
email_cliente = "cliente@email.com"
nome_cliente = "João da Silva"
desconto = "20"  # porcentagem

# --- INICIAR NAVEGADOR ---
driver = webdriver.Chrome()
driver.maximize_window()

# --- LOGIN ---
driver.get(URL_LOGIN)
time.sleep(2)

driver.find_element(By.ID, "usuario").send_keys(USUARIO)
driver.find_element(By.ID, "senha").send_keys(SENHA)
driver.find_element(By.ID, "botao_login").click()
time.sleep(3)

# --- IR PARA PÁGINA DE CUPOM ---
driver.get(URL_CUPOM)
time.sleep(2)

# --- PREENCHER FORMULÁRIO ---
driver.find_element(By.ID, "email").send_keys(email_cliente)
driver.find_element(By.ID, "nome").send_keys(nome_cliente)
driver.find_element(By.ID, "desconto").send_keys(desconto)

# --- ATIVAR BOTÕES (checkbox/toggle) ---
driver.find_element(By.ID, "ativar_cupom").click()   # exemplo de checkbox
driver.find_element(By.ID, "enviar_email").click()   # outro botão

# --- SELECIONAR UMA OPÇÃO DE LISTA ---
select_element = driver.find_element(By.ID, "tipo_cupom")
select = Select(select_element)
select.select_by_visible_text("Primeira Compra")  # ou por value: select.select_by_value("primeira")

# --- TRATAR ALERTAS (prompt de JS) ---
# Supondo que ao salvar aparece um prompt pedindo nome do cupom
driver.find_element(By.ID, "salvar_cupom").click()
time.sleep(2)

alert = Alert(driver)
alert.send_keys("CUPOM-JOAO-20OFF")  # digita no prompt
alert.accept()  # confirma

# --- FINALIZA ---
print("✅ Cupom criado com sucesso!")
time.sleep(3)
driver.quit()