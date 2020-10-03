#------------------------------------------- Healthy Programmer ------------------------------------
'''
9am - 5 pm must to drink water (3.5 litres)
Water:- water.mp3(3.5 litres drink water/every 40 minutes)    -(user need to type then after mp3 player stop) Drank -log
Eyes:- eyes.mp3(every 30 minutes exercise) - (user need to type then after mp3 player stop) EyDone
Physical activity:- physical.mp3(every 45 minutes) - (user need to type then after mp3 player stop) ExDone

rule :- pygame module use for play audio
'''
'''
import time
import pygame

def playMusic(file):
    print(file)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def isOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '17:00:00':
        return True
    else:
        return False

NumOfWaterRemaining = 18

WaterAfterEvery = 1200 #SECONDS -20 minutes
EyeExerciseAfterEvery = 1800 #seconds - 30 minutes
PhysicalExercieAfterEvery = 2700 #seconds - 45 minutes

waterMp3 = 'water.mp3'
eyesMp3 = 'eyes.mp3'
physicalMp3 = 'physical.mp3'

currenttime = time.strftime('%H:%M:%S') #hour:minute:second
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()

SleepTime = 60
'''
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):     #file argument is define file, when we write stopper then music will stop.
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_new(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")        #if we want to stop those sound then write stop
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 5
    eyesecs = 20
    exsecs = 10

    while True:
        if time() - init_water > watersecs:
            print("Water drinking time.Enter 'drank' to stop alarm")
            musiconloop('water.mp3','drank') #when we write drank then stop music.
            init_water = time()
            log_new("Drank water at")

        if time() - init_eyes > eyesecs:
            print("Eyes exercise time.Enter 'doneeyes' to stop alarm")
            musiconloop('eye.mp3','doneeyes') #when we write drank then stop music.
            init_eyes = time()
            log_new("eyes relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical activity time.Enter 'donephy' to stop alarm")
            musiconloop('exercise.mp3','donephy') #when we write drank then stop music.
            init_exercise = time()
            log_new("Physical Activity at")