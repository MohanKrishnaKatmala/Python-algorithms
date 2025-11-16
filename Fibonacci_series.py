''' 
Fibonacci series is the add the previous two  numbers get th third digit is called Fibonacci series.
This was the add the fibonacci series in the right angle triangle shape.
Fibonacci series was the continuous one that should be the definitely get the output for every loop instance so here thtat the right angle shape was happen to that fibonacci series.
Start numbers are 0 and 1. 
This series was the lines based give output.
'''
def fibonacci_series(first_number=0,second_number=1):# no parameters nut can give for the where you start from the add.
  # starting numbers.
  print("convey that add the first and second numbers at frist so when give limit was increased by 2.")
  limit=int(input("enter a limit value that was lines not the numbers."))
  print(first_number) # This to add the next number to end as the space as two words space.
  print(second_number)
  actual_limit=limit+2
  total_numbers=2 # This is to get total numbers in that right angle triangle shpae numbers.
  save_first=first_number
  save_second=second_number
  for a in range(limit):
    first_number=save_first
    second_number=save_second
    for b in range(a+1):
      summating=first_number+second_number
      print(summating,end="  ")
      total_numbers+=1
      first_number=second_number
      second_number=summating
    print() # This like the add a new line for after one inner loop execution.
  print()
  print(f"The total fibonacci series numbers are the {total_numbers} in the lines of the {actual_limit} lines.")
# calling the function
fibonacci_series()
