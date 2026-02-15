def add(a, b): # FIXME: SyntaxError: missing colon
    return a + b

def subtract(a, b):
    # FIXME: LogicError: returns wrong result
    if a>b:
        return a - b
    else:
        return b - a 

def divide(a, b):
    # FIXME: ZeroDivisionError: what if b is 0?
    try:
        result = a / b
    except ZeroDivisionError:
        return "에러: 0으로 나눌 수 없습니다."
    else:
        return result

def multiply(a, b): #수정된 함수
    # FIXME: TypeError: what if input is string '10'? 
    return float(a) * float(b)

def calculate_average(numbers):
    total = sum(numbers)
    # FIXME: NameError: variable 'count' is not defined (should be len(numbers))
    return total / count 
