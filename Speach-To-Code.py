#######################
# Import Dependencies #
#######################
import os, time, pyttsx3
import datetime, platform
import speech_recognition as sp









##################
# BG Color Class #
##################
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

### Restircting To Only Run In Windows ###
if platform.system() == "Windows":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    userSaid = "hello world"

else:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 160)
    userSaid = "hello world"

### Wishing Function ###
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")
    
## Speak Function ##
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



## Listening Function ##
def take_command(wtr=0):
    r = sp.Recognizer()
    r.pause_threshold = 1
    r.operation_timeout = 5
    with sp.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...\n")
            heard = r.recognize_google(audio)
            print(f"You Said: \"{heard}\"")
            return heard.lower()
        
        except sp.UnknownValueError:
            speak("I Didn't Understood What You Said... :(")
            print("You said something that is beyond my understanding or maybe you didn't say anything.\n")
        engine.runAndWait()
        return 0


## Instruction Function ##
def instructions():
    print("Getting started without wasting your precious time...")
    speak("Welcome to Speach To Code <HTML EDITION>, version 1.0, created by  Artin Zafari, Getting started without wasting your precious time.")


## ScilenceChecker Function Takes input and removes scilence ##
def scilenceChecker():
	userSaid = take_command().lower()
	if userSaid == "":
		userSaid = "nothing"
	elif userSaid == " ":
		userSaid = "nothing"
	else:
		userSaid = take_command().lower()


def clear_log():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("Clear")


creditsScreen = '''
 _____ _                 _          _____            _   _     _
|_   _| |__   __ _ _ __ | | _____  |  ___|__  _ __  | | | |___(_)_ __   __ _
  | | | '_ \ / _` | '_ \| |/ / __| | |_ / _ \| '__| | | | / __| | '_ \ / _` |
  | | | | | | (_| | | | |   <\__ \ |  _| (_) | |    | |_| \__ \ | | | | (_| |
  |_| |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|     \___/|___/_|_| |_|\__, |
                                                                       |___/
CREDIT:
Artin Zafari
'''
clear_log()

welcomeSplashScreen = '''

---------------------------------------------------------------------------			
		   ***
		  **/**
		 **/||**	| J A R V I S - SPEACH-To-Code  <HTML EDITION>
		 **||/**	| ---------------------------------------
		  **/**		| A R T I N   Z A F A R I
 		   ***
---------------------------------------------------------------------------	            
	
'''
clear_log()

print(f"{Bcolors.OKCYAN + welcomeSplashScreen + Bcolors.ENDC}")


