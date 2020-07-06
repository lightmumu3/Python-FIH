# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO
from load_setting_xml import *


def setGPIO_LoadSignal(isLoad):

    GPIO.setwarnings(False)
    BCM_GPIO_4_LOAD_1 = 23
    BCM_GPIO_5_LOAD_2 = 24
    GPIO.setup(BCM_GPIO_4_LOAD_1, GPIO.OUT)
    GPIO.setup(BCM_GPIO_5_LOAD_2, GPIO.OUT)
    GPIO.output(BCM_GPIO_4_LOAD_1,isLoad)
    GPIO.output(BCM_GPIO_5_LOAD_2,isLoad)

def setAlarm_Signal(isAlarm):
    GPIO.setwarnings(False)
    BCM_GPIO_29_ALARM_1 = 21
    GPIO.setup(BCM_GPIO_29_ALARM_1, GPIO.OUT)
    GPIO.output(BCM_GPIO_29_ALARM_1,isAlarm)

def readInputValue():
    BCM_GPIO_7 = 4
    # to use Raspberry Pi board pin numbers 使用板上定義的腳位號碼
    GPIO.setmode(GPIO.BCM)
    # set up pin 4 as an output  將P1接頭的11腳位設定為輸入
    GPIO.setup(BCM_GPIO_7, GPIO.IN)
    # enter while loop unitl exit 隨著時間迴圈會重複執行，直到強制離開
    while True:
        # set up input value as GPIO.11 將P1接頭的11腳位的值設定為inputValue
        inputValue = GPIO.input(BCM_GPIO_7)
        # when user press the btn 如果是真 (玩家按下按鈕)
        last_value = True
        if inputValue == False:
            # show string on screen   顯示被按下
            while inputValue == False:
            #     # Set time interval as 0.3 second delay 設定延遲間隔為零點三秒鐘
                time.sleep(0.5)
                #print("Button pressed")
                globalVal.is_Collected = True
                inputValue = GPIO.input(BCM_GPIO_7)
        else:
            pass
            # print('button not pressed')

def clearGPIO():
    GPIO.cleanup()