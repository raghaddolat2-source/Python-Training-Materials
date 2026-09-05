# ==========================================
# Task 2.1: The Planetary Weight Calculator
# ==========================================

# 1. Function definition with default parameter
def calculate_weight(mass, planet="Earth"):
    """
    Calculates the weight of an object on a given planet.
    mass: float/int representing kilograms
    planet: string representing the planet name (default is 'Earth')
    """
    if planet == "Earth":
        gravity = 9.8
    elif planet == "Mars":
        gravity = 3.71
    elif planet == "Jupiter":
        gravity = 24.79
    else:
        gravity = 0 # Fallback for unknown planets
        
    weight = mass * gravity
    
    # 2. Function returns the value instead of printing
    return weight


# 3. Execution and Testing
print("--- Planetary Weights for 100kg Mass ---")

# Calling using only a positional argument (relies on default "Earth")
earth_weight = calculate_weight(100)
print(f"Weight on Earth: {earth_weight} N")

# Calling using positional arguments
mars_weight = calculate_weight(100, "Mars")
print(f"Weight on Mars: {mars_weight} N")

# Calling using explicit keyword arguments
jupiter_weight = calculate_weight(planet="Jupiter", mass=100)
print(f"Weight on Jupiter: {jupiter_weight} N")