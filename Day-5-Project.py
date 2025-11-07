import random

print("Welcome to the PyPassword Generator!")
pass_word_len = int(input("How many letters would you like in your password? \n"))
pass_sym_len = int(input("How many symbols would you like? \n"))
pass_int_len = int(input("How many numbers would you like? \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

for letter in range(0,pass_word_len):
    password_list.append(random.choice(letters))
for letter in range(0,pass_word_len):
    password_list.append(random.choice(symbols))
for letter in range(0,pass_word_len):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"password: {password}")
