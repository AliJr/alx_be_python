def safe_divide(numerator, denominator):
    """Performs division while handling division by zero and non-numeric inputs."""
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Try dividing, handle division by zero
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."