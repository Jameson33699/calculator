print("--------Calculator--------")
print("select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

op = (input("Enter your operation: "))

if op == '1':
    num1 = int(input("First value: "))
    num2 = int(input("Second value: "))
    result = num1 + num2
    result = str(result)
    print("the result is " + result)
elif op == '2':
    num1 = int(input("First value: "))
    num2 = int(input("Second value: "))
    result = num1 - num2
    result = str(result)
    print("the result is " + result)
elif op == '3':
    num1 = int(input("First value: "))
    num2 = int(input("Second value: "))
    result = num1 * num2
    result = str(result)
    print("the result is " + result)
elif op == '4':
    num1 = int(input("First value: "))
    num2 = int(input("Second value: "))
    result = num1 / num2
    result = str(result)
    print("the result is " + result)
else:
    print("invalid operation")