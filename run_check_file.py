# run_interactive_checker.py to check the MPIN:

import sys
import os

try:
    from main import MPINValidator 
    
    from models.result import ValidationResult 
    from common.constants import Constants 
except ImportError as e:
    print(f"Error importing necessary modules: {e}")
    print("Please ensure the project structure is correct and all required files exist:")
    print("- mpin_validator.py (or package containing it)")
    print("- models/user.py, models/result.py")
    print("- validators/common_mpin.py, validators/demographic.py")
    print("- common/constants.py")
    sys.exit(1)

def get_user_input():
    """Gets MPIN length, MPIN, and demographic data from the user."""
    
    pin_length = 0
    while pin_length not in [4, 6]:
        try:
            length_input = input("Enter MPIN length (4 or 6): ")
            pin_length = int(length_input)
            if pin_length not in [4, 6]:
                print("Invalid length. Please enter 4 or 6.")
        except ValueError:
            print("Invalid input. Please enter a number (4 or 6).")

    mpin = ""
    while True:
        mpin_input = input(f"Enter your {pin_length}-digit MPIN: ")
        if len(mpin_input) == pin_length and mpin_input.isdigit():
            mpin = mpin_input
            break
        else:
            print(f"Invalid input. Please enter exactly {pin_length} digits.")

    dob = None
    spouse_dob = None
    anniversary = None

    while True:
        use_demographics = input("Check against demographics (DOB, Spouse DOB, Anniversary)? (yes/no): ").lower()
        if use_demographics in ['yes', 'y']:
            print("\nPlease enter dates in DD-MM-YYYY format. Press Enter to skip any date.")
            dob_input = input("Your Date of Birth (DD-MM-YYYY): ")
            dob = dob_input if dob_input else None
            
            spouse_dob_input = input("Spouse's Date of Birth (DD-MM-YYYY): ")
            spouse_dob = spouse_dob_input if spouse_dob_input else None
            
            anniversary_input = input("Wedding Anniversary (DD-MM-YYYY): ")
            anniversary = anniversary_input if anniversary_input else None
            break
        elif use_demographics in ['no', 'n']:
            print("Skipping demographic checks.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return pin_length, mpin, dob, spouse_dob, anniversary

def main():
    """Main function to run the interactive checker."""
    print("--- MPIN Strength Checker ---")
    
    pin_length, mpin, dob, spouse_dob, anniversary = get_user_input()
    
    result = None
    try:
        if pin_length == 4:
            # Using Part C logic which returns ValidationResult
            print("\nValidating 4-digit MPIN...")
            result = MPINValidator.validate_mpin_part_c(mpin, dob, spouse_dob, anniversary)
        elif pin_length == 6:
            # Using Part D logic which returns ValidationResult
            print("\nValidating 6-digit MPIN...")
            result = MPINValidator.validate_mpin_part_d(mpin, dob, spouse_dob, anniversary)
            
    except ValueError as e:
        print(f"\nError during validation: {e}")
        sys.exit(1)
    except Exception as e:
        # Catch unexpected errors
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

    if result:
        print("\n--- Validation Result ---")
        print(f"MPIN Entered: {'*' * pin_length}") # to avoid printing the actual PIN
        print(f"Strength: {result.strength}")
        if result.reasons:
            print("Reasons for Weakness:")
            for reason in result.reasons:
                print(f"- {reason}")
        else:
            if result.strength == Constants.WEAK:
                 print("Reason: Unknown (Check validator logic if reasons are expected but missing)")
            else:
                 print("Reason: MPIN considered strong.")
    else:
        print("Validation could not be completed.")


if __name__ == "__main__":
    main()