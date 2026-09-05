# Lambda & Higher-Order Functions

In Python, you will often encounter situations where you need a simple function for a brief moment, usually to pass into another process. Instead of writing a full `def` block, you can use **lambda expressions** to write inline, anonymous functions.  

## The Lambda Syntax

A lambda function is a small, throwaway function that does not have a formal name. It can take any number of arguments but is strictly limited to one single expression.

**Syntax:** `lambda arguments: expression`

```python
# Traditional function approach
def square_number(x):
    return x * x

# Equivalent Lambda function approach
square_lambda = lambda x: x * x

print(square_lambda(5))  # Output: 25
```

## Higher-Order Functions

A higher-order function is simply a function that accepts another function as an argument. This is where lambdas truly shine. Instead of defining a function elsewhere in your script, you can inject the logic directly inline using a lambda. Two of the most powerful higher-order functions built into Python are `map()` and `filter()`.  

## Dynamic Processing with `map()`

The `map()` function applies a specified function to every individual item within an iterable (like a list) and returns a new sequence with the modified data.  

**Syntax:** `map(function, iterable)`

**Note:** `map()` returns a "map object", so you usually need to cast it back into a `list()`.

```python
raw_prices = [10.0, 25.0, 50.0]

# Apply a 5% tax to every price in the list dynamically
taxed_prices = list(map(lambda price: price * 1.05, raw_prices))

print(taxed_prices)  # Output: [10.5, 26.25, 52.5]
```

## Data Extraction with `filter()`

The `filter()` function evaluates every item in an iterable against a specific condition. It keeps only the items where your lambda function evaluates to `True` and discards the rest.

**Syntax:** `filter(function, iterable)`

```python
sensor_readings = [12, -5, 18, -2, 30]

# Filter out any negative error readings from the sensor stream
valid_readings = list(filter(lambda x: x >= 0, sensor_readings))

print(valid_readings)  # Output: [12, 18, 30]
```
