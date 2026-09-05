import sys

def run_test():
    print("Running automated test for Blueprint Reader...\n")
    
    # Check if they are running this inside a venv by looking at sys.prefix
    if sys.prefix == sys.base_prefix:
        print("❌ Failed: Virtual environment is NOT activated.")
        print("Please activate your venv (e.g., 'source venv/bin/activate' or 'venv\\Scripts\\activate') and try again.")
        return

    try:
        # Try importing the third-party libraries they were supposed to install
        import requests
        import colorama
        
        # Verify the specific version of requests if possible
        if requests.__version__ != "2.31.0":
            print(f"⚠️ Warning: Found requests version {requests.__version__}, but expected 2.31.0.")
            print("Did you install directly from the requirements.txt file?")
        else:
            print("✅ Found exact requests version (2.31.0).")
            
        print("✅ Found colorama.")
        print("\n🏆 All tests passed! You successfully recreated the environment.")
        
    except ImportError as e:
        print(f"❌ Failed: Could not import a required package. Error details: {e}")
        print("Did you run 'pip install -r requirements.txt'?")

if __name__ == "__main__":
    run_test()