import subprocess
import sys

def run_test():
    print("Running automated test for cinema_ticketing.py...\n")

    # We simulate a sequence of customers trying to buy tickets.
    # The cinema starts with 5 tickets.
    simulated_inputs = [
        "Alice", "0",      # 1. Invalid input: 0 tickets (Should print error)
        "Bob", "6",        # 2. Oversell attempt: 6 tickets (Should reject, 5 left)
        "Charlie", "3",    # 3. Valid purchase: 3 tickets (Success, 2 left)
        "Dave", "3",       # 4. Oversell attempt: 3 tickets (Should reject, only 2 left)
        "Eve", "2"         # 5. Valid purchase: 2 tickets (Success, 0 left -> Triggers Sold Out)
    ]
    
    # Join the inputs with newline characters to simulate pressing 'Enter'
    input_string = "\n".join(simulated_inputs) + "\n"

    try:
        process = subprocess.run(
            [sys.executable, "cinema_ticketing.py"],
            input=input_string,
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout
        
        # 1. Check if the invalid input (0 tickets) was handled
        assert "Invalid request" in output, "Test Failed: Did not properly handle requests for 0 or negative tickets."
        
        # 2. Check if the initial oversell (6 tickets) was handled
        assert "Sorry Bob, we only have 5" in output, "Test Failed: Did not properly handle an oversell attempt when 5 tickets were left."
        
        # 3. Check if a valid purchase processes correctly
        assert "Success! Charlie bought 3 ticket(s)." in output, "Test Failed: Did not process a valid purchase correctly."
        
        # 4. Check if a secondary oversell (asking for 3 when 2 are left) was handled
        assert "Sorry Dave, we only have 2" in output, "Test Failed: Did not correctly track remaining inventory after a purchase."
        
        # 5. Check if the final purchase triggers the exit condition
        assert "Success! Eve bought 2" in output, "Test Failed: Did not process the final valid purchase."
        assert "Sold out!" in output, "Test Failed: Did not print the 'Sold out!' message when tickets reached 0."
        
        print("✅ All tests passed successfully! The ticketing system logic is flawless.")

    except FileNotFoundError:
        print("❌ Error: Could not find 'cinema_ticketing.py'. Make sure the file is named correctly.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. Check your Python code for infinite loops or syntax errors.")
        print("Error details:\n", e.stderr)
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output from script ---")
        print(output)

if __name__ == "__main__":
    run_test()