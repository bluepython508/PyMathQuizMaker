#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import sys

def take(args):
	pass

def create(args):
	if args.inf:
		f = open(args.inf,'r')
		quizformat = f.read()
		f.close()
	elif args.string:
		quizformat = args.string
	elif args.stdin:
		quizformat = sys.stdin.read()
	
	pass




def main():
	rootparse = argparse.ArgumentParser()
	subparse = rootparse.add_subparsers()
	parsecreate = subparse.add_parser('create')
	parsetake = subparse.add_parser('take')
	form = parsecreate.add_mutually_exclusive_group(required=True)
	form.add_argument('-f', '--file', type=argparse.FileType('r'), dest=inf)
	form.add_argument('-s', '--string')
	form.add_argument('-r', '--stdin', action="store_true")
	parsecreate.add_argument("outquiz_file", type=argparse.FileType('w'), default=sys.stdout)
	parsecreate.set_defaults(mode=create)
	parsetake.set_defaults(mode=take)
	args = rootparse.parse_args()
	args.mode(args)
if __name__ == '__main__':
	main()

