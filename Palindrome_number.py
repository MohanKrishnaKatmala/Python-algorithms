"""
A palindrome number is the forward order is equal to the reverse order is called palindrome numbers.
Input:
Take the input from the user as how much limit the user want.
Output:
Give the output of palindrome numbers up to users limit.
"""
def Palindrome_numbers():
    limit=int(input("enter a limit value "))
    total_numbers=0
    for input_number in range(limit):
        reverse_order=0
        same_number=input_number
        while(input_number!=0):
            remainder=input_number%10
            reverse_order=remainder+reverse_order*10
            input_number//=10
        if(same_number==reverse_order):
            print(same_number,end="  ")
            total_numbers+=1
    print()
    print(f"Total palindrome numbers from 0 to {limit} limit is {total_numbers} numbers.")
Palindrome_numbers()
