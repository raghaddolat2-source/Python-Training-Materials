# ==========================================
# Task 2.4: The Unbreakable Calculator
# ==========================================

print("--- The Unbreakable Division Calculator ---")

try:
    # Attempting dangerous operations that rely on user input
    numerator_str = input("Enter the numerator (top number): ")
    denominator_str = input("Enter the denominator (bottom number): ")
    
    numerator = float(numerator_str)
    denominator = float(denominator_str)
    
    result = numerator / denominator
    
except ValueError:
    # Catches inputs that cannot be cast to a float (e.g., text)
    print("Error: Please enter numbers only.")
    
except ZeroDivisionError:
    # Catches mathematical impossibility
    print("Error: Cannot divide by zero.")
    
else:
    # Executes ONLY if the try block succeeds perfectly
    print(f"Success! The result is {result}")
    
finally:
    # Executes ALWAYS, acting as our cleanup/closing step
    print("Calculation attempt complete.")