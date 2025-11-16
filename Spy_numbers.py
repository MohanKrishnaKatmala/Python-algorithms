"""
A spy number was the sum of the digits and product of the digits of original numbers are same is called Spy number.
Input:
Take the input from the user the numbers want up to that enter input limit.
Output:
Give the output of the list of spy numbers up to that input limit.
"""
def Spy_numbers():
    limit=int(input("enter a limit value "))
    total_numbers=0
    for input_number in range(limit):
        summating=0
        producting=1
        same_number=input_number
        while(input_number!=0):
            remainder=input_number%10
            summating+=remainder
            producting*=remainder
            input_number//=10
        if(summating==producting):
            print(same_number,end="  ")
            total_numbers+=1
    print()
    print(f"The total Spy numbers from 0 to {limit} limit is {total_numbers} numbers.")
Spy_numbers()
