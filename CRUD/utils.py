import random
import string

def random_string(panjang:int) -> str:
    hasil_str = "".join(random.choice(string.ascii_letters) for i in range(6))
    return hasil_str