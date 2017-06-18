#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import FileDialog
import pyautogui
import os

class tkInput:
	def __init__(self, parent, question, title):

		top = self.top = Toplevel(parent)
		top.title(title)

		Label(top, text=question).pack()

		self.e = Entry(top)
		self.e.pack(padx=5)

		b = Button(top, text="OK", command=self.ok)
		b.pack(pady=5)

	def ok(self):

		self.val = self.e.get()

		self.top.destroy()

'''
root = Tk()
d = MyDialog(root)

root.wait_window(d.top)
'''

def popinput(tk, question, title="Quiz"):
	d = tkInput(tk, question, title)

	tk.wait_window(d.top)

def create():
	while True:
		
	pass
	

def mainwindow():
	tk = Tk()
	tk.title("Math Quiz Maker")
	tk.geometry("500x500")
	#imgicon = PhotoImage(file=os.path.join('/home/pi/Desktop/PyMathQuiz','icon.gif'))
	#tk.tk.call('wm', 'iconphoto', root._w, imgicon)
	text = Label(tk, text="Quizzes!")
	text.pack()
	make = Button(tk, text="Create a Quiz", command=create)
	make.place(anchor="sw", relx=0.1, rely=0.9)
	return tk

def main():
	tk = mainwindow()
	tk.mainloop()

if __name__ == '__main__':
	main()

