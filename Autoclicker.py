import win32gui 
import win32api
import win32con
import ctypes
import threading
import time
import random
import customtkinter
import json

onLunar = False
toggled = False
blockhitting = False
CPS = 10;
keys = {}
with open("config.json", "r") as f:
    windowName = json.load(fp=f)['Window_Name']

if __name__ == "__main__":
    print("Loading Clicker...")
    try:
        post = win32gui.FindWindowEx(0, 0, 0, windowName)
        ctypes.windll.user32.MessageBoxW(post, "Use the keybind 'F' to toggle on/off", "Welcome", None)
    except:
        print("Use keybind 'F' to toggle the autoclicker on/off.  Reminder: The Program in config.json has to be open and if your receiving this message, then it's not open.")

def onWindow():
    global onLunar
    window = win32gui.FindWindowEx(0, 0, 0, windowName)
    while True:
        hWnd = win32gui.GetForegroundWindow()
        if hWnd == window:
            onLunar = True
        else:
            onLunar = False

def toggle():
    global toggled
    while True:
        if win32api.GetKeyState(0x46) == 1:
            toggled = True
        else:
            toggled = False
        time.sleep(0.1)
    
def blockhit():
     while True:
        if toggled and onLunar and blockhitting:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            time.sleep(0.025)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        time.sleep(random.uniform(0.9, 1.1))

def clicker():
    global toggled
    while True:
        if toggled and onLunar:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        try:
            time.sleep(random.uniform(1/(CPS-3), 1/(CPS+3)) - 0.01)
        except:
            time.sleep(random.uniform(1/(CPS), 1/(CPS+3)) - 0.01)



threading.Thread(target=onWindow).start()
threading.Thread(target=toggle).start()
threading.Thread(target=blockhit).start()
threading.Thread(target=clicker).start()





#
#   UI/WINDOW
#

def toggleHit():
    global blockhitting
    blockhitting = not blockhitting


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("320x240")
root.resizable(False, False)
root.title("🥧 Clicker")

mainfont = customtkinter.CTkFont(family="Monospace", size=40, weight="bold")

title = customtkinter.CTkLabel(root, text="🥧 Clicker", text_color="white", font=mainfont)
title.grid(row=0, column=0, columnspan=3, padx=40)

lcps = customtkinter.CTkLabel(root, text="Clicker", text_color="white")
lcps.grid(row=1, column=0, padx=5)

scroll = customtkinter.CTkSlider(master=root, width=200, height=30, corner_radius=15,button_corner_radius=15, bg_color="transparent", fg_color="black")
scroll.grid(row=1, column = 1, columnspan=2, padx=10, pady=15)

lcpsvalue = customtkinter.CTkLabel(root, text=str(scroll._value*20)+" CPS", text_color="white")
lcpsvalue.grid(row=1, column=3)


blockhitcheck = customtkinter.CTkCheckBox(root, text="Blockhit?", hover_color="green", border_color="green", fg_color="green", command=toggleHit)
blockhitcheck.grid(row=2, column=1, columnspan=2)



def Lcheck():
    global CPS
    while True:
        if not scroll._value*20 == 0:
            lcpsvalue.configure(text=str(round(scroll._value*20))+" CPS")
            CPS = round(scroll._value*20)
            if CPS > 15 or CPS < 7:
                lcpsvalue.configure(text_color="red")
            else:
                if CPS == 11 or CPS == 12 or CPS == 13:
                    lcpsvalue.configure(text_color="#FFD700")
                else:    
                    lcpsvalue.configure(text_color="green")
        else:
            lcpsvalue.configure(text=str(round(scroll._value*20) + 1)+" CPS")
            CPS = round(scroll._value*20) + 1
        time.sleep(0.01)

threading.Thread(target=Lcheck).start()


root.mainloop()











