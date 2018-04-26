import string
from random import *


def passwd_gen():
    """
    password generator
    """
    min_char = 8
    max_char = 12
    allchar = string.ascii_letters + string.punctuation + string.digits
    pwd = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    # print "This is your password : ",password
    # chars ="abcdefghijklmnopqrstuvwxzy1234567890"
    # password = random.choice(chars)
    return pwd

if __name__ == '__main__':
    gen_password = passwd_gen()
    # print(f"newly created password: {gen_password}")
