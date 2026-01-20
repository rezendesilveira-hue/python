import time
import pyautogui
import pyperclip

pyautogui.press('win')
time.sleep(0.5)

pyautogui.write('Firefox')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyperclip.copy('Cotação do Dolar')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=282, y=501)
time.sleep(0.2)
pyautogui.hotkey('crtl' , 'a')
pyautogui.hotkey('crtl' , 'c')

cotacao = pyperclip.paste()

print (f'Cotação do dolar :' {cotacao})