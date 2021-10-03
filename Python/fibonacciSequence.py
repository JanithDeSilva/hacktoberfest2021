# This program will help you  to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms you need? "))

# first two terms
num1, num2 = 0, 1
count = 0

# will check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(num1)
# will generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(num1)
       nth = num1 + num2
       # update values
       num1 = num2
       num2 = nth
       count += 1
