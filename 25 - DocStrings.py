# Koi bohott special nahi hai, Helps us understand te function correctly.
# Docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) #Python gives special treatment to the comment after function. It can be printed as well.

# Comments are different, since it also helps programmers understand the intent and functionality of a program. But completely ignored by Python interpreter.
# Docstrings on the otherhand are used after the function, method, class, or module. Used to document our code. Just function ke baad wali line mein.
# Valid docstring is right below the function name, or right above the function body.

# PEP 8: Document that provides guidelines and practices on how to write Python code.
#ZEN OF PYTHON- (import this - in CMD - for an amazing poem - Easter egg)