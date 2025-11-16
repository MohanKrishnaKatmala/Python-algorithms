"""
The fibonacci series wws the sum of the previous digits give the next digit is called fibonacci series.
This was the basic series in a using the end.
Inputs:
Taking the input from the user to print how many numbers user want.
Output:
Give the output of fibonacci series numbers.
"""
def fibonacci_series_normal(first_number=0,second_number=1):
  limit=int(input("enter a limit value "))
  print(first_number,end="  ")
  print(second_number,end="  ")
  total_numbers=2
  for a in range(limit-2):
    next_digit=first_number+second_number
    print(next_digti,end="  ")
    total_numbers+=1
    first_number=second_number
    second_number=next_digit
fibonacci_series_normal() # It takes the two parameters that was the first and last of the how many fibonacci series you want.By default that was first as 0 and second was the 1.         
