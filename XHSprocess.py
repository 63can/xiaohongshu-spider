
import pyautogui
import pyperclip

import time
from config import recordNumber


from utils import checkDistance, checkMatch, checkVideo, checkVideoReturn,findKeyboardInput, getVideoIcon, getVideoReturnIcon


def XHS_browse(cfg,word):
    '''
    小红书进程,依次点击心形,让fiddler代理捕获
    '''
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    
    #confidence 置信度
    coords = pyautogui.locateOnScreen('./image_folder/icon.png',confidence = 0.8)
    
    if checkMatch(coords):exit(0)
    #获取定位到的图中间点坐标
    x,y=pyautogui.center(coords)
    pyautogui.click(x,y,button='left')
    
    return_icon = pyautogui.locateOnScreen('./image_folder/return.png',confidence = 0.8)
    if return_icon!=None:
        return_icon_x,return_icon_y=pyautogui.center(return_icon)
        pyautogui.click(return_icon_x,return_icon_y,button='left')
    
    coords = pyautogui.locateOnScreen('./image_folder/search.png',confidence = 0.8)
    if checkMatch(coords):exit(0)
    
    x,nav_y=pyautogui.center(coords)
    x +=50
    pyautogui.click(x,nav_y,button='left',clicks=2,interval=0.3)
    pyautogui.hotkey('ctrl','a')
    
    #keyboardInput = findKeyboardInput(word)
    #pyautogui.typewrite(keyboardInput)
    pyperclip.copy(word)
    pyautogui.hotkey('Ctrl','v')
    pyautogui.press('enter')
    
    time.sleep(2)
    coords = pyautogui.locateOnScreen('./image_folder/comprehensive_ranking.png',confidence = 0.8)
    x,y=pyautogui.center(coords)
    pyautogui.click(x,y,button='left')
    time.sleep(0.2)
    coords = pyautogui.locateOnScreen('./image_folder/comprehensive_ranking_select.png',confidence = 0.8)
    x,y=pyautogui.center(coords)
    pyautogui.click(x,y,button='left')
    
    time.sleep(0.5)
    
    MAX_RESULT = cfg[word]['target']+5
    result_num = cfg[word]['now']
    pointer = cfg[word]['pointer']
    
    return_icon = pyautogui.locateOnScreen('./image_folder/return.png',confidence = 0.8)
    return_icon_x,return_icon_y=pyautogui.center(return_icon)
    while(result_num<MAX_RESULT):
        if result_num >= cfg['SAVE_FREQUNCY']*pointer:
            recordNumber(word,result_num,pointer)
            pointer+=1
            
        coords = pyautogui.locateAllOnScreen('./image_folder/like.png',confidence = 0.8)
        
        # video_icon = getVideoIcon()

        # ignore_items = []
        # for pos in video_icon:
        #     x,y = pyautogui.center(pos)
        #     ignore_items.append([x,y])
        roll_distance = -20
        for pos in coords:
            roll_distance = max(int(pos[1])-int(nav_y),roll_distance)
            x,y = pyautogui.center(pos)
            # if checkVideo(ignore_items,x,y,nav_y):
            #     #print('已跳过')
            #     continue
            if checkDistance(nav_y,y):
                continue
            pyautogui.click(x,y,button='left')
            time.sleep(1)
            
            
            # if checkMatch(return_icon):
            #     return_icon = getVideoReturnIcon(cfg)
            #     for id,t in enumerate(return_icon):
            #         return_icon_x,return_icon_y=pyautogui.center(t)
            #         pyautogui.click(return_icon_x,return_icon_y,button='left')
            #         time.sleep(1)
            #         pyautogui.moveTo(return_icon_x+50,return_icon_y+50)
            #         if checkVideoReturn():
            #             #print('successfully return from video')
            #             break
            #         else:
            #             print(f'test return icon{id}')
                     
                        
            # else:
            #     return_icon_x,return_icon_y=pyautogui.center(return_icon)
            #     pyautogui.click(return_icon_x,return_icon_y,button='left')
            #     time.sleep(1)
            pyautogui.click(return_icon_x,return_icon_y,button='left')
            result_num+=1
            #print(result_num)
        #print('start to roll')
        pyautogui.scroll(-roll_distance)
        time.sleep(0.5)
        
    recordNumber(word,result_num)
        
        
def XHS_keep_browse(cfg,word):
    
    MAX_RESULT = cfg[word]['target']
    result_num = cfg[word]['now']
    
    if result_num>=MAX_RESULT :
        print('---------------------')
        print(f'{word} 已满足')
        print('---------------------')
        return 1
    
    MAX_RESULT+=5
    pointer = cfg[word]['pointer']
    
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    
    coords = pyautogui.locateOnScreen('./image_folder/icon.png',confidence = 0.8)
    
    if checkMatch(coords):exit(0)
    #获取定位到的图中间点坐标
    x,y=pyautogui.center(coords)
    pyautogui.click(x,y,button='left')
    
    return_icon = pyautogui.locateOnScreen('./image_folder/return.png',confidence = 0.8)
    return_icon_x,return_icon_y=pyautogui.center(return_icon)
    
    coords = pyautogui.locateOnScreen('./image_folder/search.png',confidence = 0.8)
    if checkMatch(coords):exit(0)
    
    x,nav_y=pyautogui.center(coords)
    
    
    while(result_num<MAX_RESULT):
        if result_num >= cfg['SAVE_FREQUNCY']*pointer:

            recordNumber(word,result_num,pointer)
            pointer+=1
        coords = pyautogui.locateAllOnScreen('./image_folder/like.png',confidence = 0.8)
        
        # video_icon = getVideoIcon()

        # ignore_items = []
        # for pos in video_icon:
        #     x,y = pyautogui.center(pos)
        #     ignore_items.append([x,y])
        
        roll_distance = 100
        for pos in coords:
            roll_distance = max(int(pos[1])-int(nav_y),roll_distance)
            x,y = pyautogui.center(pos)
            # if checkVideo(ignore_items,x,y,nav_y):
            #     #print('已跳过')
            #     continue
            if checkDistance(nav_y,y):
                continue
            pyautogui.click(x,y,button='left')
            time.sleep(1)
            
            
            # if checkMatch(return_icon):
            #     return_icon = getVideoReturnIcon(cfg)
            #     for id,t in enumerate(return_icon):
            #         return_icon_x,return_icon_y=pyautogui.center(t)
            #         pyautogui.click(return_icon_x,return_icon_y,button='left')
            #         time.sleep(0.5)
            #         pyautogui.moveTo(return_icon_x+50,return_icon_y+50)
            #         if checkVideoReturn():
            #             #print('successfully return from video')
            #             break
            #         else:
            #             print(f'test return icon{id}')
                     
                        
            # else:
            #     return_icon_x,return_icon_y=pyautogui.center(return_icon)
            pyautogui.click(return_icon_x,return_icon_y,button='left')
            time.sleep(1)
            result_num+=1
            #print(result_num)
        #print('start to roll')
        pyautogui.scroll(-roll_distance)
        time.sleep(0.5)
    
    recordNumber(word,result_num)
    return 0
    
    
    
    
    
    
    
    

