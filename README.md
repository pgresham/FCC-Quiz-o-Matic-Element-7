# FCC-Quiz-o-Matic-Element-7
FCC Quiz-o-Matic: Element 7

Description:
This is a simple command line quiz program to review the FCC Element 7 GMDSS question bank. These questions are published by the FCC and are the same ones that appear on the exam.

Using the Program:
Running quiz.py loads the questions and answers from their corresponding text files in the same directory. Note: the files MUST all be in the same directory for the program to function. If quiz.py cannot open either of the files or either file encounters problems loading, the program will return an error. If this is the case, running the verify.py script will help locate the issue. This is particularly helpful in the case that different text files are being used for the quiz.

Modifying the Questions and Answers and the Format it Wants to See:
The included text documents E7AnswerKey and E7QuestionBank are made to be easily human readable and editable. The Questions should follow the following format:

[Question Number] Question:
A. Answer 1
B. Answer 2
C. Answer 3
D. Answer 4
[newline]
[Question Number] Question:
A. Answer 1
B. Answer 2
C. Answer 3
D. Answer 4
[newline] 
...And so on. 

After the last question and before the end of file, there need to be two blank  lines to correctly load the last question. 

The answer file should go as follows:
[Question Number] - [Letter or Number]
[Question Number] - [Letter or Number]
[Question Number] - [Letter or Number]
...And so forth. 

Enjoy!
