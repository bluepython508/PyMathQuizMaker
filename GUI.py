#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import FileDialog
import pyautogui
import os

def ask_multiple_choice_question(tk, prompt, options, title):
	root = Tk()
	root.title(title)
	def ok():
		global returnval
		returnval = options[v.get()]
		root.destroy()
	if prompt:
		Label(root, text=prompt).pack()
	v = IntVar()
	for i, option in enumerate(options):
		Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
	x = Button(root, text="Submit", command=ok)
	x.pack()
	root.mainloop()
	return returnval
	
class tkInput:
	def __init__(self, question, title):
		self.tk = Tk()
		tk = self.tk
		tk.title(title)
		Label(tk, text=question).pack()

		self.e = Entry(tk)
		self.e.pack(padx=5)

		b = Button(tk, text="OK", command=self.ok)
		b.pack(pady=5)
	def ok(self):

		self.val = self.e.get()

		self.tk.destroy()

def popinput(tk, question, title="Quiz"):
	d = tkInput(question, title)
	d.tk.mainloop()
	val = d.val
	del d
	return val

def create(tk):
	noqs = popinput(tk, "How many questions would you like to create?")
	print("Creating %s questions." % (noqs))
	questions = []
	for x in range(int(noqs)):
		qtype = str(ask_multiple_choice_question(title="Question %s" % (x + 1), prompt="What type of question should question %s be?" % (x + 1), options=["Addition", "Subtraction", "Multiplication", "Division"], tk=tk))
		print("Asking for input. " + str(qtype))
		d1 = popinput(tk, "How many digits should the first number have?", "Question %s" % (x + 1))
		d2 = popinput(tk, "How many digits should the second number have?", "Question %s" % (x + 1))
		q = [qtype, d1, d2]
		questions.append(':'.join(q))
	quiz = ' '.join(questions)
	showinfo("Question Set", "The question set is:\n'%s'" % (quiz))
	
	
	pass
	

def mainwindow():
	tk = Tk()
	tk.title("Math Quiz Maker")
	tk.geometry("500x500")
	#imgicon = PhotoImage(file=os.path.join('/home/pi/Desktop/PyMathQuiz','icon.gif'))
	#tk.tk.call('wm', 'iconphoto', root._w, imgicon)
	text = Label(tk, text="Quizzes!")
	text.pack()
	make = Button(tk, text="Create a Quiz", command=lambda: create(tk))
	make.place(anchor="sw", relx=0.1, rely=0.9)
	return tk

def main():
	tk = mainwindow()
	tk.mainloop()

if __name__ == '__main__':
	main()

