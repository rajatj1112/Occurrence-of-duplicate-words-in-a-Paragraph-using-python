''' 
Program to find the duplicate elements in a 
Paragraph or a String along with displaying
number of occurences of the elements

'''

# Importing necessary modules

import math as ma 
from collections import Counter

sample_string = str(input("Enter a String to find duplicates : "))
sample_string1 = sample_string.lower() # Making it universal on a single lower case condition
length = len(sample_string1)

# Deleting unwanted elements in the string 

sample_string1 = sample_string1.translate({ord('.'): None})
sample_string1 = sample_string1.translate({ord(','): None})
sample_string1 = sample_string1.translate({ord('!'): None})
# sample_string1 = sample_string1.translate({ord("'"): None})

x = sample_string1.split()

counter = Counter(x)  # Counting Occurences
occur = counter.most_common(20) # List of tuples generated

var = occur[0][1]

list1 = []
list2 = []
i = 0
for i,j in enumerate(occur): # Loop for iterating through the list of tuples
    if j[1] == var:
        list1.append(j[0])
        list2.append(j[1])

a = 0   

# Printing duplicate elements along with their no of Occurences 

print("\nThe duplicate eliminates in the list are :\n")
for val in list1:
    print(val," Occuring ",list2[a]," time/times")
    a+=1










