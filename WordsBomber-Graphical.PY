from tkinter import *
import keyboard
import time
import os
import colorama
from colorama import Fore
colorama.init()

def foo():
	os.system('Taskkill /IM WordsBomber-Graphical.exe /F')
	os.system('Taskkill /IM python.exe /F')
	os.system('Taskkill /IM WordsBomber-Graphical.py /F')
	os.system('Taskkill /IM WordsBomber-Graphical.PY /F')

def main():
	keyboard.write(message.get())

root = Tk()
root.title("WordsBomber-Graphical")
root.geometry("300x140")
root["bg"] = "gray22"
message = StringVar()
keyboard.add_hotkey('esc', foo)

def buttonclick():
	time.sleep(5)
	for __ in range(666000):
		main()
		keyboard.send("enter")

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")
message_button = Button(text="inject", fg='green', command=buttonclick)
message_button.place(relx=.2, rely=.1, anchor="c")
ebaty = """WordsBomber-Graphical - tool for sending 
a lot of messages 
to close the app in an emergency,
press the esc button, 
enter the word in the input field to get started,
and then click the inject button"""
label2 = Label(text=ebaty, justify=LEFT)
label2.place(relx=.1, rely=.2)

root.mainloop()
