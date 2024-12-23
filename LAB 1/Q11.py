#WAP to ask for a sentence and calculate the frequency of characters in the sentences.
def characterFrequency(sentence):
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

sentence = input("Enter a sentence: ")

frequency = characterFrequency(sentence)

print("Caracter Frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
