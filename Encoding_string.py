"""
Encoding a string as consecutive give the numbers of the sequence of that particular text.
Output:
Give the how many times that text or letter appears on the string in consecutive order.
"""
def Encoding_string(string):
    if(bool(string)):
        length=len(string)
        count=1 # Here count letter of the string.
        result="" # create a place holder.
        for index in range(1,length):
            if(string[index]==string[index-1]):
                count+=1
            else:
                result+=string[index-1]+str(count)
                count=1
        return result+string[-1]+str(count)
    else:
        return "There is no text in string."
string="name"
print(Encoding_string(string))
