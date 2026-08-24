

status = input(
    "Enter atmospheric status (hot/cold/comfortable): "
).strip().lower()

if status == "hot":
    recommendation = "Turn on AC"
elif status == "cold":
    recommendation = "Activate heater"
elif status == "comfortable":
    recommendation = "Idle"
else:
    recommendation = "Unknown atmospheric status"

print("\n----- CLIMATE MONITOR -----")
print(f"Atmospheric Status : {status.capitalize()}")
print(f"Recommendation     : {recommendation}")
print("---------------------------")