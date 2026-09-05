# Exception Handling: Building Robust Applications

In a perfect world, code executes exactly as intended. In the real world, users input text when you ask for numbers, network connections drop, and files go missing. When Python encounters an error it doesn't know how to handle, it raises an Exception and completely crashes the program.

To build professional, robust applications, you must anticipate these failures and handle them gracefully using `try`, `except`, `else`, and `finally` blocks.

## The Core Blocks: `try` and `except`

The fundamental concept of exception handling is "trying" a block of code. If an error occurs, instead of crashing, Python diverts the flow to the `except` block.

```python
# Unsafe approach (will crash if user types "five")
# age = int(input("Enter your age: ")) 

# Robust approach
try:
    age_str = input("Enter your age: ")
    age = int(age_str)  # This line might throw a ValueError
    print(f"You are {age} years old.")
except ValueError:
    # This code ONLY runs if a ValueError occurs in the try block
    print("Error: Please enter a valid whole number, not text.")
```

## Catching Multiple Specific Exceptions

A common mistake is using a "bare" `except:` block (one without a specific error type). This is considered a bad practice because it hides bugs by catching *everything*, including typos in your code.

Instead, you should catch specific exceptions so you can respond to different failures appropriately.

```python
def calculate_ratio(total, count):
    try:
        ratio = total / count
        return ratio
    except ZeroDivisionError:
        return "Calculation Error: Cannot divide by zero."
    except TypeError:
        return "Type Error: Both inputs must be numerical."

# Testing the different error branches
print(calculate_ratio(100, 0))         # Triggers ZeroDivisionError
print(calculate_ratio(100, "apple"))   # Triggers TypeError
```

## The Full Pipeline: `else` and `finally`

For complex operations like reading files or querying databases, you need more control over the execution flow. Python provides two additional optional blocks:

* **else:** Runs only if the `try` block succeeds completely without raising any exceptions.
* **finally:** Runs always, regardless of whether the code succeeded or failed. It is heavily used for cleanup actions, like closing files or disconnecting from databases.

```python
def process_sensor_data(data_string):
    print("Attempting to parse sensor data...")
    
    try:
        data_value = float(data_string)
        
    except ValueError:
        print("Failure: Sensor data is corrupted.")
        
    else:
        # This only executes if the float conversion succeeds
        print(f"Success: Valid data parsed ({data_value}). Logging to system.")
        
    finally:
        # This executes no matter what happens above
        print("Closing sensor connection.\n")

# Scenario 1: Clean Data
process_sensor_data("98.6")

# Scenario 2: Corrupted Data
process_sensor_data("N/A")
```
