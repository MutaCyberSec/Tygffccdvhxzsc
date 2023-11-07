import re

import random


import dns.resolver

de_arr = []

with open('names1.txt', 'r') as file:
        for line in file:
                cleaned_text = re.sub(r'[0-9@#$%^&*,;:]', '',line)
                de_arr.append(cleaned_text)
        print(len(de_arr))
second = []



with open('names2.txt', 'r') as file:
        for line in file:
                cleaned_text = re.sub(r'[0-9@#$%^&*,.();:]', '',line)
                second.append(cleaned_text)
print(len(second))


tr= set()

emails = []

import string

for x in range(3000000):


        fn = random.choice(de_arr)

        fn2 = re.sub(r'\n', ' ', fn)

        sn = random.choice(second)
        sn2 = re.sub(r'\n', ' ', sn)


        pr = random.choice(["mail.com","aol.com","yahoo.com","gmail.com"])

        xy = fn2 + sn2

        tb = xy.strip()

        ffn  = tb.replace(" ", "").replace("\t", "").replace("\n", "")


# Convert the text to lowercase to make the search case-insensitive
        de_text = ffn.lower()

# Create a set of all lowercase letters in the alphabet
        alphabet = set(string.ascii_lowercase)

# Initialize an empty set to store the found alphabet letters
        found_letters = []

# Iterate through each character in the text
        for char in de_text:
                if char in alphabet:
                        found_letters.append(char)


        fn = ''.join(found_letters)
        year = str(random.randrange(1970, 1999))
        bd  = str(random.randrange(1, 30))
        mn = str(random.randrange(1, 12))
        bdx = bd+mn
        nos =  random.choice([year,bdx])
        gn = fn  + nos +  "@"  + pr

        tr.add(gn)
trx = list(tr)
with open('norEms2.txt', 'w') as file:
        dem = ",".join(trx)
        file.write(dem)

print(len(trx))
