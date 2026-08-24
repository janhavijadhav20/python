
status = input("Enter order status (pending/shipped/delivered): ").strip().lower()

if status == "pending":
    message = "Your order has been received and is currently being processed."
elif status == "shipped":
    message = "Your order has been shipped and is on its way to you."
elif status == "delivered":
    message = "Your order has been delivered successfully. Thank you for shopping with us!"
else:
    message = "Sorry, the order status is unknown. Please check the status keyword."

print("\n----- ORDER TRACKING UPDATE -----")
print(f"Status: {status.capitalize()}")
print(f"Update: {message}")
print("---------------------------------")