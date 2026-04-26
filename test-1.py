import pyautogui as gui
import time
import pyperclip

gui.keyDown('win')
gui.press('r')
gui.keyUp('win')
gui.press('tab')
gui.press('enter')
time.sleep(0.5)
gui.typewrite('start chrome')
gui.press('enter')
time.sleep(3)
gui.click(605, 444)
time.sleep(1)
gui.typewrite('chatgpt.com')
gui.press('enter')
