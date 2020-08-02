import random
import os
import time




def clear():			#Programmed for POSIX systems, obviously needs to be changed for MS-DOS.
	os.system('clear')

def yellow(line): 				#Note Does not automatically add \n to line, must be Explicity included
	print('\033[93m {}\033[00m'.format(line),end ='')

def cyan(line): 				#Note Does not automatically add \n to line, must be Explicity included
	print('\033[96m {}\033[00m'.format(line),end ='')
def red(line):
	print('\033[91m {}\033[00m' .format(line),end ='')

def verify(q,a):
	try:
		
		if len(a)==len(q):
			for i in range(len(q)):
					if a[i] == 'A' or a[i] == 'B' or a[i] == 'C' or a[i] == 'D':
						print('[',end='')
						cyan('ok ')
						print(']  '+q[i][0][0:5])
						time.sleep(0.0005)
						
		else: 
			red('file misalignment, run verify.py script to find errors')
			exit()
	except:
		red('\nFatal error with question/answer bank\n')
		exit()
	clear()	
def mainBanner():
	yellow('  ___  ___   ___ \n  / __\/ __\ / __\ \n / _\ / /   / /    \n/ /  / /___/ /___        ')
	print('Version 1.0',end='')
	yellow('\n\/   \____/\____/        ')
	print('By Philip Gresham\n  ',end='')
	yellow('____       _                                  ___  _\n  /___ \_   _(_)____      ___         /\/\   __ _| |_(_) ___\n //  / / | | | |_  /____ / _ \ _____ /    \ / _` | __| |/ __|\n/ \_/ /| |_| | |/ /_____| (_) |_____/ /\/\ \ (_| | |_| | (__ \n\___,_\ \__,_|_/___|     \___/      \/    \/\__,_|\__|_|\___|\n\n')
	time.sleep(2)
	clear()


def mainMenu(score):
	clear()
	if score == 0.0:
		print(50*'-',end='')
		yellow('\nFCC Quiz-o-Matic\n')
		print(50*'-')
	else:
		print(50*'-',end='')
		yellow('\nFCC Quiz-o-Matic          Last Score: '+str(score)+'%\n')
		print(50*'-')
	cyan('\n1. Element 7 Quick Test (10 Questions)\n\n2. Element 7 Long Test (All 600 Questions).\n\n00. Exit (Works at any time)\n')
	x = str(input('\n:')).strip()
	if x == '1':
		shortTest(q,a)
	elif x == '2':
		grandTest(q,a)
	elif x == '00':
		clear()
		exit()
	else:
		mainMenu(score)

def testProcess(q,a,order):
	right = 0
	count = 0
	score = 0.0
	for n in order:
		print(50*'-',end='')
		yellow('\nCorrect: '+str(right)+' / '+str(count)+'    Question #'+str(count+1)+'\n')
		print(50*'-')
		colorize = 1
		for line in q[n]:
			if colorize == 1:
				cyan('\n'+line)
				colorize = 0
			else:
				print(line,end='')	
		x = input('\nAnswer: ').upper()
		while x != 'A' and x != 'B' and x != 'C' and x !='D' and x != '00':
			clear()
			print(50*'-',end='')
			yellow('\nCorrect: '+str(right)+' / '+str(count)+'    Question #'+str(count+1)+'\n')
			print(50*'-')
			colorize = 1
			for line in q[n]:
				if colorize == 1:
					cyan('\n'+line)
					colorize = 0
				else:
					print(line,end='')
			x = input('\nAnswer: ').upper()


		if x == '00':
			if count >0: #avoids division by zero error on early exit
				score = round(100*(float(right)/float(count)),2)
			else:
				score = 0
			mainMenu(score)
		elif x == a[n]:
			cyan('\nCorrect!\n')
			right += 1
		else:
			cyan('\nWrong, correct answer: '+a[n]+'\n')
		time.sleep(1.5)
		clear()
		count += 1
	if count >0:
		score = round(100*(float(right)/float(count)),2)
	else:
		score = 0
	mainMenu(score)



def grandTest(q,a):  #Called grand test b/c I couldn't remember the word 'long'
	clear()
	order = []
	for i in range(len(a)):
		order.append(i)
	random.shuffle(order)	
	testProcess(q,a,order)


def shortTest(q,a):
	clear()
	order = []
	for i in range(10):
		order.append(random.randrange(599))
	random.shuffle(order)
	testProcess(q,a,order)



if __name__ == '__main__':


	q = []
	a = []
	try:
		with open('E7QuestionBank','r') as qbank:
			buffer = []
			for line in qbank:
				if line != '\n':
					buffer.append(line+'\n')
				else:
					q.append(buffer)
					buffer = []
			qbank.close()
	except:
		red('\nQuestion Bank File Error\n')
		exit()	
	try:
		with open('E7AnswerKey','r') as abank:
			for line in abank:
				a.append(line.strip('\n')[-1:]) #only loads A B C D values. File also
			abank.close()			#includes question numbers for each to make
								#human readable and for error checking
	except:
		red('\nAnswer Bank File Error\n')
		exit()	

	clear()
	verify(q,a)
	mainBanner()
	mainMenu(0)		
