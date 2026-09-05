import subprocess
import sys

def run_test():
    print("Running automated test for config_manager.py...\n")

    try:
        process = subprocess.run(
            [sys.executable, "config_manager.py"],
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout
        
        assert "Development" in output, "Test Failed: Did not find the initial 'Development' state in output."
        assert "Deploying from Development to Production" in output, "Test Failed: Inner function deployment message missing."
        
        # Check if "Production" appears after the initial setup
        assert "Production" in output, "Test Failed: The global variable was not successfully changed to 'Production'."
        
        print("✅ All tests passed successfully! Global and Enclosing scopes were manipulated correctly.")

    except FileNotFoundError:
        print("❌ Error: Could not find 'config_manager.py'.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. Check your Python code for syntax errors.")
        print("Error details:\n", e.stderr)
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output ---")
        print(output)

if __name__ == "__main__":
    run_test()