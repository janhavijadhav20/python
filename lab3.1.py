
name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter your annual family income (₹): "))

if age < 25 and income < 300000:
    print("\nScholarship Status: Eligible")
    print("You qualify for the specialized education scholarship scheme.")
else:
    print("\nScholarship Status: Not Eligible")
    print("You do not meet the required age and income criteria.")