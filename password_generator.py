import random, string

password_length = int(input('Inserire lunghezza password: '))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''

for i in range(password_length):
    password = password + random.choice(characters)

print('Password generated: {}'.format(password))