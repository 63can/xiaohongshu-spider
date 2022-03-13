

import yaml

def readConfigFile(file_name = 'config.yaml'):
    # 打开yaml文件
    file = open(file_name, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data,Loader=yaml.FullLoader)
    return data

def writeConfigFile(data,file_name = 'config.yaml'):
    
    file = open(file_name,'w',encoding='utf-8')
    yaml.dump(data,file)
    file.close()


def recordNumber(word,result_number,pointer = None,file_name = 'config.yaml'):
    print('---------------------')
    print(f'正在保存{word}数据...')
    print('---------------------')
    data = readConfigFile(file_name)
    data[word]['now'] = result_number
    if pointer !=None:
        data[word]['pointer'] = pointer
    
    writeConfigFile(data,file_name)
    print('successfully save config.yaml')

    
    
def initialConfig(args,key_word,file_name = 'config.yaml'):
    '''
    判断是否有新键,有的话加上
    '''
    data = readConfigFile()
    
    CHANGE = False
    
    for word in key_word:
        if word not in data.keys():
            data[word] = {
                'now':0,
                'target':args.target,
                'pointer':0
            }
            CHANGE = True
        else:
            if data[word]['target']!=args.target:
                data[word]['target'] = args.target
        
    if CHANGE:
        writeConfigFile(data,file_name)
        print('---------------------')
        print('已重新生成配置文件')
        print('---------------------')
    else:
        print('---------------------')
        print('配置文件正常')
        print('---------------------')
        

def resetConfig(args,key_word,file_name = 'config.yaml'):

    data = {
        'MAX_RETURN_ICON': 20,
        'MAX_VIDEO_ICON': 20,
        'SAVE_FREQUNCY': 20
    }
    for word in key_word:
        data[word] = {
            'now':0,
            'target':args.target,
            'pointer':0
        }
        
    writeConfigFile(data,file_name)
