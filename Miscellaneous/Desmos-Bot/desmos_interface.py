from selenium import webdriver
import pyautogui
import time

def setup():
    chromedriver =  r'C:\Users\ddmin\Downloads\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.desmos.com/calculator")

    pyautogui.moveTo(1235, 25)
    pyautogui.click()

    pyautogui.hotkey('fn', 'f11')
    time.sleep(5)

    clickall()
    

def clickall():
    for y in [200, 270, 340]:
        pyautogui.moveTo(70, y)
        pyautogui.click()


def delete(number):
    
    if number == 1:
        y = 192
    elif number == 2:
        y = 257
    elif number == 3:
        y = 327
    else:
        return False
    
    pyautogui.moveTo(560, y)
    pyautogui.click()

    return True


def screenshot(number, equation):
 
    if number == 1:
        y = 200

    elif number == 2:
        y = 270

    elif number == 3:
        y = 340

    else:
        return False

    clickall()
    
    pyautogui.moveTo(70, y)
    pyautogui.click()

    down = False
    for char in equation:
        if char == '^':
            down = True
        pyautogui.typewrite(char)
        if char == ')' and down == True:
            pyautogui.press('down')
            down = False
            
    time.sleep(1)

    pic = pyautogui.screenshot()

    pic.save('graph.png')

    return True

def show_graph():
    pic = pyautogui.screenshot()
    pic.save('graph.png')
