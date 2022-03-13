
from itertools import chain
from sympy import content
from xpinyin import Pinyin as p
import pyautogui
import os
import time
import csv

def checkMatch(coords, picName = ''):
    
    if coords == None:
        #print(f"找不到图片{picName}")
        return True
    
    else: return False
    
    

def findKeyboardInput(word):
    keyboardInput = p().get_pinyin(word,'')
    return keyboardInput
    
    

def checkVideo(ignore_items,x,y,nav_y):
    '''
    跳过视频,不获取小红书中的视频,只要文章,视频会使寻找退出按钮的图像不易定位
    '''
    if y-nav_y<350:
        return True
    for i,j in ignore_items:
        if abs(i-x)<=100 and y-j>0 and y-j<350:
            return True
        
    return False
#findKeyboardInput("代餐")

def getVideoIcon(cfg):
    
    video_icon = []
    MAX_VIDEO_ICON = cfg['MAX_VIDEO_ICON']
    for i in range(1,MAX_VIDEO_ICON):
        if os.path.exists(f'./image_folder/video{i}.png'):
            video_icon.append(pyautogui.locateAllOnScreen(f'./image_folder/video{i}.png',confidence = 0.6))
        else:
            break
        
    video_icon = chain(*video_icon)
    return video_icon

def getVideoReturnIcon(cfg):
    
    video_return = []
    
    MAX_RETURN_ICON = cfg['MAX_RETURN_ICON']
    for i in range(1,MAX_RETURN_ICON):
        if os.path.exists(f'./image_folder/video_return/return{i}.png'):
            video_return.append(pyautogui.locateAllOnScreen(f'./image_folder/video_return/return{i}.png',confidence = 0.6))
        else:
            break
    
    video_return = chain(*video_return)
    return video_return
        
        

def checkDistance(nav_y,y):
    
    if y-nav_y<100:
        return True
    else:
        return False
    
def checkVideoReturn():
    coords = pyautogui.locateOnScreen('./image_folder/search.png',confidence = 0.8)
    return not checkMatch(coords)


def leftClick(image_name,interval=0.5):
    coords = pyautogui.locateOnScreen(image_name,confidence = 0.8)
    if checkMatch(coords):exit(0)
    x,y=pyautogui.center(coords)
    pyautogui.click(x,y,button='left')
    time.sleep(interval)
    
def saveArticles(word,articles):
    
    # txt
    txt_file = open(f'./result/{word}文章内容.txt','w',encoding='utf-8')
    csv_file = open(f'./result/{word}文章内容.csv','w',encoding='utf-8',newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["url","content"])
    
    for data in articles:
        #txt_file.write(data['url']+'\n')
        txt_file.write(data['content']+'\n')
        csv_writer.writerow([data['url'],data['content']])
    
    txt_file.close()
    csv_file.close()
    
    print(f'./result/{word}文章内容.csv 成功保存')
    print(f'./result/{word}文章内容.txt 成功保存')
    
    