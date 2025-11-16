"""
The Armstrong numbers are the length of the number is power raised to the individual number and their sum is equal to the original number is called Armstrong number.
Inputs:
Take the input from the user to set the limit value.
Output:
Give the result of the list of the armstrong numbers.
"""
def Armstrong_number():
    limit=int(input("enter a limit value "))
    total_numbers=0
    for input_number in range(limit):
        sum_power=0
        same_number=input_number
        while(input_number!=0):
            remainder=input_number%10
            sum_power+=pow(remainder,len(str(same_number)))
            input_number//=10
        if(sum_power==same_number):
            print(same_number,end="  ")
            total_numbers+=1
    print()
    print(f"The total Armstrong numbers from 0 to {limit} is {total_numbers} numbers.")
Armstrong_number()
