""" Making Pseudocode real. Create the Pseudocode in Python.
By the way this is NOT a nice way to name your definitions in Python, but it 
lets you get away with it.
pass lets me not code up the function. It's like on a quiz show.
"""

def LEFT(string,length):   
    # returns the left most characters of a string. 
    # I've done this one as an example.
    return string[0:length]

def RIGHT(string,length):
    # Returns the right most characters of a string
    return string[-1:-length-1:-1]

def MID (string,start,end):
    # Returns string from position x, length y. Note that the count starts at 1.
    return string[start+1, end+1]

    
def LENGTH (string):
    return len(string)


def LCASE (string):
    return string.lower()
# From here on in you need to figure out the parameters and the function.    

    
def UCASE(string):
    return string.upper()
  #Returns the upper case character. (Does nothing if already upper case). Note that this works on characters rather than a string.

def TO_UPPER(string):
    return string.upper()
  #Returns a string in upper case. (Non-alphabetic characters and upper case characters remain unchanged)

 
def TO_LOWER(string):
    return string.lower()
  #Returns a string in lower case. (Non-alphabetic characters and lower case characters remain unchanged)


 
def NUM_TO_STRING(num):
    return str(num)


def STRING_TO_NUM(string):
    return float(string)


def INT(string):
    return int(string)


def ASC(char):
    return ord(char)
  #Changes a character into its ASCII number.


# example function being called


print(TO_LOWER('AB2dW'))
