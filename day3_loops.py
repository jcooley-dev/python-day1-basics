print("Day 3: Loops Practice")
# FOR LOOP EXAMPLE
print("\nCounting from 1 to 5:")
for number in range(1, 6):
    print(number)
# LIST LOOP EXAMPLE
print("\nLooping through a list of cities:")
cities = ["Tampa", "Orlando", "Miami", "Jacksonville"]
for city in cities:
    print("City:", city)
# WHILE LOOP EXAMPLE 
print("\nWhile loop countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("\nSquare Calculator:")
for num in range(1, 6):
    square = num ** 2
    print(f"{num} squared is {square}")
    
print("Done!")
