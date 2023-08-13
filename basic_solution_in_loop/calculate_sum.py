
# QUESTION(The problem)
# Create a loop that calculates the sum of numbers from 1 to 100.


# STEP 1: UNDERSTAND THE PROBLEM
#   What are we trying to solve?
#   We are trying to calculate the sum of 1 + 2 + .. + 50

#   What are the input?
#   The inputs we need is 100 in number i.e 1 to 100

#   What are the output?
#   The output is the sum of all the numbers from 1 to 100, which is 5050

 

# STEP 2: BRAINSTORM POSSIBLE SOLUTIONS
#(What programming concept to use to solve the problem)

#   We can use loop
#   We can use recursion
#   We can use dynamic programming
#   We can use mathematical formula n(n+1)/2, s = n/2[2a + (n - 1)d]


# STEP 3: CHOOSE A SOLUTION TO IMPLEMENT

#   We are using loop to solve the problem
#   for loop
#   while loop
#   do while loop


# STEP 4: ALGORITHM FOR THE SOLUTION
# (Step by step approach to solution)

#Algorithm for 'for' loops
#   Define a function
#   initialize the variable for the loop counter
#   Write the loop condition statements with mathematical formula to solve problem
#   Write the update statement
#   Return the final answer
#   Print the final answer on the console/terminal/screen

#Algorithm For 'while' loops
#   Define a function
#   Initialize the variable for the loop counter
#   Write the loop condition statements with mathematical formula to solve problem
#   Write the body of the loop.
#   Return the final answer
#   Print the final answer on the console/terminal/screen

#Algorithm For 'do while' loops
#   Define a function
#   initialize a the loop counter
#   Write the loop condition statements with mathematical formula to solve problem
#   Write the update statement
#   Return the final answer
#   Print the final answer on the console/terminal/screen

# STEP 5: TRANSLATE THE ALGORITHM INTO A PSEUDOCODE 
# (Explain the solution)

#Pseudocode for 'for' loops
#   define a function sum_of_numbers with an input n
#   Initialize a variable named 'sum' with the value of 0
#   use for loop for i
#   use range function to print (1, n + 1)
#   sum value is += i to update loop
#   return the value of sum
#   print function sum_of_numbers on the terminal

#Pseudocode for 'while' loops
#   define a function sum_of_numbers with an input n
#   initialize a variable named 'sum' with the value of 0
#   give variable 'i' a value of 1
#   set a while condition for i <= n
#   sum value is += i to update loop
#   Increment i for every loop until condition is met
#   print function sum_of_numbers on the terminal


#Pseudocode for 'do while' loops
#   define a function sum_of_numbers with an input n
#   initialize a variable named 'sum' with the value of 0
#   give variable 'i' a value of 1
#   set a 'do' condition
#   sum value is += i to update loop
#   Increment i for every loop until condition is met
#   set a while condition for i <= 10
#   print function sum_of_numbers on the terminal


#   STEP 6: TRANSLATE THE ALGORITHM'S PSEUDOCODE INTO A CODE OF THE REQUIRED PROGRAMMING LANGUAGE
#   (Write your code)

#For loop
def sum_of_numbers(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i
	return sum
print(sum_of_numbers(100))

# OR

#While Loop
#    def sum_of_numbers(n):
#	sum = 0
#	i = 1
#	while i <= n:
#		sum += i
#		i += 1
#	return sum
#    print(sum_of_numbers(100))

#do while loop
#	def sum_of_numbers(n):
#		sum = 0
#		i = 1
#		do:
#		  sum += i
#		  i += 1
#		while i <= n
#	print(sum_of_numbers(100))