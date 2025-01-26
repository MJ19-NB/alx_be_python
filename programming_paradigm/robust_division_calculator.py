# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convertir les entrées en float pour s'assurer qu'on travaille avec des nombres
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Effectuer la division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

