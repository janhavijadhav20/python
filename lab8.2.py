
feedback = input("Enter feedback: ")

target_words = ["atmaj", "printer", "chatgpt"]

for word in target_words:
    feedback = feedback.replace(word, "****")
    feedback = feedback.replace(word.upper(), "****")
    feedback = feedback.replace(word.capitalize(), "****")

print("\n----- MODERATED FEEDBACK -----")
print(feedback)
print("------------------------------")