if __name__ == "__main__":
    instructions()
    WishMe()
    looper = 5

    while looper != 10:
        query = str(take_command())

        ## Probability Of Commands ##
        if "open notepad" in query:
            command = "C:\\Windows\\System32\\notepad.exe"
            os.system(command)
        
        elif "open browser" in query:
            command = "start https://www.google.com"
            os.system(command)
        
        elif "clear log" in query:
            clear_log()
        
        elif "pause" in query:
            a = input("Press Any Key To Continue...")
        
        elif "add address" in query:
            speak("Adding Your Address, Tell Me Your Address")
            address = input("Please Type Your Address: ")
            finalTag = (f"<address>{address}</address>")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Address Added!\n")
            speak("Address Added!")

        elif "add attribute" in query:
            speak("Adding Your Attribute")
            print("Type In Your URL.")
            URL = input("Type Your URL Address Here: ")
            URLName = input("Enter The Title Of Your URL")
            finalTag = (f'<a href="{URL}">{URLName}</a>')
            f = open("index,html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Attribute/URL Added!\n")
            speak("Attribute/URL Added!")

        elif "add audio" in query:
            speak("Adding Your Audio")
            print("Type In The Path Of Your Audio")
            audio_path = input("Type The Path Of Your Audio Here: ")
            finalTag = (f'<audio controls autoplay><source src="{audio_path}" type="audio/mpeg"></audio>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Audio Added!\n")
            speak("Audio Added!")

        elif "add blockquote" in query:
            speak("Adding Your Blockquote, Tell Me Your Blockquote Content")
            print("Say Your Blockquote Content: ")
            query = str(take_command())
            block_quote = query
            finalTag = (f'<blockquote>{block_quote}</blockquote>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Blockquote Added\n")
            speak("Blockquote Added")

        elif "add br" in query:
            speak("adding your br tag")
            finalTag = (f"<br>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("br added!\n")
            speak("br added!")


        elif "add button" in query:
            speak("adding your Button")
            buttonName = input("Enter your Button name: ")
            finalTag = (f'<button type="button">{buttonName}</button>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Attribute/URL added!\n")
            speak("Attribute/URL added!")

        elif "add comment" in query:
            speak("adding your comment, Tell me your comment")
            print("Say your comment: ")
            query = str(take_command())
            comment = query
            finalTag = (f"<!--{comment}-->\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Comment added!\n")
            speak("Comment added!")


        elif "add heading" in query:
            speak("adding your heading, Tell me your heading Size")
            print("Say your heading size: ")
            query = str(take_command())
            sizeOfHeadingTag = query
            sizeOfHeadingTag = input("Enter size of Heading Tag(1, 2 ,3 ,4...): ")
            contentOfHeading = input("Enter content of Heading: ")
            speak("Adding your heading, Tell me your heading content")
            print("Say your heading content: ")
            query = str(take_command())
            contentOfHeading = query
            finalTag = (f"<h{sizeOfHeadingTag}>{contentOfHeading}</h{sizeOfHeadingTag}>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Heading added!\n")
            speak("Heading added!")


        elif "add text" in query:
            speak("adding your text in a paragraph")
            print("Adding Your text in a paragraph!")
            query = str(take_command())
            text = query
            finalTag = (f'<p>{text}</p>')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("Text Added\n")
            speak("Text Added")
         

        elif "add hr" in query:
            speak("adding your hr tag")
            finalTag = (f"<hr>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("hr added!\n")
            speak("hr added!")

        elif "add iframe" in query:
            speak("adding your iframe tag")
            width = input("Enter Width of your ifame in pixels: ")
            height = input("Enter height of your ifame in pixels: ")
            url = input("paste/enter url for iframe: ")
            finalTag = (f"<iframe src=\"{url}\" width=\"{width}px\" height=\"{height}px\"></iframe>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("iframe added!\n")
            speak("iframe added!")
           

        elif "add image" in query:
            speak("adding your image tag")
            image_name = input("Enter name of your image: ")
            width = input("Enter Width of your image in pixels: ")
            height = input("Enter height of your image in pixels: ")
            url = input("paste/enter url for image with extension: ")
            finalTag = (f"<img src=\"{url}\" width=\"{width}px\" height=\"{height}px\" alt=\"{image_name}\">\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("image added!\n")
            speak("image added!")

        elif "exit" in query:
            speak("See You Next Time")
            exit()
        
        elif "time" in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M:%S")
            print(f"Current Time: {current_time} (Hours,Minutes,Seconds)")
        
        elif "who are you" in query:
            print("Hello There!, My Name Is Jarvis Im Here To Help You Create Your HTML Document.\n")
            speak("Hello There!, My Name Is Jarvis Im Here To Help You Create Your HTML Document.")
        
        elif "why are you helping me" in query:
            print("Well, Because I Want To Help You Acheive Your Best, And To make html easy for you!\n")
            speak("Well, Because I Want To Help You Acheive Your Best, And To make html easy for you!")
        
        elif "why are you gay" in query:
            print("You Are Gay .|.\n")
            speak("im not gay, you are gay")

        elif "how old are you" in query:
            yr_of_birth = 2022
            m_of_birth = 7
            d_of_birth = 29
            # now = datetime.datetime.now()
            cr_yr = datetime.datetime.now().year
            cr_month = datetime.datetime.now().month
            cr_day = datetime.datetime.now().day
            cr_age_yr = cr_yr - yr_of_birth
            cr_age_month = cr_month - m_of_birth
            cr_age_day = cr_day - d_of_birth
            print(f"Im {cr_age_yr} years and {cr_age_month} months {cr_age_day} days old\n")
            speak(f"Im {cr_age_yr} years, And {cr_age_month} Months ,And {cr_age_day} Days Old.")
            

        # elif "add list" in query:
        # 	speak("adding your list tag (Unordered list)")
        # 	noofitems = input("Enter number of items in your list: ")
        # 	finalTag = (f"<ul>\n")
        # 	f = open("index.html", "a")
        # 	f.write(finalTag)
        # 	for i in noofitems:
        # 		user_item_input = input("Enter your item: ")
        # 		finalTag = (f"<li>{list_items}</li>\n")
        # 		f = open("index.html", "a")
        # 		f.write(finalTag)
        # 		f.close()
        # 	    finalTag = (f"/ul>\n")
        # 		f = open("index.html", "a")
        # 		f.write(finalTag)
        # 	clear_log()
        # 	print("list added!\n")

        elif "add paragraph" in query:
            speak("adding your paragraph")
            print("\nNo Speech input for paragraph because paragraphs can be too long to speak\nDo not press enter for new line type \"<br>\" to change line")
            content = input("Start typing/paste your paragraph here: \n")
            finalTag = (f"<p>{content}</p>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("paragraph added!\n")
            speak("paragraph added!")

        elif "add video" in query:
            speak("adding your video tag")
            width = input("Enter Width of your video in pixels: ")
            height = input("Enter height of your video in pixels: ")
            url = input("paste/enter url for video without extension (mp4 only): ")
            finalTag = (f"<video width=\"{width}\" height=\"{height}\" controls><source src=\"{url}.mp4\" type=\"video/mp4\"></video>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            print("video added!\n")
            speak("video added!")

        elif "complete website" in query:
            speak("completing your website")
            finalTag = (f"</body>\n</html>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clear_log()
            speak("Website Completed!, Thanks for using Me ,Aka ,Jarvis\n")
            print("Website Completed!")

        elif "terminate program" in query:
            speak("ending program, thanks for using Me ,Aka ,Jarvis")
            os.system("cls")
            print(f"{Bcolors.OKCYAN + creditsScreen + Bcolors.ENDC}")
            print("Jarvis(S.T.Html) ended sucessfully\n")
            looper = 10

        elif "how are you today" in query:
            print("Im A Fucking Program I Have No Emotions DumbAss\n")
            speak("Im A Fucking Program ,I Have No Emotions DumbAss")
        
        elif "do you know me" in query:
            speak("Type In Your code Here")
            boss = ['pointbreak']
            a = input("Type In Your code Here: ")
            if a in boss:
                speak("Welcome Artin ,You Are My Creator")
            else:
                speak("You Are A Normal User")
        
        elif "fuck you" in query:
            print("Jeez You Kiss Your Mother With That Mouth\n")
            speak("Jeez, You Kiss Your Mother With That Mouth")

        else:
            print("\n\nREQUEST ERROR SEE THE 'HTML Elements And Voice Commands List.txt' FILE FOR HELP\n\n")
            speak("REQUEST ERROR, SEE THE,'HTML Elements And Voice Commands List.txt',FILE FOR HELP")

###########################################################################################
#                                                                                         #
#        |          ||          _________                       _____      ___________    #
#        |         |  |        |         |   \              /     |       |               #
#        |        |    |       |         |    \            /      |       |               #
#        |       |      |      |_________|     \          /       |       |               #
#        |      |        |     |\               \        /        |       |___________    #
#        |     |__________|    | \               \      /         |                   |   #
# |      |    |            |   |  \               \    /          |                   |   #
# |      |   |              |  |   \               \  /           |                   |   #
# |______|  |                | |    \               \/          __|__     ____________|   #
#                                                                                         #
###########################################################################################
#################
# AI COMPANION  #
#################