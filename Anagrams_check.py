"""
An anagram is the checking both strings as the same letters is not in order it was unorderwise is called anagrams.
Output:
Give the boolean value that was true or false.
"""
import re
from collections import Counter
def remove_unwanted_data(change_letter:str)->str:
    return re.sub(r"[^A-Za-z0-9]","",change_letter)
def is_anagram(letter1:str,letter2:str)->bool :
    change_letter1=remove_unwanted_data(letter1)
    change_letter2=remove_unwanted_data(letter2)
    return Counter(change_letter1)==Counter(change_letter2)
print(is_anagram("hello","olleh"))
print(is_anagram("name","name2"))
