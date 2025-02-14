def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle the error in another suitable way

result = function(10, 0)
print(result) # Output: 0