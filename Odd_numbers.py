"""
A odd number is the not divisible by 2 are called odd numbers.
Input:
Take the input from the user for to generate the odd numbers up to limit.
Output:
Give the list of odd numbers.
"""
def odd_numbers():
    limit=int(input("enter a limit value "))
    total_numbers=0
    for input_number in range(limit+1):
        if(input_number%2!=0):
            print(input_number,end="  ")
            total_numbers+=1
    print()
    print(f"Total odd numbers from 0 to {limit} limit is {total_numbers} numbers.")
odd_numbers()    
