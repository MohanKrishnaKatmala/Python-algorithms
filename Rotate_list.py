"""
This was the rotate the list in number of times.
Output:
Give the rotation of the list.
"""
def rotate_list(outside_list,rotate_number):
    for _ in range(rotate_number):
        store_last=outside_list[-1]
        for index in range(len(outside_list)-1,0,-1):
            outside_list[index]=outside_list[index-1]
        outside_list[0]=store_last
    return outside_list    

outside_list=[1,2,3,4,5]
rotate_number=2
print(rotate_list(outside_list,rotate_number))
