import pyautogui
import time

START_DELAY = int(3) # delay the script when it starts for # seconds
LOAD_TIME = 3.0 # time for reloading the map


def press_for(key, delay):
    pyautogui.keyDown(key)
    time.sleep(delay)
    pyautogui.keyUp(key)

def press_key(key):
    press_for(key, 0.12)

for i in range(START_DELAY):
    time.sleep(1.0)
    print(f'Starting in {START_DELAY-i}')

while True:    
    press_key('g') # open map
    press_key('f') # toggle list
    press_key('e') # select location
    press_key('e') # confirm location
    time.sleep(LOAD_TIME) # wait for loading the area
    pyautogui.keyDown('space') # Run to position
    pyautogui.keyDown('w')
    time.sleep(3.8)
    pyautogui.keyDown('a')
    time.sleep(1.0)
    pyautogui.keyUp('a')
    time.sleep(0.1)
    pyautogui.keyUp('w')
    pyautogui.keyUp('space')
    pyautogui.keyDown('b') # Use skill
    time.sleep(4.0) # Wait for rune generation
    pyautogui.keyUp('b') 
    time.sleep(1.0) # this is included so we have some time between the end of the current loop and the next one. 