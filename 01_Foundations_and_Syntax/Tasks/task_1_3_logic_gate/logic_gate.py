gates= input("chose AND, OR,NOT,XOR: ").strip().upper()
val_a=input("enter value for A (1 or 0)").strip()
val_b= input("enter value for B (1 or 0)").strip()
a = bool(int(val_a))

if gates != "NOT":
    
    b = bool(int(val_b))
else:
    b = None

if gates == "AND":
    result= a and b
    print(f"AND Gate Output: {result}")

elif gates == "OR":
    result= a or b
    print(f"OR Gate Output: {result}")

elif gates == "NOT":
    result = not a
    print(f"NOT Gate Output: {result}")

elif gates == "XOR":
    result= a != b
    print(f"XOR Gate Output: {result}")

else:
    print("Error: Unrecognized gate selected.")
