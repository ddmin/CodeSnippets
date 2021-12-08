from PIL import Image
from PIL import ImageGrab

import pytesseract
from pytesseract import image_to_string

import pyautogui

import re
import time

remove_blemish = lambda s: ''.join([char for char in s if char.isalpha() or char == "'"])

def get_screen(box1, box2):
    x1, y1 = box1
    x2, y2 = box2

    printscreen =  ImageGrab.grab(bbox=(x1,y1,x2,y2))
    return printscreen

def setup():
    pyautogui.click(x=1800, y=700)
    pyautogui.click(x=950, y=770)

def type_words(text):
    for word in text:
        word_fixed = word.lower()
        pyautogui.typewrite(word_fixed + ' ')

def configure_text_boxes():
        print("Place mouse over top left corner of first row and press enter.")
        input()
        box1 = pyautogui.position()

        print("Place mouse over bottom right corner of first row and press enter.")
        input()
        box2 = pyautogui.position()

        print("Place mouse over top left corner of second row and press enter.")
        input()
        box3 = pyautogui.position()

        print("Place mouse over bottom right corner of second row and press enter.")
        input()
        box4 = pyautogui.position()

        return (box1, box2, box3, box4)

def main():
    box1_corner1, box1_corner2, box2_corner1, box2_corner2 = configure_text_boxes()
    setup()

    # Path to tesseract.exe file
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

    img = get_screen(box1_corner1, box1_corner2)

    text = list(map(remove_blemish, image_to_string(img).split()))

    start_time = time.time()
    type_words(text)

    while (time.time() - start_time) < 62:
        img = get_screen(box2_corner1, box2_corner2)
        text = list(map(remove_blemish, image_to_string(img).split()))
        type_words(text)
        time.sleep(0.4)

main()
