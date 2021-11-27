'''
Basic command line app that allows user to input any number of YouTube/Soundcloud urls
and desired wait time in hours:minutes:seconds.
When timer reaches zero, a random url will be selected from the list and opened.
'''
import os
import time
import webbrowser
import random

song_list = []

def choose_songs():
    number_of_songs = int(input('Enter desired number of songs: '))
    while number_of_songs > 0:
        song_list.append(input('Please paste song url here: '))
        number_of_songs -= 1

def play_random_song():
    return song_list[random.randint(0,len(song_list) - 1)]

choose_songs()

hours = int(input('Please enter the desired number of hours: '))
minutes = int(input('Please enter the desired number of minutes: '))
seconds = int(input('Please enter the desired number of seconds: '))

start = input('Enter "R" to start timer.')

while start.lower() == 'r':
    if seconds == 0:
        seconds = 60 
        minutes -= 1
    if minutes < 0:
        minutes = 59
        hours -= 1
    os.system('cls')
    seconds -= 1
    print(hours, ':', minutes, ':', seconds)
    time.sleep(1)
    if hours == 0 and minutes == 0 and seconds == 0:
        break

webbrowser.open(play_random_song())