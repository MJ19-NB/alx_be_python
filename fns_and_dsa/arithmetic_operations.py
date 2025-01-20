def perform_operation(num1, num2, operation):
    # Check for 'add' operation
    if operation == 'add':
        return num1 + num2
    # Check for 'subtract' operation
    elif operation == 'subtract':
        return num1 - num2
    # Check for 'multiply' operation
    elif operation == 'multiply':
        return num1 * num2
    # Check for 'divide' operation with zero division handling
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"

