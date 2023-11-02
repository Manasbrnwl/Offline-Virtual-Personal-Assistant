import os, datetime, rotatescreen as rs, urllib, keyboard, time
from playsound import playsound
import offlineSpeechRecognition as off
import pyautogui as ui
import Brigthness_Volume_toggle as bv
import codepath as cp
import speak as sp
import chatbot as cb

def login():
    hour = int(datetime.datetime.now().hour)
    if (hour>=6 and hour< 12):
        sp.speak("Good Morning !")
    elif (hour>= 12 and hour<18):
        sp.speak ("Good Afternoon !")
    else:
        sp.speak("Good Evening !")
    date()
    sp.speak("I am Thermo")#, Please guide me how may i help you")

def logout():
    sp.speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        sp.speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        sp.speak("Good afternoon")
    elif (hour >= 18 and hour < 20):
        sp.speak("Good Evening")
    else:
        sp.speak("Good Night.. Sweet Dreams")

def portrait():
    
    screen = rs.get_primary_display()
    screen.rotate_to(90)

def landscape():
    screen = rs.get_primary_display()
    screen.rotate_to(0)

def screenCapture():
    sp.speak('name your screenshot')
    query = off.listen()
    myScreenshot = ui.screenshot()
    myScreenshot.save(r'C:\\Users\\mystm\\Desktop\\Major Project\\Screenshot\\'+query+'.png')

