# tail recursion is a form of recursion in which the recursive 
# call is the last operation in the function. This is important for efficiency reasons.
# Some languages or compilers (like in functional languages) can recognize tail recursion 
# and optimize the recursive calls to avoid growing the stack, this optimization is 
# called Tail Call Optimization (TCO).

# Python does not support Tail Call Optimization out of the box 
#and would generate a RecursionError for large inputs. 
# But we can still write tail-recursive functions in Python.

def factorial(n, accumulator=1):
    if n == 0: 
        return accumulator
    else:
        return factorial(n-1, n * accumulator)

print(factorial(998))  
