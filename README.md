
***Journey Through Pahoa v1.0 Game (README.txt)***

Note: The actual separate README file is included in the collection of files above. I am including this readme along with the other readme files so that they can all be in one place for your convenience.


***GENERAL INFORMATION***

"Journey Through Pahoa" is a short text-based adventure game centered around making a series of decisions in order to make it out of the wilderness alive and back home safe and sound.

"Journey Through Pahoa" is posted on Github, and distributed manually via Noble Bautista and other owners of "Journey Through Pahoa" including National Louis University.

"Journey Through Pahoa" uses no external services, and exclusively operates on the Python coding language.


***SYSTEM REQUIREMENTS***

"Journey Through Pahoa" is capable of operating on any computer capable of running the Python coding language. If python is not installed, please visit https://python.org to download.

To run "Journey Through Pahoa," Run Main.py. All other files are submodules that Main.py uses in order for the game to run. 

While playing, the user will be given a series of written passages and scenarios that will be paired with input prompts. 

As the user answers these prompts, they will traverse the game by either succeeding and moving forward in the chapters, being temporarily sent back to previous chapters, or terminated all together depending on their selection.


***CODE INFORMATION***

The structure of "Journey Through Pahoa" is fundamentally reliant on rudimentary Python coding structures. 

Overall, it is based on functions that include a series of if and while statements that are programmed to run differently depending on the user's selection.

Below is a list of each .py file within the "Journey Through Pahoa" game with a brief description of their purpose/function.


***Main.py: loads Main() which calls game_intro() within function.

***Chapter1.py: loads Main1() which calls Chapter1_intro. Includes references to four other possible results (functions) 

***Chapter2.py: loads Main2() which calls Chapter2_intro. Includes references to four other possible results (functions)

***Chapter3.py: loads Main3() which calls Chapter3_intro. Includes references to four other possible results (functions)

***Chapter4.py: loads Main4() which calls Chapter4_intro. Includes references to three other possible results (functions), which include more options within said functions

**Chapter5.py: loads Main5() which calls Chapter5_intro. Includes references to three other possible results (functions), which include more options within said functions


***gameover.py: The module that is referenced whenever a player choses an option that terminates their journey.


***MODULE 9***

Coding assignments for Module #9's lab assignment. Assignments consisted of using while loops in order to test infinite, indefinite and definite iteration. Below are the file names and descriptions to follow along with more clarification.


• Module9_Problem1.py: Write an infinite loop that prints “Infinite”. An infinite loop never ends. The condition is always true. 

• Module9_Problem2.py: Using a while loop, create a list called L that contains the numbers 0 to 10. On each iteration, the loop should append the current value of a counter variable to the list and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.

• Module9_Problem3.py: Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100.

• Module9_Problem4.py: Create a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens. Confirm the list results using a print statement.

***MODULE 8***

Coding assignments for Module #8's lab assignment. Assignments consisted of using functions and boolean algebra in order to test different problems. Below are the file names and descriptions to follow along with more clarification.


• Mod8Prob1.py: Two numbers are randomly generated between 1 and 20 (boundary inclusive). To test for equality, write a function that returns True if two numbers are equal and False otherwise. The program repeats until two identical numbers are produced. Once equal, it prints the two numbers as well as the number of times the function called. 

• Mod8Prob2.py: Write a function that takes three inputs from a user and prints the largest number without using max(). Generate three integer values using random.randint(1, 30)

• Mod8Prob3.py: Write a function that takes a list containing five numbers generated by random.randint(1, 5) and prints whether the value 4 is in that list.

• Mod8Prob4.py: Write a function that takes each element of a list called years and returns True if it is a leap year or False otherwise. Create a list of leap years that includes leap years only after checking each element of the list years. Your result should be checked with the calendar.isleap() function.

• Mod8Prob5.py: Write a function that prints “All items are ready.” if your game character has picked up all the items needed to perform certain task. And checks the character’s defuff state is the same as that of the task.


***MODULE 7***

Coding assignments for Module #7's lab assignment. Assignments consisted of testing out creating and using Python functions, many of them being user defined functions that used for loops and imported modules to streamline coding (i.e. math, random, turtle, etc). Below are the file names and descriptions to follow along with for more clarification.

• VolOfSphere.py (Problem 1): Write a function VolOfSphere(r) which returns the volume of a sphere of radius r. Make sure you use the math module in your solution.

• CheckRange.py (Problem 2): Write a Python function CheckRange(number) to check whether a number is in a given range (1, 10). The number should be randomly generated 20 times in the range (1, 15). Print how many times a number is in a given range.

• SumOfFood.py (Problem 3): Write a Python function SumOfFood(foodDict) that sums the price of each food item in a dictionary. Use foodDict = {“Pizza”: 3.50, “Sandwich”: 5.30, “Hamburger”: $9.45, “Spaghetti”: 5.75}

• Unique.py (Problem 4): Write a Python function Unique(lst) that takes a list of numbers and returns a new list with unique elements of the given list. Use lst = [1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]. Use the append function to create a new list where elements are unique. The count function should not be used to identify elements that appear more than once in a list.

• Squares.py (Problem 5): Write a Python function Squares(t, sz) using the following chunk of code as a base to produce the image shown. Assume the innermost square is 20 units per side, and each successive square is 20 units bigger per side, than the one inside it. below. Use t as an instance of turtle object and sz as length of each side.

• Flower.py (Problem 6): Write a Python function Flower(t, sz) using the polygon program from the last module. Call the function in a way to create a pattern similar to below. Use t as an instance of turtle object and sz as length of each side.

