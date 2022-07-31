import string
import random

#characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    #length o password from the user
    length = int(input("Enter password length: "))
    #number of character types
    alphabets_count = int(input("Enter alphabet count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))
    characters_count = alphabets_count + digits_count + special_characters_count
    #check total length with character sum count
    #print not valid if sum is greater than length
    if characters_count > length:
        print("Character total count is greater than password length")
        return
    #initializing the password
    password = []
    #picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))
    #picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))
    #picking random special characters
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))
    #if the total characters count is less than password length
    #add random characters to make it equal to the length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))
    #shuffling the resultantpassword
    random.shuffle(password)
    #converting the list to string
    #printing the list
    print("".join(password))

# invoking the function
generate_random_password()
