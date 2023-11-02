
#Brightness Control
import screen_brightness_control as sc, pyautogui
def brightness(query):
    # print(sc.get_brightness())
    l= {'zero':0, 'one':10, 'two':20, 'three':30, 'four':40, 'five':50, 'six':60, 'seven':70, 'eight':80, 'nine':90, 'ten':100}
    sc.set_brightness(l.get(query))

#Volume Control
import pyautogui

def volume(query):
    if 'volume up' in query:
        pyautogui.press("volumeup")
    elif 'volume down' in query:
        pyautogui.press("volumedown")
    elif 'volume mute' in query or 'volume unmute' in query:
        pyautogui.press("volumemute")
        
# brightness('zero')
# volume("volumedown")
# time.sleep(5)
# print(pyautogui.position())