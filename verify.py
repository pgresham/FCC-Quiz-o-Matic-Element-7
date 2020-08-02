#Use this program to verify that questions and answers line up in their corresponding files.
def red(line):
	print('\033[91m {}\033[00m' .format(line),end ='')
if __name__ == '__main__':
	q = []
	a = []
	flag = 0
	try:
		with open('E7QuestionBank','r') as qbank:
			buffer = []
			for line in qbank:
				if line != '\n':
					buffer.append(line)
				else:
					q.append(buffer)
					buffer = []
			qbank.close()
	except:
		flag = 1
		red('\nRead error with Question Bank File\n')
		print('This probably means either the file isn\'t named correctly or is not in the same directory as the main script. It could also be that you don\'t have privileges to access the files')
	try:
		with open('E7AnswerKey','r') as abank:
			for line in abank:
				a.append(line.strip('\n'))
			abank.close()
	except:
		flag = 1
		red('\nRead error with Answer Bank File\n')
		print('This probably means either the file isn\'t named correctly or is not in the same directory as the main script. It could also be that you don\'t have privileges to access the files')
	
	if flag == 1:
		print('\n')
		exit()
	
	
	
	if len(a) != len(q):
		print(len(a),len(q))
		red('Mismatched length\n')
		print('The file parser loads the questions and answers using a newline as a delimiter if there isn\'t one (and only one) line of whitespace between each question or if there is any whitespace in the answer key, they will not line up correctly. Additionally, the way in which the question bank loads requires TWO newline spaces at the end of the file (before EOF) to load correcly. Hope that helps!')
		exit()
		
	for i in range(min(len(q),len(a))):
			if a[i][0:5] != q[i][0][0:5]:
				red('Check for errors at Answer:'+a[i][0:5]+' Question: '+q[i][0][0:5])
	exit()
	

