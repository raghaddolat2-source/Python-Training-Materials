import os

def run_test():
    print("Running automated test for Project Skeleton...\n")
    all_passed = True

    # 1. Check directories
    for folder in ['src', 'tests']:
        if not os.path.isdir(folder):
            print(f"❌ Failed: Could not find the '{folder}' directory.")
            all_passed = False
        else:
            print(f"✅ Found '{folder}' directory.")

    # 2. Check .gitignore and its contents
    if not os.path.isfile('.gitignore'):
        print("❌ Failed: Could not find the '.gitignore' file.")
        all_passed = False
    else:
        with open('.gitignore', 'r') as f:
            content = f.read()
            if 'venv/' not in content and 'venv' not in content:
                print("❌ Failed: '.gitignore' is missing the 'venv/' rule.")
                all_passed = False
            elif '__pycache__' not in content:
                print("❌ Failed: '.gitignore' is missing the '__pycache__' rule.")
                all_passed = False
            else:
                print("✅ Found '.gitignore' with correct rules.")

    if all_passed:
        print("\n🏆 All tests passed! Your project structure looks professional.")

if __name__ == "__main__":
    run_test()