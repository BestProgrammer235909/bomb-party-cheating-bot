import pyautogui
import time
from random import uniform


def type_word(word):
    if word:
        word = word.lower()
        # pyautogui.hotkey('alt', 'tab')
        # Type the word
        for i in word:
            n = uniform(0.01, 0.05)
            pyautogui.press(i)
            time.sleep(n)
        # Press Enter
        pyautogui.press('enter')
        pyautogui.hotkey('alt', 'tab')
        return
