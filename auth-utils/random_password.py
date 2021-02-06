import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation.replace("'", "").replace("\\", "").replace("&", "")

pw_chars = list(f"{LETTERS}{NUMBERS}{PUNCTUATIONS}")
random.shuffle(pw_chars)

pw_string = "".join(random.choices(pw_chars, k=8))

print(pw_string)