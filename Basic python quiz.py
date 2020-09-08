#Task 1: Adding machine
x= -1
y= 8
print(x+y)

#Task 2: Character count
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)



