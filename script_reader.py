import os
import time
import pyautogui
import sys

# reads the script, line by line

def script_go(filename, start_timer, time_cooldown):

    print(f'Programm starts is {start_timer} seconds')
    time.sleep(start_timer)  # start countdown

    count = 0
    with open(filename) as file:
        content = file.readlines()

    for word in content:
        pyautogui.typewrite(word)  # types the word
        pyautogui.press('enter')
        time.sleep(time_cooldown)
        count += 1


script_namew = input("Enter your txt file name: ")
script_name = script_namew + '.txt'

if not os.path.isfile(script_name):
    print(f"{script_namew} doesn't exist")
    sys.exit()

timer = int(input("Enter programm start timer: "))
cooldown = int(input("Enter programm enter cooldown: "))

script_go(script_name, timer, cooldown)
