# ==========================================
# Task 2.2: Global Configuration Manager
# ==========================================

# 1. Global Scope Variable
system_env = "Development"

def deploy_to_production():
    # 2. Claiming access to modify the global variable
    global system_env 
    
    # An enclosing variable to demonstrate scope layers
    target_env = "Production" 
    
    # 3. Nested function utilizing the enclosing scope
    def log_deployment():
        # This function can read 'system_env' (Global) and 'target_env' (Enclosing)
        print(f"Deploying from {system_env} to {target_env}...")
        
    # Trigger the inner logging function
    log_deployment()
    
    # Change the global variable state
    system_env = target_env

# 4. Execution
print(f"Initial State: {system_env}")

deploy_to_production()

print(f"Final State: {system_env}")