"""
Finding the sum is in their in list or not in consecutive order.
The list contains the digits only.
The consecutive order can check the sum.
Output:
If there is a sum give that numbers as output.
"""
def find_the_sum(outside_list,sum_value):
    for index in range(len(outside_list)):
        result=0
        for sub_index in range(index,len(outside_list)):
            result+=outside_list[sub_index]
            if(result==sum_value):
                print(outside_list[index:sub_index+1])
        
outside_list=[1,2,3,4,5]
sum_value=9
find_the_sum(outside_list,sum_value) # Here there is no return on explicitly in that function.So here give print() function will give the None so i avoid it.Actually i write thte print() in function so here then again write will have the None also represent at output.So avoid at in calling in this point.
