"""
Missing a number to find in a consecutive way.
Output:
Get the missing number.
"""
def find_missing_number(outside_list):
    import math
    length=len(outside_list)
    actual_sum=(length+1)/2*(length+2) # Here length was the +1 increase for the missing number count.
    give_sum=sum(outside_list)
    return f"The missing number in the list {outside_list} was {math.floor(actual_sum-give_sum)}."
outside_list=[1,2,3,5] # missing number was 4.
print(find_missing_number(outside_list))
