

# playing = True

# lives = 10

# while playing:
#     lives -=1

#     if lives % 2 == 0:
#         pass
#         #add addition instructions / code
#         #playing = False
#     else:
#         print(lives)
#     if lives <= 0:
#         playing = False




# 2-7-25 Code Challenge

# Finish this function so that it returns the number of vowels in a given string:

import string


def vowel_count(sentence: str) -> int:
    count = 0
    vowels = "aeiou"

    # Create a loop to check for vowels
    for letter in sentence:
        if letter in vowels:
            count += 1


    return count


assert 6 == vowel_count("This is a random string")
assert 12 == vowel_count("Another string to test the code challenge".lower())
assert len("".join([letter for letter in string.ascii_lowercase if letter in "aeiou"])) == vowel_count(string.ascii_lowercase)

print(string.ascii_lowercase)

z = [x for x in range(10)]
print(len(z))