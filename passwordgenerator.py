import random

characters = "abcdefghijklmnopABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$"

length = int(input("enter the password length: "))

password = " "

for i in range(length):
    password = password+ random.choice(characters)

print(f"your password is ", password)