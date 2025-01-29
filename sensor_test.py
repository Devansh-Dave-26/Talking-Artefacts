import RPi.GPIO as GPIO
from pygame import mixer
import pygame
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led = 24
sensor = 21

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

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
        GPIO.output(led, 0)
        print("LED OFF")
        mixer.music.load('1_audio.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led, 1)
        print("LED ON")
        sen_sel = 1

    elif(playing == 0):
        mixer.music.load('1_audio.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()
        GPIO.output(led, 1)
        print("LED ON")
        playing = 1
        sen_sel = 1


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
        GPIO.output(led, 0)
        print("LED OFF")
        time.sleep(1)


def default():
    return "No Sensor Active!!!"

switcher = {
    1: sensor_1,
    2: retrigger_and_stop,

    }

def switch(val):
    return switcher.get(val, default)()

while True:
    print(GPIO.input(sensor))
    if(GPIO.input(sensor) == 1):
        if(sen_sel != 1):
            switch(1)
        elif(sen_sel==1):
            switch(2)

    while(mixer.music.get_busy() == False):
        sen_sel = 0
        playing = 0
        GPIO.output(led, 0)
        break
