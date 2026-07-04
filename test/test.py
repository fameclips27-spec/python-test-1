def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Function Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

pick = int(input("Pick an operation betweenn (1-4): "))

num1 = float(input("Enter first digit: "))
num2 = float(input("Enter second digit: "))
 
if pick == 1:
    print("Result:", add(num1, num2))
elif pick == 2:
    print("Result:", subtract(num1, num2))
elif pick == 3:
    print("Result:", multiply(num1, num2))
elif pick == 4:
    print("Result:",divide(num1, num2))
else:
    print("Invalid operation.")


except ValueError:
print("Error: Please enter valid numbers.")

except ZeroDivisionError:
print("Error")

