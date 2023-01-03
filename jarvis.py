import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests 
import pywhatkit as kit
import smtplib
import sys
import time
import pyautogui
import speedtest
import psutil
import operator
import instaloader
from PyPDF2 import PdfFileReader
from pypdf import PdfReader
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer , QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_jarvisUI
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import pywikihow
# import cv2

engine = pyttsx3.init('sapi5')#api to take voice from user
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)#0-24
    tt = time.strftime("%I:%M %p")
    if(hour>=0 and hour<=12):
        speak(f"Good Morning Ishu,its {tt}")
    elif hour>=12 and hour<=15:
        speak(f"Good Afternoon Ishu,its {tt}")
    else:
        speak(f"Good Evening Ishu,its {tt}")
    speak("I am Jarvis")
    speak("Hope you are doing great, How are you?")
    # speak("Please Tell me how may I help you")

def takeCommand():#It takes microphone input from the user and returns string output
    r = sr.Recognizer()# helps to recognise audio
    #using microphone to listen
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1
        # r.non_speaking_duration = 5
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        # listen microphone for audio

    try:
        print("Recognising...")
        # now using google try to recognise audio get from microphone
        query = r.recognize_google(audio,language = 'en-In')#en-in
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        # speak("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ishumiglani96@gmail.com','I$hui$hu969696')
    server.sendmail('ishumiglani96@gmail.com',to,content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4e938d94c3dd4ab1aba2625e046ef639'
    
    main_page = requests.get(main_url).json()
    print(main_page)
    articles = main_page["articles"]
    head = []
    day = ["first",'second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")

def pdf_reader():
    book = open("spm.pdf","rb")
    pdfReader = PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book are {pages}")
    speak("Sir please enter the page number which you want me to read")
    pg = int(input("enter the page number here : "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def pdfreader():
    speakSpeedChange()
    reader = PdfReader("spm.pdf")
    speak(f"Total number of pages in this book are {len(reader.pages)}")
    speak("Sir please enter the page number which you want me to read")
    pg = int(input("enter the page number here : "))
    page = reader.pages[pg]
    text = page.extract_text()
    print(text)
    speak(text)
    engine.setProperty('rate', 200) # Normal Speed Rate x2

def speakSpeedChange():
    speak("Please select the speed rate for you")
    engine.setProperty('rate', 100) # Decrease the Speed Rate x2
    speak("This is slower speed")
    engine.setProperty('rate', 200) # Normal Speed Rate x2
    speak("This is slower speed")
    engine.setProperty('rate', 250) # Increase the Speed Rate x1.25
    speak("This is faster speed")
    engine.setProperty('rate', 200) 
    speak("which speed would you like me to speakk with, choose 1,2 or 3 and type : ")
    choice = int(input("Enter your speed : "))
    
    match(choice):
        case 1:
            engine.setProperty('rate', 100) 
        case 2:
            engine.setProperty('rate', 200) 
        case 3:
            engine.setProperty('rate', 250) 
        case default:
            speak("Try again and Enter a valid choice ")

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d hours %02d minutes %02d seconds" % (hours, minutes, seconds)

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing task for diff queries
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "great" in query or "fine" in query or "good" in query:
            speak("I wish this will remain always")
        elif "what about you" in query or "how are you" in query:
            speak("Always inspired by you,I am also doing great")
        # to open notepad
        elif "open notepad" in query:
            speak("Ok opening Notepad for you!")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        # to close notepad
        elif "close notepad" in query:
            speak("Okay sir! closing Notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "play music" in query:
            music_dir = 'C:\\Users\\Ishu\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            temp = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[temp]))
            '''
                                   or
                                #    to play mp3 only
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))
            '''
        elif "ip address" in query:
            speak("Finding your Ip")
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}")
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        # elif "search" in query:
        #     speak("What should I search for you?")
        #     cm = takeCommand().lower()
        #     webbrowser.open(f"{cm}")
        elif 'open my mail' in query:
            webbrowser.open("https://gmail.com")
        elif "open trees" in query:
            webbrowser.open("https://www.geeksforgeeks.org/dsa-sheet-by-love-babbar/#BinaryTrees")
        elif "whatsapp to mummy" in query:
            # speak("Enter the no. to which you want to send message")
            no = "+918198984898"
            speak("What message do you want to send to mommy?")
            mess = takeCommand().capitalize()
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            # sec = int(datetime.datetime.now().second)
            kit.sendwhatmsg(no,mess,hour,min+1)
        elif "whatsapp" in query:
            speak("Enter the no. to which you want to send message")
            no = input()
            speak("Enter your message")
            mess = input()
            kit.sendwhatmsg(no,mess,9,22)
        
        elif "play song on youtube" in query:
            speak("Which song would you want to play?")
            cmd = takeCommand().lower()
            kit.playonyt(f"{cmd}")
        elif "lallu" in query:
            speak("Same to you")
        elif "mommy" in query or "mummy" in query:
            speak("Ishu tu bhola hh")
        elif "email" in query:
            try:
                speak("what should I say?")
                content = takeCommand().lower()
                speak("to whom you want to send this email,enter.")
                to = input()
                speak("for review purpose,please confirm the message")
                speak(f"{content}")
                speak("May I send this? Type y for yes and n for No")
                option = input()
                option = option.lower()
                if option == 'y':
                    sendEmail(to,content)
                    speak(f"Email has been sent to {to}")
                else:
                    speak("Ok I will not send this")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am unable to send this email")
        
        elif "weather" in query or "temperature" in query:
            search = "temperature in panipat"
            url = f"https://www.google.com/search?q={search}"
            i = requests.get(url)
            data = BeautifulSoup(i.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")
        
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me about news" in query:
            speak("Ok Sir! fetching your latestnews. Please Wait!")
            news()
        elif "alarm" in query:
            speak("Sir please tell me the time to set alarm, for example set alarm to 5:30 am")
            tt = takeCommand().lower()
            tt = tt.replace("set alarm to ","")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 4:
                music_dir = 'C:\\Users\\Ishu\\Music'
                songs = os.listdir(music_dir)
                temp = random.randint(0,len(songs)-1)
                os.startfile(os.path.join(music_dir,songs[temp]))
        # elif "tell me a joke" in query:
        #     joke = pyjokes.get_joke()
        #     speak(joke)
        elif "shutdown the system" in query:
            os.system("shutdown /s /t s")
        elif "restart the system" in query:
            os.system("shutdown /r /t s")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrproof.dil,SetSuspendState 0,1,0")
        elif "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system has {percentage} percent battery which will remain till {convertTime(battery.secsleft)}")
            charging_status = battery.power_plugged
            if charging_status:
                speak("Our system is connected to power and getting up charged")
            else:
                if(percentage>70):
                    speak("We have enough power to continue work!")
                elif percentage>=40 and percentage<=75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage>=15 and percentage<=30:
                    speak("we do not have enough power to work, please connect to charging")
                elif percentage<=15:
                    speak("We have very low power,please connect to charging the system will shutdown very soon")

######################################################################################################################################
######################################################################################################################################
        elif "find me" in query:
            speak("Wait Sir! let Me Check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()

                city = geo_data['city']

                country = geo_data['country']
                speak("Thnkuu for your Patience Sir!")
                speak(f"I am not so sure, but I think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry Sir I am unable to find due to any technical or network issue")
                pass
######################################################################################################################################
############################To check an Instagram Profile##########################################################################################################
######################################################################################################################################
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Please enter the userName correctly")
            name = input("enter the username here : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            time.sleep(5)
            speak("Sir I like this account's profile picture,may I save it?")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir,profile pic is saved in your main folder.Now I am ready for your next command")
            else:
                speak("Ok Sir! You knows better than me.")
######################################################################################################################################
############################To take a screenshot##########################################################################################################
######################################################################################################################################
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Sir first,please tell me the name for this screenshot fle")
            name = takeCommand().lower()
            speak("Please sir hold the screen for few seconds, I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir,your screenshot is saved in our main folder. Now I am ready for next Command")
######################################################################################################################################
############################To read a pdf##########################################################################################################
######################################################################################################################################
        elif "read pdf" in query:
            pdfreader()
######################################################################################################################################
############################To read a pdf##########################################################################################################
######################################################################################################################################
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("Sir please tell me, you want to hide this folder or make it visible for everyone ? ")
            condition = takeCommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("Sir all the files in this folder are now hidden")
            
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("Sir all the files in this folder are now visible to everyone,I wish you are taking guarntee of this because I am not taking")
            
            elif "leave" in condition:
                speak("Ok Sir!, you are alwways right!")

######################################################################################################################################
############################To read a pdf##########################################################################################################
######################################################################################################################################
        elif "calculation" in query:
            # r = sr.Recognizer()
            # with sr.Microphone as source:
            #     print("Listening...")
            #     r.adjust_for_ambient_noise(source)
            #     audio = r.listen(source)
            
            # my_string = r.recognize_google(audio)
            speak("say what you want to calculate, example 3 plus 3")
            my_string = takeCommand().lower()
            print(my_string)
            try:
                def get_operation_fn(op):
                    myDic =  {
                        '+' : operator.add,
                        'plus' : operator.add,
                        '-' : operator.sub,
                        'minus' : operator.sub,
                        'x' : operator.mul,
                        'multiply' : operator.mul,
                        '/' : operator.__truediv__,
                        'divided by' : operator.__truediv__
                    }
                    return myDic[op]
                def eval_binary_expr(op1,oper,op2):
                    op1,op2 = int(op1) , int(op2)
                    return get_operation_fn(oper)(op1,op2)
                # speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))
            except Exception as e:
                speak("I want you to try first, if unable to solve,then again ask from me.")
        elif "internet speed" in query:
            speak("Ok Sir let me check your speed")
            st = speedtest.Speedtest()
            dl = st.download()
            dl = round(dl / 8e+6,2)

            up = st.upload()
            up = round(up / 8e+6,2)
            speak(f"sir we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
        elif "activate how to do mod" in query:
            speak("how to do mode is activated, please tell me what you want to know")
            while True:
                speak("please tell me what you want to know?")
                how = takeCommand().lower()
                try:   
                    if "yes" in condition:
                        speak("Ok Sir, then please tell me what you want to know?")
                    if "no" in how or 'exit' in how:
                        speak("Ok sir, deactivating how to do mod")
                        break
                    else:
                        max_results = 1
                        how_to = pywikihow.search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak("Here's your recipie")
                        speak(how_to[0].summary)
                    time.sleep(2)
                    speak("Do you want me to search anything else too?")
                except Exception as e:
                    speak("Sorry Sir! I am unable to find this")            
        elif "no thanks" in query or "sleep" in query or "take some resr" in query or "take rest" in query or "no jarvis" in query:
            speak("I am going to sleep! Wake up me whenever you need me")
            # sys.exit()
            break
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "search" in query:
            speak("What should I search for you?")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
        elif "none" == query:
            pass
        else:
            speak("Sir I am unable to recognize what you said, please try again")
        speak("Sir, do you have any other work ?")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        engine.setProperty('rate', 170)
        time.sleep(0.3)
        speak("I hope you all like me and Ishu's Hardwork for creating me")
        time.sleep(0.2)
        speak("We will soon back with more such functionalities in me")
        time.sleep(0.2)
        speak("Till then Please like and comment on our video,if you like and also subscribe our channel for more such amazing innovations")
        time.sleep(0.2)
        speak("Link of the video is mentioned below!")
        time.sleep(0.2)
        speak("Thank You and have a Nice Day!")
        time.sleep(0.2)
        
        # self.TaskExecution()
        # while True:
        #     self.query = takeCommand().lower()
        #     if "wake up" in self.query or "are you there" in self.query or "hello jarvis" in self.query:
        #         TaskExecution()
        #     elif "bye jarvis" in self.query or "bye" in self.query or "good bye jarvis" in self.query:
        #         speak("Good Bye Sir! have a Nice day")
        #         sys.exit()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvasis = Main()
jarvasis.show()
exit(app.exec_())













        # elif "open camera" in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret,img = cap.read()
        #         cv2.imshow('webcam',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        #     cap.release()
        #     cv2.destroyAllWindows()
























