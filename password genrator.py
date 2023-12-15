
import random
import string

def password_generator(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

generated_password = password_generator()
print("Generated Password is:", generated_password)