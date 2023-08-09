	EXAMPLE TEMPLATE.
	
    QUESTION (The Problem to Solve)
	Write a program in Python that calculates the factorial of a number.

STEP 1	UNDERSTAND THE PROBLEM
	What are we trying to solve?
	We want to get the value of a number (n = n X n-1 X .. X1)
	What are the input?
	5
	What are the output?
	120
STEP 2	BRAINSTORM POSSIBLE SOLUTIONS
	(What programming concept to use to solve the problem)
	We could use a recursive function to calculate the factorial.
	We could use a loop to calculate the factorial.
	We could use a table to store the factorials of all numbers from 0 to n.

STEP 3	CHOOSE A SOLUTION TO IMPLEMENT
	Chosen option
	We choose recursive function to solve the problem
	Why do we chose this option?
	
STEP 4	TEST SOLUTION WITH ALGORITHM 
	(Step by step approach to solution)
	Get a number n. (in this case 5 is our n)
	Multiply the number n by n-1 till n = 1 i.e 5 X 4 X 3 X 2 X 1
	Your final answer is the factorial

STEP 5	TRANSLATE THE ALGORITHM INTO A PSEUDOCODE 
	(Explain the solution)
	Import required libraries
	using math libraries it has the factorial function
	
	define factorial function for n 
	Condition n is equal to 0
	Then return 1
	Else
	Return n X factorial(n - 1)

STEP 6	TRANSLATE THE ALGORITHM'S PSEUDOCODE INTO A CODE OF THE REQUIRED PROGRAMMING LANGUAGE
	(Write your code)
	PYTHON
	Import math
	
	Def factorial(n): 
	if n == 0: 
	        return 1 
	else: 
	        return n * factorial(n - 1)

STEP 7	TEST CODE 
	(Compile the code to test for failure or success)
	Passed
	fail
    
STEP 8	DEBUG CODE
	(If code doesn't work, try and fix it)
	Copy your code here and highlight what you fixed
	
STEP 9	REFACTOR YOUR SOLUTION
	(Make it readable, concise and easier it understand able)
	