***MODULE 6***

Coding assignments for Module #6's lab assignment. Assignments consisted of testing out common Python modules, including Random & Math. Below are notes to follow along for more clairfication for each file.

•	Problem 1 – randomrange.py: Use a for statement and random.randrange to print 10 random integers between 25 and 35. 

•	Problem 2 – randomint.py: Use random.randint to print an odd integer between 0 and 100.

•	Problem 3 – randomday.py: Use random.choice to select a day of the week from a list and print that day. 

•	Problem 4 – pi.py: Calculate an approximation for pi using Leibniz’s formula, which is one of algorithms calculating the mathematical constant pi. Write a program that approximates π  according to the Leibniz’s formula using the following pseudo codes. Then compare the result with the value of math.pi in the math module.

•	Problem 5 – degrees.py:Convert radians to degrees using 2π rad = 360°. Write a program to convert a user input value in radians to the value in degrees. Print this value to compare it to a value computed using the degrees function in the math module for the same input value.

•	Problem 6 – factorial.py: Write a program that uses a for loop to compute the factorial of a user input value. Print the result to compare to be compared with the calculated value using the factorial function in the math module. 

***MODULE 5***

Coding assignments for Module #5's lab assignment. Assignments consisted of testing out for loops, as well as creating turtle designs/drawings. Below are notes to follow along for more clairfication for each file.

-Problem1_Mod5Lab.py
o	Consider a program that asks the user to enter a number and prints “Hello World” by that number. 

-Problem2_Mod5Lab.py
o Assume you have a list of numbers 4, 10, 13, 3, 6, 7, 42, 9, 20. Write a loop that prints each of the numbers on a new line.

-Problem3_Mod5Lab.py
o Consider a program that prints the integers from 1 to 50. If a number is multiples of three, then prints “Divisible by three” instead of printing the number and for the multiples of seven prints “Divisible by seven”. For numbers which are multiples of both three and seven print “Divisible by both”.  

-Problem4_Mod5Lab.py
o Write a program that asks the user for the number of sides, the length of the side, the color of the line, and the fill color of a regular polygon. The program should draw the polygon and then fill it with the user inputted color. 

-Problem5_Mod5Lab.py
o Choose one of the following drawings. Then write a program to draw what you choose with the turtle methods provided in Summary of Turtle Methods (Picture chosen: five rings in different colors; International Olympics logo).

***MODULE 4***

Coding assignments for Module #4's lab assignment. This was a debugging assignment for Python code. Descriptions of each project are in commentary within select code Below are notes with the amout of errors found along with the specific type of error.

-	collections.py
o	#Of Errors: FIVE (5)
o	Error Types (each): Variable Error (misspelled), Syntax Error (Ending bracket missing/in wrong place), Syntax Error (missing comma), Syntax Error (parenthesis), Syntax Error (print statement (commas, unnecessary operators)).

-	branching.py
o	#Of Errors: SIX (6)
o	Error Types (each): Syntax Error (period instead of parenthesis), Syntax error (wrong operator used), Syntax Error (no colon), Syntax Error (quotations), Syntax Error (incorrect operator), Value Error (elif statement formula missing).

-	grading.py
o	#Of Errors: SIXTEEN (16)
o	Error Types (each): Syntax Error (unmatched parenthesis (did not call integer properly)), Variable Error (exam_3 should be exam_three), Syntax Error (should call int not str), Syntax Error (missing commas when defining “grades” variable),  Syntax Error (missing colon in elif statement),  Syntax Error (missing quotations around “C”), Syntax Error (incorrect operator used for B grade parameters), Syntax Error (missing function for elif statement for F grade), Value Error (Elif statement parameters for C grade), Value Error (elif statement parameters for D grade), Syntax Error (missing parenthesis in call to print), Syntax Error (again, missing parenthesis in call to print), Syntax Error (wrong operator (used “is” instead of “==”)),Variable Error (grades is misspelled), Variable error (grade should have been grades), Variable Error (Letter-grade should have been Letter_grade)

-	pirate.py
o	#Of Errors: FOUR (4)
o	Error Types (each): Syntax Error (missing quotations), Syntax Error (opening brackets did not match closing parenthesis), Value Error (elif statement should be an else statement), Syntax Error (properly indent print statement for else statement).

-	time2.py
o	#Of Errors:
o	Error Types (each): Value Error (hours misspelled), Value Error (“wait_time” variable misspelled), Value Error (“time_when_to_start” variable does not exist, should print “time_when_start”)

***MODULE 3***

List of all Module 3 lab problems with their descriptions (clarifying commentary will be in code files):

Problem 1 – Write a program that prints your name with a greeting message. 

Problem 2 – Write a program that prints three items, such as your name, your favorite movie, the city name you live in. 

Problem 3 – Write a program that prints the sum of the first ten positive integers, 1 + 2 + 3 + 4 +
5 + …+ 9 + 10.  

Problem 4 - Write a program that computes the area of a circle. Prompt the user to enter the radius and print the answer with a nice message. 

Problem 5 - Write a program that computes the MPG (Miles per Gas) for a car. Prompt the user to enter the number of miles driven and the number of gallons it used. Print the answer with a message. 

Problem 6 - Write a program that prints the balance of an account after the first, second, and third year. The account has an initial balance of $1,000 and earns 5 percent interest per year. 

Problem 7 - It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (Wednesday) and you return home after 10 nights, then you would return home on Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of the day you will return on. 

Problem 8 – Write a program that prints a house that looks exactly like the following (see problem 8 code file)
