print("Day 4: Reading Files")

#Open file
with open("sample_data.txt", "r") as file:
    lines = file.readlines()

print("Raw lines:")
print(lines)

print("\nProcessed Data:")

count_30_plus = 0    #Counter starts at 0

for line in lines:
    city, age = line.strip().split(",")
    age = int(age)

    if age >= 30:
        print(f"{city} has age {age} (30+)")
        count_30_plus += 1     #Increase counter
    else:
        print(f"{city} has age {age} (Under 30)")
print ("\nTotal cities 30+: ", count_30_plus)

