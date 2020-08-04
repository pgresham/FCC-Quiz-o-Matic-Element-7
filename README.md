# FCC-Quiz-o-Matic-Element-7

<h2>Description:</h2>
<p>This is a simple command line quiz program to review the FCC Element 7 GMDSS question bank. These questions are published by the FCC and are the same ones that appear on the exam. The main program is written in Python 3.x for *nix systems. Modifying the clear() function (changing 'clear' to 'cls') should make it work in Windows, but this has not yet been tested.</p>

<h2>Using the Program:</h2>
<p>Running quiz.py loads the questions and answers from their corresponding text files in the same directory. Note: the files MUST all be in the same directory for the program to function. If quiz.py cannot open either of the files or either file encounters problems loading, the program will return an error. If this is the case, running the verify.py script will help locate the issue. This is particularly helpful in the case that different text files are being used for the quiz.</p>

<h2>Modifying the Questions and Answers and the Format it Wants to See:</h2>
<p>The included text documents E7AnswerKey and E7QuestionBank are made to be easily human readable and editable. The Questions should follow the following format:</p>

<p>[Question Number] Question:<br/>
A. Answer 1<br/>
B. Answer 2<br/>
C. Answer 3<br/>
D. Answer 4<br/>
[newline]<br/>
[Question Number] Question:<br/>
A. Answer 1<br/>
B. Answer 2<br/>
C. Answer 3<br/>
D. Answer 4<br/>
[newline] <br/>
...And so on. <br/></p>

<p>After the last question and before the end of file, there need to be two blank  lines to correctly load the last question. </p>

<p>The answer file should go as follows:<br/>
[Question Number] - [Letter or Number]<br/>
[Question Number] - [Letter or Number]<br/>
[Question Number] - [Letter or Number]<br/>
...And so forth. <br/></p>

<h3>Enjoy!</h3>
