
# Python Fundamentals: Module 2.
Control Structures and Collections

In this project, the use and logical structures of Python control structures will be put into practice.



## Content
Project description

Characteristics of the program to be built

Problems and solutions


## Project description
The project is divided into two parts.

Part One:
Create a program to identify the length of an input word. The correct word must be between four and eight letters. Keep the following considerations in mind:
If the word is between four and eight letters long, a message indicating that the word is correct should be printed.
If the word is less than four letters long, a message should be displayed stating: "Hacen falta letras. Solo son N letras" (N being the number of letters in the word).
If the word is more than eight letters long, a message should be displayed stating: "Sobran letras. Tiene N letras" (N being the number of letters in the word).

Part Two:

Create a program that based on two input numbers (coordinates), identifies in which of the four quadrants the point is located. The program should verify that none of the coordinates are 0.
## Characteristics of the program

Before starting to write the code, I established the characteristics and logic that the program must follow to achieve the project's required conditions.

Both parts of the project require the use of conditionals to outline the program flow. I found that the main functions would be "if" and "while." The use of "if" is simple since it will be used for information inputs that fall within established ranges and allow for a final response.

To ensure that the program works correctly, it is necessary to test the order of the conditionals and the combinations that avoid errors in the program flow.
## Problems and solutions

Part One:

Using "If" and "Elif" it is possible to run the program to condition the length of a sentence, but using "while" simplifies the process and allows the user to continue entering sentences until the desired length is reached.

One of the problems encountered when running the program was when words with more than 8 letters are entered, the program requests the entry of a new word and does not allow progress if the new word has fewer than 4 letters. To solve this problem, a "while" loop was introduced within the first "while" loop. This checks that the word does not have less than 4 letters, but also does not continue advancing if it has more than 8.

Part Two:

Using conditionals to locate a point in one of the quadrants of a Cartesian plane is not complex.

When running the program, I found that the most difficult part was organizing the conditionals so that even if the value 0 is entered in "x or y," it continues to work and requests whole numbers until one can be located in the quadrants of a Cartesian plane.

To solve this problem I introduced a check by multiplying the variable x and y, if either of these two variables is zero the automatic result of the check would be 0 and this check would be useful to introduce a "while" loop which can be passed until both values of x and y are different from zero.

By Brenda Mayén Almaguer
