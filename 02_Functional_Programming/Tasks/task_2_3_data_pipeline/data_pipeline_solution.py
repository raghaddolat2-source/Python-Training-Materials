# ==========================================
# Task 2.3: The Data Pipeline Purifier
# ==========================================

raw_sensor_data = [15.5, -2.0, 18.1, 0.0, -99.9, 22.4]

# 1. Filter: Keep only numbers greater than or equal to 0.0
# We use a lambda to define the condition inline, and list() to convert the filter object back to a list
valid_data = list(filter(lambda x: x >= 0.0, raw_sensor_data))

# 2. Map: Multiply the remaining valid readings by 1.5
# We use a lambda to apply the math operation to every item in the valid list
calibrated_data = list(map(lambda x: x * 1.5, valid_data))

# 3. Output
print(f"Original Raw Data:   {raw_sensor_data}")
print(f"Filtered Valid Data: {valid_data}")
print(f"Calibrated Data:     {calibrated_data}")