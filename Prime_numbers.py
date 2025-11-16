"""
A prime number is the it has the two factors one was its own number and another one was common factor to all that was 1.
0 and 1 are not prime numbers and composite numbers.
Input:
Take the input from the user for the input limit prime numbers were generate.
Output:
Give the prime numbers list up to limit.
"""
def Prime_number():
    limit=int(input("enter a limit value  "))
    total_numbers=0
    for input_number in range(1,limit+1):
        count=0
        for divider in range(1,input_number+1):
            if(input_number%divider==0):
                count+=1
        if(count==2):
            print(input_number,end="  ")
            total_numbers+=1
    print()
    print(f"Total prime numbers from 0 to {limit} limit is {total_numbers} numbers.")
Prime_number()
