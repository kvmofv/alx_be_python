
def safe_divide(x, y):
    try:
        x = float(x)
        y = float(y)

    except ValueError:
        return "Error: Please enter numeric values only."


    try:
       result = x / y
       return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
