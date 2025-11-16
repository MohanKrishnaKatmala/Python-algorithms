"""
A composite number is the it has the more than two factors is called composite numbers.
Not prime numbers are called composite numbers.
0 and 1 are not a composite and prime number.
Input:
Take the input from the user for limit number to generate the composite numbers.
Output:
Give the list of the composite numbers.
"""
def composite_numbers():
    limit=int(input("enter a limit value "))
    total_numbers=0
    for input_number in range(1,limit+1):
        count=0
        for divider in range(1,input_number+1):
            if(input_number%divider==0):
                count+=1
        if(count>2):
            print(input_number,end="  ")
            total_numbers+=1
    print()
    print(f"Total prime numbers from 0 to {limit} limit is {total_numbers} numbers.")
composite_numbers()    
