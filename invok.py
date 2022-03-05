import pyautogui as pg
import keyboard
from time import *
def Ghost_Walk():
    #keyboard.send('q');sleep(0.001); keyboard.send('q+w'); keyboard.send('r')
    keyboard.send('q');sleep(0.1); keyboard.send('q'); sleep(0.1); keyboard.send('w'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def Blast():
    #keyboard.send('q+w+e'); keyboard.send('r')
    keyboard.send('q');sleep(0.1); keyboard.send('w'); sleep(0.1); keyboard.send('e'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def Tornado():
    #keyboard.send('w');sleep(0.001); keyboard.send('w+q'); keyboard.send('r')
    keyboard.send('w');sleep(0.1); keyboard.send('w'); sleep(0.1); keyboard.send('q'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def Meteor():
    #keyboard.send('e');sleep(0.001); keyboard.send('e+w'); keyboard.send('r')
    keyboard.send('e');sleep(0.1); keyboard.send('e'); sleep(0.1); keyboard.send('w'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def Sunstrike():
    keyboard.send('e');sleep(0.1); keyboard.send('e'); sleep(0.1); keyboard.send('e'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def EMP():
    keyboard.send('w');sleep(0.1); keyboard.send('w'); sleep(0.1); keyboard.send('w'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def ColdSnap():
    keyboard.send('q');sleep(0.1); keyboard.send('q'); sleep(0.1); keyboard.send('q'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def IceW():
    keyboard.send('q');sleep(0.1); keyboard.send('q'); sleep(0.1); keyboard.send('e'); sleep(0.1); keyboard.send('r'); sleep(0.1)
def Forge():
    keyboard.send('e');sleep(0.1); keyboard.send('e'); sleep(0.1); keyboard.send('q'); sleep(0.1); keyboard.send('r'); sleep(0.1)
sleep(2)
def Script_Inject():
    pg.alert('Добро пожаловать в Scriptorio 3.0\nЖелаем приятного использования :)')
    while True:
        if keyboard.is_pressed('q'):
            pg.alert('Скрипт активирован')
            while keyboard.is_pressed('-') != True:
                if keyboard.is_pressed('4'):
                    try:
                        Tornado()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('5'):
                    try:
                        Meteor()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('6'):
                    try:
                        Blast()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('7'):
                    try:
                        Ghost_Walk()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('8'):
                    try:
                        Sunstrike()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('1'):
                    try:
                        ColdSnap()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('2'):
                    try:
                        EMP()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('3'):
                    try:
                        IceW()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('0'):
                    try:
                        Forge()
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('m'): pg.alert('скрипт деактивирован'); break
        if keyboard.is_pressed('='): pg.alert('Программа оффнута'); break
Script_Inject()