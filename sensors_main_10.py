import RPi.GPIO as GPIO
from pygame import mixer
import pygame
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor1 = 7
sensor2 = 11
sensor3 = 12
sensor4 = 13
sensor5 = 15
sensor6 = 16
sensor7 = 18
sensor8 = 19
sensor9 = 21
sensor10 = 23


led1 = 24
led2 = 26
led3 = 29
led4 = 31
led5 = 32
led6 = 33
led7 = 35
led8 = 36
led9 = 37
led10 = 38

GPIO.setup(sensor1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor5, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor6, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor7, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor8, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor9, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor10, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)
GPIO.setup(led7, GPIO.OUT)
GPIO.setup(led8, GPIO.OUT)
GPIO.setup(led9, GPIO.OUT)
GPIO.setup(led10, GPIO.OUT)


sen_sel = 0
retriggered_sensor = 0
playing = 0
current_time = 0
sensor_retrigger_time = 0


mixer.init()

def sensor_1():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('01_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led1, 1)
        sen_sel = 1

    elif(playing == 0):
        mixer.music.load('01_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led1, 1)
        playing = 1
        sen_sel = 1

        
def sensor_2():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('02_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led2, 1)
        sen_sel = 2

    elif(playing == 0):
        mixer.music.load('02_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led2, 1)
        playing = 1
        sen_sel = 2


def sensor_3():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('03_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led3, 1)
        sen_sel = 3

    elif(playing == 0):
        mixer.music.load('03_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led3, 1)
        playing = 1
        sen_sel = 3


def sensor_4():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('04_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led4, 1)
        sen_sel = 4

    elif(playing == 0):
        mixer.music.load('04_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led4, 1)
        playing = 1
        sen_sel = 4

def sensor_5():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('05_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led5, 1)
        sen_sel = 5

    elif(playing == 0):
        mixer.music.load('05_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led5, 1)
        playing = 1
        sen_sel = 5

def sensor_6():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('06_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led6, 1)
        sen_sel = 6

    elif(playing == 0):
        mixer.music.load('06_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led6, 1)
        playing = 1
        sen_sel = 6

def sensor_7():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('07_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led7, 1)
        sen_sel = 7

    elif(playing == 0):
        mixer.music.load('07_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led7, 1)
        playing = 1
        sen_sel = 7

def sensor_8():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('08_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led8, 1)
        sen_sel = 8

    elif(playing == 0):
        mixer.music.load('08_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led8, 1)
        playing = 1
        sen_sel = 8

def sensor_9():

    global sen_sel
    global playing
    global current_time
    mixer.init()
    pygame.init()

    current_time = pygame.time.get_ticks()/1000

    if(playing != 0):
        mixer.music.stop()
        switch(11)
        mixer.music.load('09_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led9, 1)
        sen_sel = 9

    elif(playing == 0):
        mixer.music.load('09_eng.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led9, 1)
        playing = 1
        sen_sel = 9


def led_off():
        GPIO.output(led1, 0)
        GPIO.output(led2, 0)
        GPIO.output(led3, 0)
        GPIO.output(led4, 0)
        GPIO.output(led5, 0)
        GPIO.output(led6, 0)
        GPIO.output(led7, 0)
        GPIO.output(led8, 0)
        GPIO.output(led9, 0)
        GPIO.output(led10, 0)
        

    
def retrigger_and_stop():
    global sen_sel
    global playing
    global current_time
    global sensor_retrigger_time
    global retriggered_sensor

    pygame.init()
    mixer.init()

    sensor_retrigger_time = pygame.time.get_ticks()/1000
    if(sensor_retrigger_time - current_time > 10):
        mixer.music.stop()
        switch(11)
        time.sleep(1)

def default():
    return "No Sensor Active!!!"

switcher = {
    1: sensor_1,
    2: sensor_2,
    3: sensor_3,
    4: sensor_4,
    5: sensor_5,
    6: sensor_6,
    7: sensor_7,
    8: sensor_8,
    9: sensor_9,
    10: retrigger_and_stop,
    11: led_off,
    }

def switch(val):
    return switcher.get(val, default)()

while True:
    if(GPIO.input(sensor1) == 1):
        if(sen_sel != 1):
            switch(1)
        elif(sen_sel==1):
            switch(10)
            
    elif(GPIO.input(sensor2) == 1):
        if(sen_sel != 2):
            switch(2)
        elif(sen_sel==2):
            switch(10)    

    elif(GPIO.input(sensor3) == 1):
        if(sen_sel != 3):
            switch(3)
        elif(sen_sel==3):
            switch(10)    

    elif(GPIO.input(sensor4) == 1):
        if(sen_sel != 4):
            switch(4)
        elif(sen_sel==4):
            switch(10)

    elif(GPIO.input(sensor5) == 1):
        if(sen_sel != 5):
            switch(5)
        elif(sen_sel==5):
            switch(10)

    elif(GPIO.input(sensor6) == 1):
        if(sen_sel != 6):
            switch(6)
        elif(sen_sel==6):
            switch(10)
            
    elif(GPIO.input(sensor7) == 1):
        if(sen_sel != 7):
            switch(7)
        elif(sen_sel==7):
            switch(10)
            
    elif(GPIO.input(sensor8) == 1):
        if(sen_sel != 8):
            switch(8)
        elif(sen_sel==8):
            switch(10)
            
    elif(GPIO.input(sensor9) == 1):
        if(sen_sel != 9):
            switch(9)
        elif(sen_sel==9):
            switch(10)



    while(mixer.music.get_busy() == False):
        sen_sel = 0
        playing = 0
        switch(11)
        break
