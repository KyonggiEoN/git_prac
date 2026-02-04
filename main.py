# FIXME: ImportError: src.calc doesn't exist (should be src.calculator)
import src.calculator as cal
import src.attendance as atd

def main():
    print("=== EoN Buggy System ===")
    
    # Bug 1: Running calculator
    print(cal.add(5, 10))

    # Bug 2: Calling non-existent function
    # FIXME: AttributeError/NameError: function not defined
    name = input("이름을 입력하시오 : ")
    atd.check_attendance(name)



if __name__ == "__main__":
    main()
