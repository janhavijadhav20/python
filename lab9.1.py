# Consumer Transaction Tracker

transactions = []

# Accept five transaction values
for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: "))
    transactions.append(amount)

# Calculate largest transaction and average spend
largest_transaction = max(transactions)
average_spend = sum(transactions) / len(transactions)

# Display results
print("\nTransaction Summary")
print("-------------------")
print("Transactions:", transactions)
print(f"Largest transaction: {largest_transaction:.2f}")
print(f"Average spend: {average_spend:.2f}")
