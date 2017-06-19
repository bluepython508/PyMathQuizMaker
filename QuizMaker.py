#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import sys
import random as r
random = r.SystemRandom()
expansions = {"d":["Divide %s by %s.",'//'], "a":["Add %s to %s.", '+'] ,"s":["Subtract %s from %s.", '-'] ,"m":["Multiply %s by %s.", '*']}
def createq(qf):
	qf = qf.split(":")
	question = expansions[qf[0]][0]
	no1 = str(random.randint((10**(int(qf[1])-1)), (10**(int(qf[1])))))
	no2 = str(random.randint((10**(int(qf[2])-1)), (10**(int(qf[2])))))
	answer = eval(no1 + expansions[qf[0]][1] + no2)
	if qf[0] == "s":
		return (question % (no2, no1), answer)
	else:	
		return (question % (no1, no2), answer)


def take(args):
	messages = {True:["Correct!", "Very good!", "Right", "Awesome!"], False:["Wrong", "Incorrect", "Too bad"]}
	quiz = args.inf.read()
	key = args.keyf.read()
	quiz = quiz.split("\n\n")
	key = key.split('\n')
	quiz.pop()
	results = []
	for question in quiz:
		guess = eval(input(question))
		answer = eval(key[quiz.index(question)])
		print(random.choice(messages[(guess==answer)]))
		results.append((guess == answer))
	correct = 0
	for x in results:
		if x:
			correct += 1
	percent = (correct/len(key))*100
	print("You got %s percent correct." % (percent))
	def replace(x):
		if x:
			return "Correct"
		else:
			return "Incorrect"
	if args.record_file:
		result = map(replace, results)
		results = ' '.join(result)
		args.record_file.write("Percent: %s\n%s" % (percent, results))
	pass

def create(args):
	if args.inf:
		quizformat = args.inf.read()
	elif args.string:
		quizformat = args.string
	elif args.stdin:
		quizformat = sys.stdin.read()
	quizqs = quizformat.split(" ")
	questions = []
	answers = []
	for qf in quizqs:
		if qf[0] in expansions.keys():
			question, answer = createq(qf)
			questions.append(str(question))
			answers.append(str(answer))
		else:
			print("'%s' is not a recognized type of question." % (qf[0]))
	questions.append('\n')
	answers.append('\n')
	quiz = '\n\n'.join(questions)
	key = '\n'.join(answers)
	args.outfile_quiz.write(quiz)
	args.outfile_key.write(key)
	pass




def main():
	rootparse = argparse.ArgumentParser()
	subparse = rootparse.add_subparsers()
	parsecreate = subparse.add_parser('create')
	parsetake = subparse.add_parser('take')
	parsetake.add_argument('-q', '--quiz', type=argparse.FileType('r'), dest="inf", required=True)
	parsetake.add_argument('-k', '--key', type=argparse.FileType('r'), dest="keyf", required=True)
	parsetake.add_argument('-r', '--record-file', dest="record_file", type=argparse.FileType('w'), required=False)
	form = parsecreate.add_mutually_exclusive_group(required=True)
	form.add_argument('-f', '--file', type=argparse.FileType('r'), dest="inf")
	form.add_argument('-s', '--string')
	form.add_argument('-r', '--stdin', action="store_true")
	parsecreate.add_argument('-q', '--quiz', dest="outfile_quiz", type=argparse.FileType('w'), default=sys.stdout, required=False)
	parsecreate.add_argument('-k', '--key', dest="outfile_key", type=argparse.FileType('w'), default=sys.stdout, required=False)
	parsecreate.set_defaults(mode=create)
	parsetake.set_defaults(mode=take)
	args = rootparse.parse_args()
	args.mode(args)
if __name__ == '__main__':
	main()

