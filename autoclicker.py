import mouse
import keyboard
import time
import os
import asyncio

def start():
    global work
    work = True
    print('Autoclicker on')

def stop():
    global work
    work = False
    print('Autoclicker off')

time_ = 0

def run_autoclicker():
    while True:
        if work:
            mouse.click('left')
            time.sleep(time_)
            
def main_menu():
    global time_
    print('Autoclicker\n\tby Angel')
    time.sleep(3)
    clear()
    print(f'Autoclicker\n\nStart: `\nStop: Shift+`\nSpeed: {time_}\n\n')
    for x in range(1):
        time_ = input('Enter speed: ')
        print(f'Speed: {time_}')
        time_ = float(time_)
        run_autoclicker()

work = False

keyboard.add_hotkey('`', start)
keyboard.add_hotkey('shift+`', stop)

clear = lambda: os.system('cls')

if __name__ == '__main__':
    main_menu()