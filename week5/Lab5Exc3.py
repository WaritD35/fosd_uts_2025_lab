def vowel_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return print(f"Vowel count = {count}")

while True:
    sentence = str(input("String: "))
    sentence = sentence.lower()

    if sentence == "*":
        print("Done")
        break
    else:
        vowel_count(sentence)



