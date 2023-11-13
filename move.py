import pyautogui
import time

while True:
    current_x, current_y = pyautogui.position()
    
    novo_x = current_x + 10
    novo_y = current_y + 10
    pyautogui.moveTo(novo_x, novo_y, duration=0.25)
    
    time.sleep(60)
