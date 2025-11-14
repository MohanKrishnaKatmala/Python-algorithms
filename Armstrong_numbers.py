# A armstrong number is the the length of the number is power raised to the individual digits and their sum is equal to the orginal number is called Armstrong number.
def Armstrong_numbers():
  limit=int(input("enter a limit value "))# numbers can give armstrong numbers up to this limit .
  total_numbers=0 # to count the total numbers.
  for input_number in range(limit): # This is to take the numbers from 0 to limit here limit-1 is the last value here limit is not take as last .
    summating=0 # initial sum it like placeholder for sum for further execution.
    same_number=input_number # when checking and get the length of the number input_number is changing in while loop so here store the input_number before go to while loop.
    while(input_number!=0): # the numbe is should be 0 or greater than 0 no negative numbers.
      remainder=input_number%10# This is to take the last number like 12/10 give the 2 remainder which was the number to take.
      summating+=pow(remainder,len(str(same_number))) # This is the main logic for the armstrong numbers.
      input_number//=10 # This like change the input_number for take the delete the last value take the rest .
    if(summating==same_number):  # check teh statement
      print(summating,end="  ") # print in a end with two blank space in between the numbers.
      total_numbers+=1 # this is to update the numbers to +1 every time add of the number.
  print()
  print(f"The total armstrong numbers up to limit {limit} is {total_numbers} numbers.")
Armstrong_numbers()
