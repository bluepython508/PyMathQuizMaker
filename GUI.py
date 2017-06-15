#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Tkinter import *
import turtle
import pyautogui
import os

def mainwindow():
	tk = Tk()
	tk.title("Math Quiz Maker")
	tk.geometry("500x500")
	#imgicon = PhotoImage(file=os.path.join('/home/pi/Desktop/PyMathQuiz','icon.gif'))
	#tk.tk.call('wm', 'iconphoto', root._w, imgicon)
	text = Label(tk, text="Quizzes!")
	text.pack()
	return tk

def main():
	tk = mainwindow()
	tk.mainloop()

if __name__ == '__main__':
	main()

