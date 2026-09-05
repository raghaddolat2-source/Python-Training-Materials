# Variable Scoping

The LEGB RuleIn Python, just because you define a variable does not mean you can access it from anywhere in your script. The specific region of code where a variable is visible and accessible is known as its Scope.  

Understanding scope is critical because it dictates a variable's "lifetime" (when it is created in memory and when it is destroyed) and prevents variable name collisions in large programs.

## The LEGB Resolution Order

When you use a variable name, Python does not just guess what you mean. It searches for that variable in four specific levels of scope, strictly in the following order: **Local**, **Enclosing**, **Global**, and **Built-in (LEGB)**. If it checks all four and finds nothing, it throws a `NameError`.  

1. **Local Scope (L)**

    Variables defined inside a function are local to that function. They are created when the function runs and are immediately destroyed when the function finishes returning its value.

    ```python
    def calculate_discount(price):
    discount_rate = 0.20  # Local variable
    return price - (price * discount_rate)

    print(calculate_discount(100))

    # This will crash! 'discount_rate' does not exist outside the function.
    # print(discount_rate) 
    ```

2. **Enclosing Scope (E)**

    This scope applies when you have nested functions (a function defined inside another function). The inner function can read variables defined in the outer (enclosing) function's local scope.

    ```python
    def server_status():
    status_message = "All systems operational."  # Enclosing scope variable
    
    def display_status():
        # The inner function can access the outer function's variable
        print(f"Status Update: {status_message}")
        
    display_status()

    server_status()
    ```

3. **Global Scope (G)**

    Variables defined at the top level of your script, outside of any functions, are in the Global scope. They can be read from anywhere in your code, including inside functions.

    However, if you want to modify a global variable from inside a function, you must explicitly declare it using the **global** keyword.

    ```python
    system_mode = "Dev"  # Global variable

    def switch_to_prod():
        global system_mode  # We must declare this to change the global variable
        system_mode = "Prod"
        print(f"Mode switched to {system_mode}")

    switch_to_prod()
    print(f"Current System Mode: {system_mode}")
    ```

4. **Built-in Scope (B)**

    If Python cannot find the variable in the Local, Enclosing, or Global scopes, it checks the Built-in scope. This contains pre-assigned names built directly into Python, such as print, len, int, and id.

    **Warning: Variable Shadowing**

    If you name a local or global variable the same as a built-in function, you will "shadow" (overwrite) it, breaking that tool for the rest of your script.  

    ```python
    # VERY BAD PRACTICE: Shadowing a built-in function
    # list = [1, 2, 3] 
    # Now if you try to use the actual list() function later, your program will crash!
    ```
