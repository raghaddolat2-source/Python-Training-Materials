import subprocess
import sys

def run_test():
    print("Running automated test for planetary_calculator.py...\n")

    try:
        process = subprocess.run(
            [sys.executable, "planetary_calculator.py"],
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout
        
        # We look for the exact mathematical results. 100 * 9.8 = 980.0
        assert "980" in output, "Test Failed: Did not find the correct weight for Earth (980.0)."
        assert "371" in output, "Test Failed: Did not find the correct weight for Mars (371.0)."
        assert "2479" in output, "Test Failed: Did not find the correct weight for Jupiter (2479.0)."
        
        print("✅ All tests passed successfully! Function parameters and defaults are working properly.")

    except FileNotFoundError:
        print("❌ Error: Could not find 'planetary_calculator.py'.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. Check your Python code for syntax errors.")
        print("Error details:\n", e.stderr)
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output ---")
        print(output)

if __name__ == "__main__":
    run_test()