import subprocess
import sys

def run_test():
    print("Running automated tests for unbreakable_calc.py...\n")

    # Define test cases: (Simulated Input, Expected Output text, Test Name)
    test_cases = [
        ("10\n2\n", "Success!", "Valid Division Test"),
        ("10\n0\n", "Cannot divide by zero", "ZeroDivisionError Test"),
        ("ten\n5\n", "numbers only", "ValueError Test")
    ]

    all_passed = True

    for user_input, expected_result, test_name in test_cases:
        try:
            process = subprocess.run(
                [sys.executable, "unbreakable_calc.py"],
                input=user_input,
                text=True,
                capture_output=True,
                check=True
            )
            
            output = process.stdout
            
            # 1. Check if the specific error or success message was triggered
            if expected_result not in output:
                print(f"❌ {test_name} Failed. Expected to see: '{expected_result}'")
                all_passed = False
            
            # 2. Check if the finally block ran regardless of the outcome
            if "Calculation attempt complete" not in output:
                print(f"❌ {test_name} Failed. The 'finally' block message was missing.")
                all_passed = False
                
            if expected_result in output and "Calculation attempt complete" in output:
                 print(f"✅ {test_name} Passed.")

        except FileNotFoundError:
            print("❌ Error: Could not find 'unbreakable_calc.py'.")
            return
        except subprocess.CalledProcessError as e:
            print(f"❌ Script crashed on {test_name}. The try/except block failed to catch the error.")
            all_passed = False

    if all_passed:
        print("\n🏆 All tests passed! Your calculator is truly unbreakable.")
    else:
        print("\n⚠️ Some tests failed. Please review your exception blocks and try again.")

if __name__ == "__main__":
    run_test()