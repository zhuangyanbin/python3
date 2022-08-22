#! /usr/bin/python
# -*-coding:utf-8-*-

import re
import time
import pyttsx3
from cnocr import CnOcr
from PIL import ImageGrab

def play_voice(voice_result):
    pp = pyttsx3.init()
    vol=pp.getProperty('volume')
    #pp.setProperty('vol',vol+0.5)

    """语速"""
    rate = pp.getProperty('rate')  # 获取当前语速的详细信息
    #print(rate)  # 打印当前语速
    pp.setProperty('rate', 180)  # 重设语速

    """音量"""
    volume = pp.getProperty('volume')  # 获取当前音量（最小为0，最大为1）
    #print(volume)  # 打印当前音量
    pp.setProperty('volume',volume+ 100.0)  # 在0到1之间重设音量

    """发音"""
    voices = pp.getProperty('voices')  # 获取当前发音的详细信息
    pp.setProperty('voice',voices[0].id) #更改发音参数


    pp.say(voice_result)

    pp.runAndWait()

def product_pic():
    bbox = (0, 0, 1000, 1000)
    im = ImageGrab.grab(bbox)
    TimeName = time.strftime("%Y%m%d%H%M%S", time.localtime())
    pic_name="./pic/"+TimeName+".png"
    im.save(pic_name)
    read_pic(pic_name,TimeName)
    print(TimeName)
def read_pic(pic_name,TimeName):
    print(TimeName)
    print(pic_name)
    # img_fp = pic_name
    ocr = CnOcr()  # 所有参数都使用默认值
    # out = ocr.ocr(pic_name)
    out = ocr.ocr('./pic/66.png')
    list_num = int(len(out))
    print(list_num)
    for i in range(0, list_num):
        txt = str(out[i].get('text'))
        # print(txt)
        # txt = "突然受到，北俱芦洲你长寿郊外"
        if txt[0:4] == "突然受到":
            print(TimeName,txt)
            if re.findall("花果山", txt):
                address = "花果山"
            elif re.findall("北俱芦洲", txt):
                address = "北俱芦洲"
            elif re.findall("长寿郊外", txt):
                address = "长寿郊外"
            elif re.findall("大唐境外", txt):
                address = "大唐境外"
            elif re.findall("江南野外", txt):
                address = "江南野外"
            else:
                print("error")
                address = "null"
            print(address)
            if address == "null":
                voice_result="叮叮叮叮，放叉子了，但是我没看见在哪放的"
            else:
                voice_result="叮叮叮叮"+ address + "放叉子了"
            print(voice_result)
            play_voice(voice_result)
        else:
            continue

def main():
    product_pic()

if __name__=="__main__":
    # while True:
    #     main()
    a=100000000
    for i in range(0,a):
        main()