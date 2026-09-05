import os

def run_test():
    print("Running automated test for Blueprint Writer...\n")
    
    if not os.path.isfile('requirements.txt'):
        print("❌ Failed: Could not find 'requirements.txt'.")
        print("Did you run the 'pip freeze > requirements.txt' command?")
        return

    with open('requirements.txt', 'r') as f:
        content = f.read().lower()
        if 'cowsay' not in content:
            print("❌ Failed: The package 'cowsay' is missing from requirements.txt.")
            print("Make sure you 'pip install cowsay' BEFORE running 'pip freeze'.")
        else:
            print("✅ Found 'cowsay' explicitly listed in the requirements file.")
            print("\n🏆 All tests passed! Your environment blueprint is ready to share.")

if __name__ == "__main__":
    run_test()