from getlongestword import getlongestword
from type_word import type_word
from getword import getword
import pyautogui
import pyperclip
import time


def main():
    alphabet = []
    used = []
    res = ''
    while True:
        # ...
        input('Press enter:')
        # Run your code or call the desired function
        pyautogui.hotkey('alt', 'tab')
        pyautogui.moveTo(731, 563)
        pyautogui.click(clicks=2)
        pyautogui.hotkey('ctrl', 'c')

        # Retrieve the copied text from the clipboard
        copied_text = pyperclip.paste()
        # Assign the copied text to a variable
        s = copied_text
        li = getlongestword(s, used, alphabet)
        if li:
            res = li[0]
            alphabet = list(li[1])
        else:
            li = getword(s, used, alphabet)
            res = li[0]
            alphabet = list(li[1])

        pyautogui.moveTo(693, 955)
        pyautogui.click()
        type_word(res)
        text_to_copy = 'python main.py'
        pyperclip.copy(text_to_copy)


if __name__ == '__main__':
    main()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
