
import pyautogui
import pyperclip
from utils import leftClick
import time

def fiddlerSaveData(word):
    
    leftClick('./image_folder/fiddler/fiddler.png')
    leftClick('./image_folder/fiddler/clickItem.png')
    pyautogui.hotkey('ctrl','a')
    leftClick('./image_folder/fiddler/file.png')
    leftClick('./image_folder/fiddler/save.png')
    leftClick('./image_folder/fiddler/selected_session.png')
    leftClick('./image_folder/fiddler/text.png')
    
    coords = pyautogui.locateOnScreen('./image_folder/fiddler/filename.png',confidence = 0.8)
    x,y=pyautogui.center(coords)
    x+=50
    pyautogui.click(x,y,button='left',clicks=2,interval=0.2)
    pyperclip.copy(word+'_fiddler.txt')
    pyautogui.hotkey('Ctrl','v')
    pyautogui.press('enter')
    
    coords = pyautogui.locateOnScreen('./image_folder/fiddler/replace.png',confidence = 0.8)
    if coords != None:
        x,y = pyautogui.center(coords)
        pyautogui.click(x,y,button='left')
    
    # im = pyautogui.screenshot()
    # im.save('屏幕截图.png')

def fiddlerClean():
    leftClick('./image_folder/fiddler/x.png',0.1)
    leftClick('./image_folder/fiddler/remove.png')
    
    
    # im = pyautogui.screenshot()
    # im.save('屏幕截图.png')
    