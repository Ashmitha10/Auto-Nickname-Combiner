import random

def get_user_input():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    style = input("Preferred nickname style (short / fun / formal): ").strip().lower()
    return first_name, last_name, style

def generate_nicknames(first, last, style):
    nicknames = []

    # Basic combinations
    nicknames.append(first[:3] + last[-3:])
    nicknames.append(last[:3] + first[-3:])
    nicknames.append(first[:2] + last[:2])
    nicknames.append(last[:2] + first[:2])
    nicknames.append(first + last)
    nicknames.append(last + first)

    # Fun style (add random numbers or symbols)
    if style == 'fun':
        symbols = ['_', '!', '@', '24', '99']
        for i in range(5):
            nick = random.choice([first, last]) + random.choice(symbols)
            nicknames.append(nick)
            nicknames.append(random.choice(symbols) + first[:2] + last[-2:])

    # Short style
    if style == 'short':
        nicknames.append(first[:2])
        nicknames.append(last[:2])
        nicknames.append(first[0] + last[0])

    # Formal style
    if style == 'formal':
        nicknames.append("Mr." + first)
        nicknames.append("Ms." + last)
        nicknames.append("Dr." + first + last[:1])

    # Remove duplicates
    unique_nicknames = list(set(nicknames))
    return unique_nicknames

def display_nicknames(nicknames):
    print("\nGenerated Nicknames:")
    for idx, name in enumerate(nicknames, 1):
        print(f"{idx}. {name}")

def save_to_file(nicknames):
    choice = input("Do you want to save the nicknames to a file? (yes/no): ").strip().lower()
    if choice == 'yes':
        with open("nicknames.txt", "w") as file:
            for name in nicknames:
                file.write(name + "\n")
        print("Nicknames saved to nicknames.txt!")

# Main program
first, last, style = get_user_input()
nicks = generate_nicknames(first, last, style)
display_nicknames(nicks)
save_to_file(nicks)
 
