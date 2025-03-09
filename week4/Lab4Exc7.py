vowel = ["a", "e", "i", "o", "u"]
vovel_count = 0

while True:
    character = input("Enter a character: ")
    character = character.lower()

    if character == ".":
        break
    elif character in vowel:
        vovel_count += 1

print("Number of vowels: ", vovel_count)