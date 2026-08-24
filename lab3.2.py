
name = input("Enter Your Name :")
score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active academic backlogs: "))

if score >= 70 and backlogs == 0:
    print("\nPlacement Status: Eligible")
    print("The candidate meets all placement eligibility criteria.")
else:
    print("\nPlacement Status: Not Eligible")

    if score < 70:
        print("- Graduation score must be at least 70%.")
    if backlogs > 0:
        print("- Candidate must have no active academic backlogs.")