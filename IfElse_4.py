from datetime import datetime
import os, random, easygui

helloIntent = ['hi','hey','hello','howdy','hello there','hi there']
timeIntent = ["current time","time please","what's the time","tell me time","time"]
dateIntent = ["today's date","date please","what's the date","tell me date","date"]
musicIntent = ['play music','start music','play a song','start a song']

# Identity Operators  - in, not in
chat = True
while chat:
    msg = input("Enter your message: ")
    if msg in helloIntent:
        print('Hello User')
    elif msg in timeIntent:
        current_time = datetime.now().time()
        print(current_time.strftime('%H:%M:%S %p'))
    elif msg in dateIntent:
        current_date = datetime.now().date()
        print(current_date.strftime('%d/%m/%y %a'))
    elif msg in musicIntent:
        # path = 'C:/Users/asus/Music'
        # os.chdir(path)
        # songs = os.listdir()
        # s = random.choice(songs)
        path = easygui.fileopenbox()
        os.startfile(path)
    elif msg == 'show songs':
        path = 'C:/Users/asus/Music'
        os.chdir(path)
        songs = os.listdir()
        for index,songName in enumerate(songs, start=1):
            print(index, songName)
        songNumber = int(input("Enter number of song you want to play : "))
        os.startfile(songs[songNumber - 1])
    elif msg == 'bye':
        print('Bye User')
        chat = False
    else:
        print("I donot understand")