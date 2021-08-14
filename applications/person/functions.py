# Extra functions for application person
import random
import string

def pass_generator(size=12, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
