#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.simpledialog import SimpleDialog, askinteger
import tkinter.simpledialog as sd
from tkinter.messagebox import *
from tkinter.filedialog import *
import os



class CopyShow(sd.Dialog):
	def __init__(self, parent, text, caption, title=None):
		self.text = text
		self.caption = caption
		super().__init__(parent, title)

	def buttonbox(self):
		box = Frame(self)

		w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
		w.pack(side=LEFT, padx=5, pady=5)

		self.bind("<Return>", self.ok)
		self.bind("<Escape>", self.cancel)

		box.pack()


	def body(self, master):
		d = self
		self.show = Entry(master, width=-1)
		self.caption = Label(master, text=d.caption)
		self.caption.pack(side=TOP)
		self.show.insert(10,d.text)
		self.show.config(state='readonly')
		self.show.pack(side=BOTTOM)






class MultiChoiceQ(SimpleDialog):
	pass



def ask_multiple_choice_question(title, prompt, options, tk):
	d = MultiChoiceQ(tk, prompt, options, title=title)
	returnval = options[d.go()]
	return returnval

def popinput(tk, question, title="Quiz"):
	val = askinteger(title, question)
	return val

def create(tk):
	noqs = popinput(tk, "How many questions would you like to create?")
	if not noqs:
		return
	print("Creating %s questions." % (noqs))
	questions = []
	for x in range(int(noqs)):
		qtype = str(ask_multiple_choice_question(title="Question %s" % (x + 1), prompt="What type of question should question %s be?" % (x + 1), options=["Addition", "Subtraction", "Multiplication", "Division"], tk=tk))
		print("Asking for input. " + str(qtype))
		d1 = str(popinput(tk, "How many digits should the first number have?", "Question %s" % (x + 1)))
		if d1 == 'None':
			return
		d2 = str(popinput(tk, "How many digits should the second number have?", "Question %s" % (x + 1)))
		if d2 == 'None':
			return
		q = [qtype[0].lower(), d1, d2]
		questions.append(':'.join(q))
	quiz = ' '.join(questions)
	#showinfo("Question Set", "The question set is:\n'%s'" % (quiz))
	save = askyesno('Save','Would you like to save this quiz format?')
	if save:
		f = asksaveasfile(parent=tk, title='Save quiz format')
		print(quiz, file=f)
		f.close()
	show = askyesno('Show quiz format','Would you like to view this quiz format?')
	if show:
		show = CopyShow(tk, quiz, 'Quiz format', 'Quiz Format')
		pass
	system = './quiz create -s "%s" -k %s -q %s' % (quiz, '%s','%s')
	quizfile = asksaveasfilename(parent=tk,title='Where would you like to save the quiz?')
	if quizfile == '()':
		return
		
	keyfile = asksaveasfilename(parent=tk,title='Where would you like to save the key?')
	if keyfile == '()':
		return
	system_wp = system % (keyfile, quizfile)
	os.system(system_wp)
	
def take(tk):
	qf = askopenfile(parent=tk, title='Where is the quizfile?')
	kf = askopenfile(parent=tk, title='Where is the keyfile?')
	key = kf.read()
	quiz = qf.read()
	kf.close()
	qf.close()
	keylist = key.split('\n')[:-2]
	quizqs = quiz.split('\n\n')[:-1]
	print (quizqs,keylist)
	key = keylist
	quiz = quizqs
	if len(quiz) != len(key):
		showerror(title='Quiz', message='The key and quiz files do not match!')
		return
	record = []
	for (q, a) in zip(quiz, key):
		useranswer = askinteger('Quiz', q)
		if useranswer == int(a):
			showinfo('Answer', 'You are correct!')
			record.append(1)
		else:
			showinfo('Answer', 'You\'re wrong. The answer is %s' % a)
			record.append(0)
	score = (sum(record)/len(quiz))*100
	showinfo('Percentage', 'You got %s questions correct!(%s%%)' % (sum(record),score))
	rf = None
	while rf == None:
		rf = asksaveasfile(parent=tk, title='Where would you like to save your score?')
	print('%s%%\n%s'%(score,record), file=rf)
	rf.close()



def mainwindow():
	tk = Tk()
	tk.title("Math Quiz Maker")
	tk.geometry("300x300")
	text = Label(tk, text="Quizzes!")
	text.pack()
	make = Button(tk, text="Create a Quiz", command=lambda: create(tk))
	takeb = Button(tk, text='Take a Quiz', command=lambda: take(tk))
	takeb.place(anchor="se", relx=0.9, rely=0.9)
	make.place(anchor="sw", relx=0.1, rely=0.9)
	return tk

def main():
	tk = mainwindow()
	tk.mainloop()

if __name__ == '__main__':
	main()

