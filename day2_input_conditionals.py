print("Day 2: Input + Conditionals")

name = input("What is your name? ").strip()
age_text = input("How old are you? ").strip()

# Basic validation
if not age_text.isdigit():
    print("Please enter a number for age next time.")
else:
    age = int(age_text)
    future_age = age + 10

    print(f"Nice to meet you, {name}.")
    print(f"In 10 years, you’ll be {future_age}.")

    if future_age >= 30:
        print("30+ club is coming 😄")
    else:
        print("Still in your 20s, enjoy it.")