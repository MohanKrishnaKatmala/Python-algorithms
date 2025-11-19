"""
This was the find the longest substring in the string.
The substring was the consecutive text in the string.
Output:
Give the max substring and its length of the number.
"""
def longest_substring(string):
    seen=set()
    left=0
    max_length=0
    start=0
    for right in range(len(string)):
        while(string[right] in seen):
            seen.remove(string[left])
            left+=1
        seen.add(string[right])
        if(right-left+1>max_length):
            max_length=right-left+1
            start=left
    return max_length,string[start:max_length+start]        
string="starringly"
max_length,longest_substring=longest_substring(string)
print(max_length,longest_substring)
