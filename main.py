# FIXME: ImportError: src.calc doesn't exist (should be src.calculator)
import src.calc as calculator
from src.attendance import check_attendance

def main():
    print("=== EoN Buggy System ===")
    
    # Bug 1: Running calculator
    print(calculator.add(5, 10))

    # Bug 2: Calling non-existent function
    # FIXME: AttributeError/NameError: function not defined
    run_system_check()

if __name__ == "__main__":
    main()
