# PyMathQuizMaker

## Creating a quiz
This is an application for making math quizzes. 
To create a quiz:
```bash
quiz create (-f filename|-s string|-r) [-k keyfile] [-q quizfile]
```
If you use -f, you must pass a file path. The file must contain a question set following the rules below.
If you use -s, pass a string with a question set.
if you use -r, the question set will be read from stdin.
-k and -q set the output files (default stdout).
### Question sets
In a question set, each question must be seperated by a space. Each question should start with one of the letters a*(add)*, s*(subtract)*, m*(multiply)*, d*(divide)*.It should be followed by ':', the the number of digits in the first number, ':', and the number of digits in the second number.

## Taking a quiz
To take a quiz, you must create one first.
```bash
quiz take -q quizfile -k keyfile -r outfile
```
-q and -k are required. They are files as created with ```quiz create```.
It outputs the percentage and correct questions into _outfile_.
