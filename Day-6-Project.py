import random

word_list = ["aardvark", "baboon", "camel"]
guess = input("Guess a letter: ").lower()

index = random.randint(0,2)
answer = word_list[index]
print(answer)

placeholder = ""
for i in range(len(word_list[index])):
    placeholder += "_"
print(placeholder)

display = ""
for letter in word_list[index]:
    if (guess == letter):
        display += letter
    else:
        display += "_"

print(display)