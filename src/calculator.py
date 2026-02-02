def add(a, b) # FIXME: SyntaxError: missing colon
    return a + b

def subtract(a, b):
    # FIXME: LogicError: returns wrong result
    return a + b 

def divide(a, b):
    # FIXME: ZeroDivisionError: what if b is 0?
    return a / b

def multiply(a, b):
    # FIXME: TypeError: what if input is string '10'?
    return a * b

def calculate_average(numbers):
    total = sum(numbers)
    # FIXME: NameError: variable 'count' is not defined (should be len(numbers))
    return total / count 
