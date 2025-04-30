# Step 1: Create an empty list
tasks = []  # This is your to-do list. Right now it's empty.

# Step 2: Add tasks using append()
tasks.append("Buy milk")         # Adds "Buy milk" to the list
tasks.append("Do homework")      # Adds "Do homework" to the list
print("After append:", tasks)    # Output: ['Buy milk', 'Do homework']

# Step 3: Remove a task using remove()
tasks.remove("Buy milk")         # Removes "Buy milk" from the list
print("After remove:", tasks)    # Output: ['Do homework']

# Step 4: Add more tasks
tasks.append("Exercise")
tasks.append("Call mom")
print("More tasks added:", tasks)  # Output: ['Do homework', 'Exercise', 'Call mom']

# Step 5: Sort the list
tasks.sort()   # Sorts the list alphabetically
print("After sort:", tasks)  # Output: ['Call mom', 'Do homework', 'Exercise']

# Step 6: Reverse the list
tasks.reverse()
print("After reverse:", tasks)  # Output: ['Exercise', 'Do homework', 'Call mom']

# Step 7: Count how many times a task appears
tasks.append("Call mom")
print("Call mom count:", tasks.count("Call mom"))  # Output: 2

# Step 8: Copy the list
backup = tasks.copy()
print("Backup list:", backup)  # Output: Same as tasks list





#What You Learned:

# Method          #What it does

# append()        #Adds item at the end
# remove()        #Removes a specific item
# sort()          #Sorts list (A to Z)
# reverse()       #Reverses the list order
# count()         #Counts how many times item appears
# copy()          #Makes a copy of the list



# SOME INTERESTING



# Step 1: Create an empty list / एक खाली लिस्ट बनाते हैं
tasks = []

# Step 2: Add tasks using append() / append() का उपयोग करके कार्य जोड़ते हैं
tasks.append("Buy groceries")    # "Buy groceries" लिस्ट में जोड़ें
tasks.append("Clean the house")  # "Clean the house" लिस्ट में जोड़ें
tasks.append("Study Python")     # "Study Python" लिस्ट में जोड़ें
print("Initial List (after append):", tasks)  # लिस्ट में जोड़ने के बाद

# Step 3: Insert a task at position 1 / एक कार्य को पोज़ीशन 1 पर डालना
tasks.insert(1, "Call Mom")  # "Call Mom" को लिस्ट के दूसरे स्थान पर डालते हैं
print("List (after insert):", tasks)  # लिस्ट में जोड़ने के बाद

# Step 4: Remove a completed task / पूरा हुआ कार्य हटाना
tasks.remove("Clean the house")  # "Clean the house" को लिस्ट से हटाते हैं
print("List (after remove):", tasks)  # लिस्ट से हटाने के बाद

# Step 5: Pop the last task / आखिरी कार्य हटाना और दिखाना
last_task = tasks.pop()  # लिस्ट का आखिरी आइटम हटा दिया गया और स्टोर किया गया
print("Last task removed:", last_task)  # हटाया गया कार्य दिखाते हैं
print("List (after pop):", tasks)  # लिस्ट में बदलाव के बाद

# Step 6: Count the occurrences of a task / "Call Mom" कितनी बार आया है गिनना
tasks.append("Call Mom")
call_mom_count = tasks.count("Call Mom")  # "Call Mom" की गिनती निकालते हैं
print("Count of 'Call Mom':", call_mom_count)  # "Call Mom" की गिनती दिखाते हैं

# Step 7: Sort the list / लिस्ट को अल्फाबेटिकली सॉर्ट करना
tasks.sort()  # लिस्ट को A-Z में सॉर्ट किया गया
print("List (after sort):", tasks)  # सॉर्ट करने के बाद लिस्ट

# Step 8: Reverse the list / लिस्ट को उल्टा करना
tasks.reverse()  # लिस्ट को उल्टा किया गया
print("List (after reverse):", tasks)  # उलटी लिस्ट दिखाते हैं

# Step 9: Extend the list with multiple tasks / extend() से कई कार्य जोड़ना
tasks.extend(["Read book", "Work on project", "Drink water"])
print("List (after extend):", tasks)  # लिस्ट में और कार्य जोड़ने के बाद

# Step 10: Copy the list / लिस्ट की कॉपी बनाना
backup_tasks = tasks.copy()  # tasks लिस्ट की कॉपी बनाना
print("Backup List:", backup_tasks)  # बैकअप लिस्ट दिखाते हैं

# Step 11: Clear the list / लिस्ट को पूरी तरह से साफ़ करना
tasks.clear()  # लिस्ट को साफ़ कर दिया गया
print("List (after clear):", tasks)  # लिस्ट को क्लियर करने के बाद

