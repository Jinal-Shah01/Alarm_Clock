"""

@author Jinal Shah

Alarm Clock

"""
import datetime
import time
import pygame

# Initializing the pygame
pygame.init()

alarm_time = input("Alarm Time(Don't put AM or PM yet!): ")
am_pm = input("AM or PM? ")

alarm_time_array = alarm_time.split(":")

if am_pm == "PM":
    hour = str(12+12-(12-int(alarm_time_array[0])))
else:
    hour = str(alarm_time_array[0])

minute = str(alarm_time_array[1])

current_datetime = datetime.datetime.now().__str__()
current_datetime_array = current_datetime.split(" ")
current_time_array = current_datetime_array[1].split(":")


while hour != current_time_array[0] or minute != current_time_array[1]:
    time.sleep(30)
    current_datetime = datetime.datetime.now().__str__()
    current_datetime_array = current_datetime.split(" ")
    current_time_array = current_datetime_array[1].split(":")

pygame.mixer.music.load('/Users/jinalshah/PycharmProjects/Python_Class_Projects/Project 3/Alarm.mp3')
pygame.mixer.music.play(loops=5)
time.sleep(10)
