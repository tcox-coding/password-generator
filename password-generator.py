import random
import string, secrets

length = input('Enter password length: ')

possible_chars = string.ascii_letters + './1234567890!@#$%^&*()'

for i in range(int(length)):
    print(random.choice(possible_chars), end='')