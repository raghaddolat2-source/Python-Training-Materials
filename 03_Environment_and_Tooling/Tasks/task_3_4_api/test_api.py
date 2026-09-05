import subprocess
import sys

def run_test():
    print("Running automated test for API Consumer...\n")
    
    if sys.prefix == sys.base_prefix:
        print("⚠️ Warning: Virtual environment does not appear to be activated.")
        print("If this fails, activate your venv and try again.\n")

    try:
        process = subprocess.run(
            [sys.executable, "fetch_data.py"],
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout.strip()
        
        # Look for a successful 200 HTTP status code in their print statement
        if "200" in output:
            print(f"✅ Script executed successfully. Output: {output}")
            print("\n🏆 All tests passed! You have successfully consumed a third-party API.")
        else:
            print(f"❌ Failed: Expected to see status code '200' in the output, but got:\n'{output}'")

    except FileNotFoundError:
        print("❌ Error: Could not find 'fetch_data.py'.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. This usually happens if 'requests' isn't installed in your active environment.")
        print("Error details:\n", e.stderr)

if __name__ == "__main__":
    run_test()