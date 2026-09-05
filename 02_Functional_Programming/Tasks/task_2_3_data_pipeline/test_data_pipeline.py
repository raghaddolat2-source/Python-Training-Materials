import subprocess
import sys

def run_test():
    print("Running automated test for data_pipeline.py...\n")

    try:
        process = subprocess.run(
            [sys.executable, "data_pipeline.py"],
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout
        
        # The expected list string representations
        expected_filtered = "[15.5, 18.1, 0.0, 22.4]"
        expected_mapped = "[23.25, 27.15, 0.0, 33.6]"
        
        assert expected_filtered in output.replace(" ", ""), "Test Failed: The filter() step did not yield the correct list of non-negative numbers."
        assert expected_mapped in output.replace(" ", ""), "Test Failed: The map() step did not correctly multiply the valid readings by 1.5."
        
        print("✅ All tests passed successfully! Your lambda pipeline is fully functional.")

    except FileNotFoundError:
        print("❌ Error: Could not find 'data_pipeline.py'.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. Check your Python code for syntax errors.")
        print("Error details:\n", e.stderr)
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output ---")
        print(output)

if __name__ == "__main__":
    run_test()