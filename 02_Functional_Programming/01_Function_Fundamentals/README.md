# Function Fundamentals: Building Modular Code

As your Python scripts grow larger, writing every line of code sequentially from top to bottom becomes unmanageable. Functional Programming introduces the concept of breaking your code into smaller, independent, and reusable blocks called functions.  

A function is essentially a mini-program within your script designed to do one specific job.

## Defining and Calling Functions

In Python, you define a function using the `def` keyword, followed by the function's name, parentheses `()`, and a colon `:`. The code block inside the function must be indented.

To execute the function, you must "call" or "invoke" it by writing its name followed by parentheses.

Basic Syntax & Example:

```python
# 1. Defining the function
def initialize_system():
    """
    This is a docstring (documentation string).
    It explains that this function prints a startup sequence.
    """
    print("Booting up...")
    print("System initialization complete.")
# 2. Calling the function
initialize_system()
```

**Naming Rule:** Just like variables, function names should be lowercase with words separated by underscores (`snake_case`). They should ideally begin with a verb since functions perform actions (e.g., `calculate_total`, `fetch_data`).

## Parameters and Arguments

Functions become truly powerful when you can pass data into them.

* **Parameter:** The variable listed inside the parentheses in the function definition.
* **Argument:** The actual value you pass into the function when you call it.
  
### Positional Arguments

By default, Python matches arguments to parameters based on their order (position).  

```python
def calculate_area(length, width):
    area = length * width
    print(f"The area is {area} square units.")

# 'length' becomes 10, 'width' becomes 5 based on their positions
calculate_area(10, 5) 
```

### Keyword Arguments

You can also explicitly state which parameter receives which value by using keyword arguments. When you use keyword arguments, the order in which you pass them no longer matters.  

```python
def configure_server(host, port, protocol):
    print(f"Server starting on {protocol}://{host}:{port}")

# Order does not matter because we are explicitly naming the parameters
configure_server(protocol="https", port=443, host="10.0.0.1")
```

## Setting Default Parameters

Sometimes, a parameter will usually have the same value, and you only want to change it occasionally. You can assign a default value to a parameter in the function definition.

If the user calls the function without providing an argument for that parameter, Python will automatically use the default.

```python
def ping_device(ip_address, retries=3):
    print(f"Pinging {ip_address} {retries} times...")

# We only provide the IP. The function defaults to 3 retries.
ping_device("192.168.1.50")

# We override the default by providing a specific number of retries.
ping_device("192.168.1.99", retries=5)
```

**Crucial Rule:** When defining a function, all parameters with default values must be placed at the very end of the parameter list, after all parameters without defaults.

* **Correct:** `def setup(name, age, status="Active"):`
* **Incorrect:** `def setup(status="Active", name, age):` (This will cause a SyntaxError)

## Managing Return Values

While a function can print output directly to the console, it is usually much better for a function to process data and hand the result back to the main program. This is done using the `return` keyword.  

When Python encounters a `return` statement, the function terminates immediately, and the specified value is sent back to the caller.

```python
def convert_currency(usd_amount, exchange_rate):
    converted = usd_amount * exchange_rate
    return converted
    
    # Any code written down here will NEVER execute because the function has already returned.
    # print("This will never print.")

# We must store the returned value in a variable to use it
euro_wallet = convert_currency(100, 0.92)
print(f"You have €{euro_wallet:.2f}")
```

### Returning Multiple Values

Unlike many other programming languages, Python allows you to return multiple values from a single function by separating them with commas. Python automatically packages them into a Tuple.

```python
def get_user_metrics():
    # Simulating data retrieval
    name = "Alice"
    age = 28
    is_active = True
    
    # Returning three distinct values
    return name, age, is_active

# "Unpacking" the returned values into three separate variables simultaneously
user_name, user_age, user_status = get_user_metrics()

print(f"Name: {user_name}, Age: {user_age}, Active: {user_status}")
```
