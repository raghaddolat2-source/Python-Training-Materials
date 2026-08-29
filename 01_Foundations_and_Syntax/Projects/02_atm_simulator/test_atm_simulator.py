import subprocess
import sys

def run_test():
    print("Running automated test for atm_simulator.py...\n")

    # We simulate a sequence of customer withdrawals.
    # The account starts with $200.00.
    simulated_inputs = [
        "-50",     # 1. Invalid input: Negative amount (Should print error)
        "250",     # 2. Oversell attempt: More than balance (Should reject, balance still $200)
        "150",     # 3. Valid withdrawal: $150 (Success, balance drops to $50)
        "100",     # 4. Oversell attempt: $100 when only $50 remains (Should reject)
        "50"       # 5. Final withdrawal: Exactly $50 (Success, balance reaches $0 -> Triggers exit)
    ]
    
    # Join the inputs with newline characters to simulate pressing 'Enter'
    input_string = "\n".join(simulated_inputs) + "\n"

    try:
        process = subprocess.run(
            [sys.executable, "atm_simulator.py"],
            input=input_string,
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout
        
        # 1. Check if the invalid negative input was handled
        assert "Invalid request" in output, "Test Failed: Did not properly handle requests for $0 or negative amounts."
        
        # 2. Check if the initial overdraft was handled
        assert "Insufficient funds. You only have $200.00" in output, "Test Failed: Did not properly reject an overdraft attempt when $200.00 was available."
        
        # 3. Check if a valid withdrawal processes correctly and updates balance
        assert "Success! Dispensing $150.00" in output, "Test Failed: Did not process the first valid withdrawal."
        assert "Your new balance is $50.00" in output, "Test Failed: Did not correctly update the balance to $50.00 after withdrawal."
        
        # 4. Check if a secondary overdraft (asking for $100 when $50 is left) was handled
        assert "Insufficient funds. You only have $50.00" in output, "Test Failed: Did not correctly track the new balance during a secondary overdraft attempt."
        
        # 5. Check if the final withdrawal triggers the exit condition
        assert "Success! Dispensing $50.00" in output, "Test Failed: Did not process the final valid withdrawal."
        assert "Account empty." in output, "Test Failed: Did not print the 'Account empty' farewell message when the balance reached 0."
        
        print("✅ All tests passed successfully! The ATM logic is completely secure.")

    except FileNotFoundError:
        print("❌ Error: Could not find 'atm_simulator.py'. Make sure the file is named correctly.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. Check your Python code for infinite loops or syntax errors.")
        print("Error details:\n", e.stderr)
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output from script ---")
        print(output)

if __name__ == "__main__":
    run_test()