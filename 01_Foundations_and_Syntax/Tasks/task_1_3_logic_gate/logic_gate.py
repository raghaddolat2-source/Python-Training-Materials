gates= input("chose AND, OR,NOT,XOR: ").strip().upper()
a= bool(int(input("enter value for A (1 or 0)"))).strip()
b= bool(int(input("enter value for B (1 or 0)"))).strip()
if gates != "NOT":
    
    b = bool(int(b))
else:
    b = None

if gates == "AND":
    reslt= a and b
    print(f"AND Gate Output: {result}")

elif gates == "OR":
    reslt= a or b
    print(f"OR Gate Output: {result}")

elif gates == "NOT":
    result = not a
    print(f"NOT Gate Output: {result}")

elif gates == "XOR":
    reslt= a != b
    print(f"XOR Gate Output: {result}")
    
else:
    print("Error: Unrecognized gate selected.")
  
