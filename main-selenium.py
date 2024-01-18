import os
import time
import pyautogui
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

load_dotenv()
SECRET_LINK = os.environ.get('SECRET_LINK')
SECRET_CODE = os.environ.get('SECRET_CODE')
SECRET_PIN = os.environ.get('SECRET_PIN')
SECRET_CPF = os.environ.get('SECRET_CPF')

# Setup chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(SECRET_LINK)

# Set window to full screen
driver.fullscreen_window()

# Clica na aba Registrar ponto
pyautogui.click(x=290, y=290, duration=1)
time.sleep(1)

# Clica no campo de código
pyautogui.click(x=75, y=580, duration=1)
time.sleep(1)

# Digita no campo do código
pyautogui.write(SECRET_CODE.upper())

# Vai para o próximo campo
pyautogui.press('tab')
time.sleep(1)

# Digita no campo do PIN
pyautogui.write(SECRET_PIN)

# Clica no campo de captcha
pyautogui.click(x=175, y=675, duration=1)
time.sleep(2)

# Clica no botão registrar
pyautogui.click(x=290, y=750, duration=1)
time.sleep(3)

# Segunda aba

# Clica no campo de CPF
pyautogui.click(x=80, y=580, duration=1)
time.sleep(1)

# Digita no campo CPF pausadamente
for char in str(SECRET_CPF):
    pyautogui.typewrite(char)
    time.sleep(0.3)

# Clica para finalizar o processo
pyautogui.click(x=300, y=660, duration=1)

# Close the driver
driver.quit()