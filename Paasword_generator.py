import random
import string

def pass_gen(legnth: int = 14):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(legnth))
    return password

password = pass_gen()
print(f"Generated password: {password}")