def samay():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    sp.speak(f"The current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    sp.speak("The current date is")
    sp.speak(date)
    sp.speak(month)
    sp.speak(year)
    
def information():
    sp.speak("I am Thermo, version 3.0, I am a Personal Virtual Computer Assistent, I am developed by Manas Baranwal")
    sp.speak("Now i hope you know me")

def connect(host='http://google.com'):
    
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
    
if __name__ == "__main__":
    os.system('cls')
    name = 0
    query = 0
    print("         ====================================================================================================         ")
    print("                  _________    _     _     ______     __________    ___         ___       _______                     ")
    print("                 !___   ___!  ! !   ! !   ! _____!   !   __    /   !   \       /   !     (   _   )                    ")
    print("                     ! !      ! !___! !   ! !__      !  !_/   /    ! !\ \     / /! !    (   ( )   )                   ")
    print("                     ! !      !  ___  !   !  __!     !     __/     ! ! \ \   / / ! !   (   (   )   )                  ")
    print("                     ! !      ! !   ! !   ! !____    ! !\  \       ! !  \ \_/ /  ! !    (   (_)   )                   ")
    print("                     !_!      !_!   !_!   !______!   !_!  \__\     !_!   \___/   !_!     (_______)                    ")
    print("         ====================================================================================================         ")
    print("                                                                          OFFLINE VIRTUAL PERSONAL ASSISTANT          ")   
    print("                                                                         ====================================         ")   
    # print("                                                                              Developed By :- Manas Baranwal          ")  
    # print("                                                                             --------------------------------         ")                      
    print("\n")
    # login()


    # test
    # sp.speak( 'You are connected to internet!' if connect() else 'you are not connected on internet' )

    print('sp.speak :- ( Hello Thermo , Hey Thermo or Activate Thermo ) to Wakeup the Thermo.')
    
    while(True):
        query = off.listen()
        if('thermo' in query or 'activate' in query or 'hello' in query or 'hey' in query):
            # print("Activated :-)")
            playsound('D:\\Python\\Major Project\\Thermo.mp3')
               
            query = off.listen()
            
#visual studio code

            if 'open code' in query or 'open visual studio code' in query:
                sp.speak("opening visual studio code")
                os.startfile(cp.vscode)
                continue
                    
            elif 'close code' in query or  'close visual studio code' in query:
                os.system("taskkill /f /im Code.exe")
                sp.speak("done!")
                continue    
            
#command prompt            
            
            elif 'open cmd' in query or 'open command prompt' in query:
                sp.speak("opening command prompt")
                os.startfile(cp.cmd)
                continue
                    
            elif 'close cmd' in query or  'close command prompt' in query:
                os.system("taskkill /f /im Command Prompt.lnk")
                sp.speak("done!")
                continue  
            
#run            
            
            elif 'open run' in query:
                sp.speak("opening run")
                os.startfile(cp.run)
                continue
                    
            elif 'close run' in query:
                os.system("taskkill /f /im Run.lnk")
                sp.speak("done!")
                continue  
            
#control panel            
            
            elif 'open controlPanel' in query or 'open control panel' in query:
                sp.speak("opening control panel")
                os.startfile(cp.controlPanel)
                continue
                    
            elif 'close controlPanel' in query or  'close control panel' in query:
                os.system("taskkill /f /im Control Panel.lnk")
                sp.speak("done!")
                continue  
            
#On Screen Keyboard            
            
            elif 'open keyboard' in query:
                sp.speak("opening On Screen Keyboard")
                os.startfile(cp.keyboard)
                continue
                    
            elif 'close keyboard' in query:
                os.system("taskkill /f /im On-Screen Keyboard.lnk")
                sp.speak("done!")
                continue  
            
#voice access            
            
            elif 'open voice access' in query:
                sp.speak("opening voice access")
                os.startfile(cp.voiceaccess)
                continue
                    
            elif 'close voice access' in query:
                os.system("taskkill /f /im Voice access.lnk")
                sp.speak("done!")
                continue   
            
#powershell            
            
            elif 'open powershell' in query or 'open power shell' in query:
                sp.speak("opening Windows PowerShell")
                os.startfile(cp.powershell)
                continue
                    
            elif 'close powershell' in query or 'close power shell' in query:
                os.system("taskkill /f /im Windows PowerShell.lnk")
                sp.speak("done!")
                continue  
            
#Adobe Illustrator            
            
            elif 'open illustrator' in query:
                sp.speak("opening Adobe Illustrator 2021")
                os.startfile(cp.Illustrator)
                continue
                    
            elif 'close illustrator' in query:
                os.system("taskkill /f /im Adobe Illustrator 2021.lnk")
                sp.speak("done!")
                continue  
            
#Microsoft Access            
            
            elif 'open access' in query:
                sp.speak("opening Microsoft Access")
                os.startfile(cp.Access)
                continue
                    
            elif 'close access' in query:
                os.system("taskkill /f /im Access.lnk")
                sp.speak("done!")
                continue  

#Adobe Photoshop            
            
            elif 'open photoshop' in query or 'open photo shop' in query:
                sp.speak("opening Adobe Photoshop 2021")
                os.startfile(cp.Photoshop)
                continue
                    
            elif 'close photoshop' in query or 'close photo shop' in query:
                os.system("taskkill /f /im Adobe Photoshop 2021.lnk")
                sp.speak("done!")
                continue  
            
#Brave            
            
            elif 'open brave' in query:
                sp.speak("opening Windows PowerShell")
                os.startfile(cp.Brave)
                continue
                    
            elif 'close brave' in query:
                os.system("taskkill /f /im Brave.lnk")
                sp.speak("done!")
                continue  
            
#Microsoft Excel            
            
            elif 'open excel' in query:
                sp.speak("opening Microsoft Excel")
                os.startfile(cp.Excel)
                continue
                    
            elif 'close excel' in query:
                os.system("taskkill /f /im Excel.lnk")
                sp.speak("done!")
                continue  
         
#Google Chrome           
            
            elif 'open chrome' in query or 'open google chrome' in query:
                sp.speak("opening Google Chrome")
                os.startfile(cp.Chrome)
                continue
                    
            elif 'close chrome' in query or 'close google chrome' in query:
                os.system("taskkill /f /im Google Chrome.lnk")
                sp.speak("done!")
                continue  
#Microsoft Edge         
            
            elif 'open edge' in query or 'open microsoft edge' in query:
                sp.speak("opening Microsoft Edge")
                os.startfile(cp.Edge)
                continue
                    
            elif 'close edge' in query or 'close microsoft edge' in query:
                os.system("taskkill /f /im Microsoft Edge.lnk")
                sp.speak("done!")
                continue  
#OneDrive           
            
            elif 'open onedrive' in query or 'open one drive' in query:
                sp.speak("opening OneDrive")
                os.startfile(cp.OneDrive)
                continue
                    
            elif 'close onedrive' in query or 'close one drive' in query:
                os.system("taskkill /f /im OneDrive.exe")
                sp.speak("done!")
                continue  
          
#OneNote           
            
            elif 'open onenote' in query or 'open one note' in query:
                sp.speak("opening OneNote")
                os.startfile(cp.OneNote)
                continue
                    
            elif 'close onenote' in query or 'close one note' in query:
                os.system("taskkill /f /im OneNote.exe")
                sp.speak("done!")
                continue  

#Outlook           
            
            elif 'open onelook' in query or 'open one look' in query:
                sp.speak("opening Outlook")
                os.startfile(cp.Outlook)
                continue
                    
            elif 'close onelook' in query or 'close one look' in query:
                os.system("taskkill /f /im Outlook.exe")
                sp.speak("done!")
                continue  

#PC Manager         
            
            elif 'open pc manager' in query or 'open p c manager' in query:
                sp.speak("opening PC Manager")
                os.startfile(cp.PCmanager)
                continue
                    
            elif 'close pc manager' in query or 'close p c manager' in query:
                os.system("taskkill /f /im PC Manager.exe")
                sp.speak("done!")
                continue  

#Microsoft PowerPoint         
            
            elif 'open powerpoint' in query or 'open power point' in query:
                sp.speak("opening Microsoft PowerPoint")
                os.startfile(cp.PowerPoint)
                continue
                    
            elif 'close powerpoint' in query or 'close power point' in query:
                os.system("taskkill /f /im PowerPoint.exe")
                sp.speak("done!")
                continue  
         
#Microsoft Publisher        
            
            elif 'open publisher' in query:
                sp.speak("opening Microsoft Publisher")
                os.startfile(cp.Publisher)
                continue
                    
            elif 'close publisher' in query:
                os.system("taskkill /f /im Publisher.exe")
                sp.speak("done!")
                continue  
         
#Visual Studio 2019         
            
            elif 'open visualstudio' in query or 'open visual studio' in query:
                sp.speak("opening Visual Studio 2019")
                os.startfile(cp.VisualStudio)
                continue
                    
            elif 'close visualstudio' in query or 'close visual studio' in query:
                os.system("taskkill /f /im Visual Studio 2019.exe")
                sp.speak("done!")
                continue  
         
#Microsoft Word        
            
            elif 'open word' in query:
                sp.speak("opening Microsoft Word")
                os.startfile(cp.Word)
                continue
                    
            elif 'close word' in query:
                os.system("taskkill /f /im Word.exe")
                sp.speak("done!")
                continue  
         
#Dev-C++        
            
            elif 'open dev c++' in query or 'open dev c + +' in query:
                sp.speak("opening Dev-C++")
                os.startfile(cp.Cpp)
                continue
                    
            elif 'close dev c++' in query or 'close dev c + +' in query:
                os.system("taskkill /f /im Visual Studio 2019.exe")
                sp.speak("done!")
                continue 
                      
#Free Download Manage        
            
            elif 'open free download manage' in query:
                sp.speak("opening Free Download Manage")
                os.startfile(cp.fdm)
                continue
                    
            elif 'close free download manage' in query:
                os.system("taskkill /f /im Visual Studio 2019.exe")
                sp.speak("done!")
                continue  
         
#IntelliJ IDEA Community Edition (Java)       
            
            elif 'open java' in query:
                sp.speak("opening IntelliJ IDEA Community Edition")
                os.startfile(cp.Intellij)
                continue
                    
            elif 'close java' in query:
                os.system("taskkill /f /im IntelliJ IDEA Community Edition 2021.2.2.exe")
                sp.speak("done!")
                continue  
         
#MySQL Workbench 8.0 CE         
            
            elif 'open my sql' in query or 'open my s q l' in query:
                sp.speak("opening MySQL Workbench")
                os.startfile(cp.MySQL)
                continue
                    
            elif 'close my sql' in query or 'close my s q l' in query:
                os.system("taskkill /f /im MySQL Workbench 8.0 CE.exe")
                sp.speak("done!")
                continue   
         
#Node.js       
            
            elif 'open node js' in query or 'open node j s' in query:
                sp.speak("opening Node.js")
                os.startfile(cp.Nodejs)
                continue
                    
            elif 'close node js' in query or 'close node j s' in query:
                os.system("taskkill /f /im Node.js.exe")
                sp.speak("done!")
                continue  
         
#WordPad        
            
            elif 'open wordpad' in query or 'open word pad' in query:
                sp.speak("opening WordPad")
                os.startfile(cp.WordPad)
                continue
                    
            elif 'close wordpad' in query or 'close word pad' in query:
                os.system("taskkill /f /im WordPad.exe")
                sp.speak("done!")
                continue  
         
#Task Manager        
            
            elif 'open task manager' in query:
                sp.speak("opening Task Manager")
                os.startfile(cp.TaskM)
                continue
                    
            elif 'close task manager' in query:
                os.system("taskkill /f /im Task Manager.exe")
                sp.speak("done!")
                continue  

#Git Bash        
            
            elif 'open git bash' in query:
                sp.speak("opening Git Bash")
                os.startfile(cp.GitBash)
                continue
                    
            elif 'close git bash' in query:
                os.system("taskkill /f /im Git Bash.exe")
                sp.speak("done!")
                continue  
        
#AnyDesk        
            
            elif 'open anydesk' in query or 'open any desk' in query:
                sp.speak("opening AnyDesk")
                os.startfile(cp.AnyDesk)
                continue
                    
            elif 'close anydesk' in query or 'close any desk' in query:
                os.system("taskkill /f /im AnyDesk.exe")
                sp.speak("done!")
                continue 

#Chatbot perform

            elif ("let's talk" in query or 'want to talk' in query
             or 'talk' in query):
                sp.speak("Ok! let's talk")
                while True:
                    query = off.listen()
                    cb.respone(query)
        
#Bluetooth

            elif 'bluetooth' in query:
                keyboard.press_and_release("windows+a")
                time.sleep(2)
                ui.click(x=1710, y=573)
                keyboard.press_and_release("escape")
                if 'on' in query:
                    sp.speak("Bluetooth is turned On")
                else:
                    sp.speak("Bluetooth is turned Off")
                continue

#Wi-Fi

            elif 'wifi' in query or 'wi fi' in query or 'why fi' in query:
                keyboard.press_and_release("windows+a")
                time.sleep(2)
                keyboard.press_and_release("return")
                keyboard.press_and_release("escape")
                if 'on' in query:
                    sp.speak("Wi-Fi is turned On")
                else:
                    sp.speak("Wi-Fi is turned Off")
                continue

#Airoplane

            elif 'airoplane' in query or 'aeroplane' in query or 'airplane' in query:
                keyboard.press_and_release("windows+a")
                time.sleep(2)
                ui.click(x=1835, y=575)
                keyboard.press_and_release("escape")
                if 'on' in query:
                    sp.speak("Airoplane mode is turned On")
                else:
                    sp.speak("Airpolane mode is turned Off")
                continue
                      
#Provide Time

            elif 'time' in query:
                samay()
                sp.speak("Thank you")
                continue

#Screen Portrait

            elif 'screen portrait' in query:
                portrait()
                sp.speak('done!')
                continue

#Screen Landscape

            elif 'screen landscape' in query:
                landscape()
                sp.speak('done!')
                continue
                    
#Provide Date

            elif 'date' in query:
                date()
                sp.speak("thank you")
                continue

#Screenshot

            elif ("screenshot" in query):
                screenCapture()
                sp.speak("Done!")
                continue
            
#brightness

            elif 'brightness' in query or 'display light' in query:
                query = query.replace("brightness", "")
                query = query.replace("display light", "")
                query = query.replace(" ", "")
                try:
                    bv.brightness(query)
                except:
                    sp.speak("Sorry couldn't understand")
                    
#volume
                    
            elif 'volume' in query:
                try:
                    bv.volume(query)
                except:
                    sp.speak("Sorry couldn't understand")

#Add Reminder

            elif ("create a reminder list" in query or "reminder" in query):
                sp.speak("What is the reminder?")
                try:
                    data = off.listen()
                    sp.speak("You said to remember that" + data)
                    reminder_file = open("thermo reminder.txt", 'a')
                    reminder_file.write('\n')
                    reminder_file.write(data)
                    reminder_file.close()
                except Exception:
                    sp.speak("Sorry i an unable to search your query")

                    
#Close Application

            # elif 'close' in query:
            #     keyboard.press_and_release('alt+F4')
            #     sp.speak('done!')
                        
#Restart Computer

            elif 'restart' in query or 'restart the pc' in query:
                sp.speak("do you want to restart this p. c.")
                q = off.listen()
                if "yes" in q:
                    logout()
                    os.system("shutdown /r /t 1")  
                    break
                else:
                    sp.speak("ok sir")
                    continue

#Shutting Down Computer

            elif 'shutdown' in query or 'shut down' in query:
                sp.speak("do you want to shutdown this p. c.")
                q = off.listen()
                if "yes" in q:
                    logout()
                    os.system("shutdown /s /t 1")  
                    break
                else:
                    sp.speak("ok sir")
                    continue