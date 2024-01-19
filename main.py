import os
import time
import pyautogui
import pyperclip
import subprocess
from dotenv import load_dotenv

# Carrega as variaveis de ambiente
load_dotenv()
SECRET_LINK = os.environ.get('SECRET_LINK')
SECRET_CODE = os.environ.get('SECRET_CODE')
SECRET_PIN = os.environ.get('SECRET_PIN')
SECRET_CPF = os.environ.get('SECRET_CPF')

# Abre o Google Chrome
subprocess.run(['google-chrome'])

time.sleep(2)

# Foca na barra de digitação do navegador
pyautogui.hotkey('ctrl', 'l')

# Copia o link para a área de transferência
pyperclip.copy(SECRET_LINK)

# Cola o link na área de endereço
pyautogui.hotkey('ctrl', 'v')

# Pressiona Enter para abrir o link
pyautogui.press('enter')

time.sleep(2)

pyautogui.hotkey('F11')

time.sleep(2)

# Clica na aba Registrar ponto
pyautogui.click(x=290, y=250, duration=1)

time.sleep(1)

# Clica no campo de código
pyautogui.click(x=50, y=440, duration=1)

time.sleep(1)

# Digita no campo do código
pyautogui.write(SECRET_CODE.upper())

# Vai para o próximo campo
pyautogui.press('tab')

time.sleep(1)

# Digita no campo do PIN
pyautogui.write(SECRET_PIN)

# Clica no campo de captcha
pyautogui.click(x=150, y=540, duration=1)

time.sleep(2)

# Clica no botão registrar
pyautogui.click(x=255, y=620, duration=1)

# Segunda aba
time.sleep(3)

# Clica no campo de CPF
pyautogui.click(x=50, y=440, duration=1)

time.sleep(1)

# Digita no campo CPF pausadamente
for char in str(SECRET_CPF):
    pyautogui.typewrite(char)
    time.sleep(0.3)

# Clica para finalizar o processo
pyautogui.click(x=273, y=525, duration=1)

time.sleep(2)

pyautogui.hotkey('F11')

time.sleep(2)

# Fecha a janela do Chrome
pyautogui.hotkey('ctrl', 'w')