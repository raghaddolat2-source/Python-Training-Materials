while True:
    passworld=input("Enter a password to evaluate :")
    errors=[""]
    is_long=True if len(passworld)>=8 else False
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in passworld: 
        if char.isupper():
            has_upper =True
        
        elif char.islower():
            has_lower = True
    
        elif char.isdigit():
             has_digit = True
         
        elif char in "!@#$%^&*":
            has_special = True
       
    if not is_long:
        errors.append("  - Must be at least 8 characters long.")
    if not has_upper:
        errors.append("  - Must contain at least one uppercase letter.")
    if not has_lower:
        errors.append("  - Must contain at least one lowercase letter.")
    if not has_digit:
        errors.append("  - Must contain at least one digit.")
    if not has_special:
        errors.append("  - Must contain at least one special character (!@#$%^&).")

    if is_long and has_upper and has_lower and has_digit and has_special:
        print("Your password is valid.")
        break
    else:
        print(f"Your password is invalid. {', '.join(errors)} try again")
