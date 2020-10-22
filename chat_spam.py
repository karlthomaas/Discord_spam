import pyautogui
import time


def onewordspam(word, countdown):  #spams only 1 word, with certain cooldown
    while countdown >= 0:
        print(f"You have {countdown} seconds left.")
        countdown -= 1
        time.sleep(1)
    while True:
        for number in range(11):
            pyautogui.typewrite(word)
            pyautogui.press('enter')
        time.sleep(10)
        

# you can choose the word, the word spam amount, time when the program starts and spam cooldown
def spamv2(word, amount, countdown, cooldown): 
    while countdown >= 1:
        print(f"You have {countdown} seconds left.")
        countdown -= 1
        time.sleep(1)

    while amount >= 0:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        amount -= 1
        time.sleep(cooldown)


# you can choose, how high you want to count from the 0

def counting(amount, countdown, cooldown): 
    while countdown >= 0:
        print(f"You have {countdown} seconds left")
        countdown -= 1
        time.sleep(1)
    i = 0
    while i < amount:
        i += 1
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')
        pyautogui.time.sleep(cooldown)


choice = input("Choose following-\n1. OneWordSpam\n2. SpamV2\n3. Counting\n: ").lower()

if choice == '1' or choice == 'onewordspam':
    x = input('Insert a spam word: ')
    y = float(input('Activate the program in: '))

    onewordspam(x, y)

elif choice == '2' or choice == 'spamv2':
    x = input('Insert a spam word: ')
    y = int(input('Times you want to spam it: '))
    f = float(input('Insert enter cooldown: '))
    z = float(input('Activate the program in: '))

    spamv2(x, y, z, f)

elif choice == '3' or choice == 'counting':
    x = float(input('Insert counting end number: '))
    y = float(input('Activate the program in: '))
    f = float(input('Insert Enter cooldown: '))

    counting(x, y, f)
    pass
