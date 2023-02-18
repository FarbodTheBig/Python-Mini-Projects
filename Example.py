#main program function. 
def is_valid(s):
    stack = []
    mapping = {")":"(","}":"{","]":"["}
    #main loop that contains a basic mapping algorithm.
    for char in s :
        if char in mapping :
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element :
                return False 

        else : 
            stack.append(char)
            
    return not stack 

#starting to get the input from user.

s = input("Enter a string containing barackets: ")
if is_valid(s):
    print(f"{s} is valid")
else :
    print(f"{s} is not valid")
    

