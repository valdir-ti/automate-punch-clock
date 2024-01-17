import os
from dotenv import load_dotenv
import pyautogui
import subprocess
import time
import pyperclip

load_dotenv()

SECRET_LINK = os.environ.get('SECRET_LINK')
SECRET_CODE = os.environ.get('SECRET_CODE')
SECRET_PIN = os.environ.get('SECRET_PIN')
SECRET_CPF = os.environ.get('SECRET_CPF')

# Pausa para dar tempo de focar no local correto
time.sleep(1)

# Abre o Google Chrome
subprocess.run(['google-chrome', '--incognito'])

pyautogui.hotkey('ctrl', 'l')

# Copia o link para a área de transferência
pyperclip.copy(SECRET_LINK)

pyautogui.hotkey('ctrl', 'v')

# Pressiona Enter para abrir o link
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=570, y=390, duration=1)

time.sleep(2)

pyautogui.click(x=333, y=577, duration=1)

time.sleep(1)

# Digitando o email no campo
pyautogui.write(SECRET_CODE)

# Indo para o próximo campo
pyautogui.press('tab')

time.sleep(1)

pyautogui.write(SECRET_PIN)

pyautogui.press('tab')

time.sleep(1)

pyautogui.click(x=428, y=671, duration=1)

time.sleep(1)

pyautogui.click(x=534, y=750, duration=1)

# Segunda aba
time.sleep(5)

pyautogui.click(x=380, y=590, duration=1)

pyautogui.write(SECRET_CPF)

time.sleep(2)

pyautogui.click(x=550, y=660, duration=1)

# Fecha a janela do Chrome
pyautogui.hotkey('alt', 'f4')