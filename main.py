

from config import initialConfig, readConfigFile, resetConfig
from XHSprocess import XHS_browse, XHS_keep_browse
import argparse

from fiddler_process import fiddlerClean, fiddlerSaveData
from selenium_process import getXHScontent
from utils import leftClick, saveArticles


def main(args):
      
    key_word = args.key_word

    if args.reset:
        resetConfig(args,key_word,args.config)
        print('配置文件已重置')
        return 
    
    initialConfig(args,key_word)
    cfg = readConfigFile(args.config)
    
    if args.keep:
        for word in key_word:
            if XHS_keep_browse(cfg,word)==0:
                print(f'小红书数据采集完成{word}')
                fiddlerSaveData(word)
                print(f'fiddler数据导出完成')
                fiddlerClean()
                
                # 返回代码编辑器,以便程序输出信息查看
                # 如果不是vscode,请截取你的底部导航栏的代码编辑器(如pycharm)的截图,并替换(./image_folder/codeIDE.png)
                leftClick('./image_folder/codeIDE.png')
                articles = getXHScontent(word)
                saveArticles(word,articles)
    
    for word in key_word:
        XHS_browse(cfg,word)
        print(f'小红书数据采集完成{word}')
        fiddlerSaveData(word)
        print(f'fiddler数据导出完成')
        fiddlerClean()
        
        # 返回代码编辑器,以便程序输出信息查看
        # 如果不是vscode,请截取你的底部导航栏的代码编辑器(如pycharm)的截图,并替换(./image_folder/codeIDE.png)
        leftClick('./image_folder/codeIDE.png')
        articles = getXHScontent(word)
        saveArticles(word,articles)
        
    print('All jobs have been finished!')
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # 中断之后继续执行
    parser.add_argument("--keep",action='store_true')
    # 按当前关键字参数重置配置文件信息，配置信息初始化,不会执行程序
    parser.add_argument('--reset',action='store_true')
    # 关键字 | 多参数
    parser.add_argument('key_word',  metavar='N', type=str, nargs='*',default=['藕粉','养生','代餐'])
    # 采集数量 
    # 微信小程序小红书最大100,请勿调大，可以调小
    parser.add_argument('--target',default=100,type=int)
    # 配置文件位置 | 程序会主动检查,如需重置内容可使用--reset指令
    parser.add_argument('--config',default='config.yaml',type=str)

    args = parser.parse_args()
    main(args)
    