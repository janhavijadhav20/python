print("******************* COUNTDOWN *******************")

import time

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print(f"Time Left: {seconds} seconds")
    time.sleep(1)
    seconds = seconds - 1


print("🎉🎆🎇 HAPPY NEW YEAR ! 🎇🎊🎆")