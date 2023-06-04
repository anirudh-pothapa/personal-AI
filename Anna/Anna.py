import time
import speech_recognition as sr
import pyttsx3 
#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline.
import datetime
import pywhatkit # library for WhatsApp and YouTube automation. 
import wikipedia 
import pyjokes
import pyautogui
import os 
import sys
import webbrowser
from pyautogui import click
from keyboard import write
from time import sleep
import randfacts
import requests

 #Initialize the engine
engine = pyttsx3.init()

#Set the voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #change index to change voices

#engine.setProperty('voice', voice_id) 
# (with voice_id being an ID of the voice in your system;
# you can grab the list of available voices from engine.getProperty('voices')) 


#Function to  Convert text to speech .
def talk(text):
    #Initialize the engine
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    #Initialize the recognizer
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'anna' in command:
                command = command.replace('anna', '')
                print(command)
                
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        command = ''
    except sr.RequestError:
        print("Sorry, I'm currently unable to process your request. Please try again later.")
        command = ''
        
    return command    

#wishme according to the time of day
def wishme():
    hour = int(datetime.datetime.now().hour) #taking hours from date time 0-24 typecast to integer
    if hour>=0 and hour<12:
        talk("Good Morning!")
        
    elif hour>=12 and hour<18:
        talk("Good Afternoon!")
        
    else:
        talk("Good Night!")
            
    talk("I am Anna")
    talk("How can I help you")    
    
#RESPONDING TO VARIOUS inputs hello, play automation....       
def run_anna():
    command = take_command()
    if 'hello' in command or 'hi' in command:
        talk("hello sir i am anna")
        talk("how may i help you")
        
    elif 'how are you' in command:
        talk("I am great thank you")
        talk('how about you')    
        
    elif 'play' in command:
        talk("ok opening youtube...")
        song = command.replace('play', '')
        talk("playing"+ song)
        pywhatkit.playonyt(song)     #youtube_automation()
        
    elif 'time' in command:          #time
        time = datetime.datetime.now().strftime('%I:%M %p')    
        print(time)
        talk("The time is" + time)
        
    elif 'who is' in command:
        talk("let me get you something")
        person = command.replace('who is', '')
        info = wikipedia.summary(person,sentences=2)
        print(info)
        talk(info) 
      
    elif 'joke' in command:
        talk(pyjokes.get_joke())  
        
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")    
        
     #opening applications   
    elif 'code' in command:
        talk("I am on it..")
        codepath = "C:\\Users\\aniru\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    
    elif 'stopwatch' in command:
        talk("I am on it..")
        codepath = "C:\\Users\\aniru\\OneDrive\\Desktop\\Stopwatch.exe"
        os.startfile(codepath)
    
    elif 'chrome' in command:
        talk("I am on it..")
        codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codepath)
            
    #go to sleep        
    elif 'sleep' in command:
        talk("Thank you for calling me sir, I am going to sleep")
        sys.exit()
        
    #take a screenshot
    elif 'screenshot' in command:
        talk("hold your screen, I am taking a screenshot")    
        name = "screenshot"
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        talk("I am done taking a screen shot, it's saved in main folder")
    
    #surfing on the internet
    elif 'search' in command:
        data = command.replace('search', '') 
        talk("searching" + data)
        pywhatkit.search(data)  

    #opening Instagram
    elif 'insta' in command or 'instagram' in command:
        name = input('name : ')
        webbrowser.open(f"www.instagram.com/{name}")
        talk(f"here is the profile of {name}")
        
    #youtube automation and volume controls
    elif 'volume up' in command:
        talk("increasing the volume by 2 points")
        pyautogui.press("volumeup") 
        
        
    elif 'volume down' in command:
        talk("decreasing the volume by 2 points")
        pyautogui.press("volumedown")        
        
    elif 'mute' in command:
        talk("mute")
        pyautogui.press('m')
      
    elif 'restart' in command:
        talk("restarting")
        pyautogui.press('0')
     
    elif 'skip' in command:
        talk("skipping")
        pyautogui.press('l')        
        
     
    elif 'back' in command:
        talk("back")
        pyautogui.press('j')   
        
    elif 'full screen' in command:
        talk("fullscreen")
        pyautogui.press('f')                 
            
    #closing window          
    elif 'close' in command:
        talk("ok closing the window")
        click(1880,18)
        
                
    #minimising window          
    elif 'mimimise' in command:
        talk("ok minimising the window")
        click(1791,25)
                            
                            
    # #whatsapp automation
    # elif 'whatsapp' in command:
    #     talk("opening whatsapp web")
    #     pywhatkit.search('whatsapp web')
    #     sleep(3)
    #     click(317,414)
    #     sleep(2)
    #     click(219,265) 
    #     talk("who do you want to send a message")
    #     name = take_command()
    #     write(name)
    #     click(219,265)
    #     sleep(1)
    #     click(247,405)
    #     talk("get ready to send a voice message")
    #     sleep(3)
    #     click(1848,963)
    #     sleep(6) #after 6 seconds voice message is ended and sent
    #     click(1848,963)
        
     
     # Automate Video streaming websites   
    elif 'hotstar' in command:
        pywhatkit.search('Disney+hotstar')
        talk("opening hotstar")
        sleep(3)
        click(333,425)
        sleep(2)
        click(71,465)
        sleep(2)
        click(439,222)
        talk("which movie do you want to watch")
        movies = take_command()
        write(movies)
        sleep(3)
        click(275,403)
        sleep(2)
        click(495,944)
        talk("movie is set to play... ")
            
            
    #random facts on internet
    elif 'facts' in command:
        talk("here are some facts")
        a = randfacts.get_fact()        
        b = randfacts.get_fact()      
        c = randfacts.get_fact()      
        d = randfacts.get_fact()      
        e = randfacts.get_fact()    
        
        x = a,b,c,d,e
        facts = ("one","two","three","four","five")     
                                 
        for i in range(len(facts)):
            print(f"fact number {facts[i]}:",x[i])         
            talk(f"fact number {facts[i]},{x[i]}")        
            
            sleep(2)             
            

                
wishme()
while True:
    run_anna()



    
    
    
    

    
 
 
         