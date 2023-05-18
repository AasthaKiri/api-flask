import random
import string

def get_pass():
    # With combination of lower and upper case
    char= string.digits+string.ascii_letters
    result_str = ''.join(random.choice(char) for i in range(12))
    # print random string
    # print(result_str)
    return result_str

