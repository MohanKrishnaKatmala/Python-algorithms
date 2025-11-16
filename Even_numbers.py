"""
A even number is the divisible by 2 is called is a even number.
0 is also a even number.
Input:
Take the input from the user for input limit for even numbers generate.
Output:
Give the list of even numbers up to limit.
"""
def even_numbers():
    limit=int(input("enter a limit value "))
    total_numbers=0
    for input_number in range(limit+1):
        if(input_number%2==0):
            print(input_number,end="  ")
            total_numbers+=1
    print()
    print(f"Total even numbers from 0 to {limit} limit is {total_numbers} numbers.")
even_numbers()
