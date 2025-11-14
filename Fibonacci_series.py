# Fibonacci series is the add the previous two  numbers get th third digit is called Fibonacci series.
# This was the add the fibonacci series in the right angle triangle shape.
# Fibonacci series was the continuous one that should be the definitely get the output for every loop instance so here thtat the right angle shape was happen to that fibonacci series.
# Start numbers are 0 and 1. 
def fibonacci_series(first_number=0,second_number=1):# no parameters nut can give for the where you start from the add.
  first_number=0
  second_number=1
  # starting numbers.
  print(first_number,end="  ") # This to add the next number to end as the space as two words space.
  print(second_number)
  total_numbers=2 # This is to get total numbers in that right angle triangle shpae numbers.
  limit=int(input("enter a limit value to print up to that lines  "))+1 # Here 0 and 1 should be display for the better output.
  for a in range(limit):
    for b in range(a+1):
      summating=first_number+second_number
      print(summating,end="  ")
      total_numbers+=1
      first_number=second_number
      second_number=summating
    print() # This like the add a new line for after one inner loop execution.
  print()
  print(f"The total fibonacci series numbers are the {total_numbers} in the lines of the {limit} lines.")
# calling the function
fibonacci_series()
      
      
  
  
  
