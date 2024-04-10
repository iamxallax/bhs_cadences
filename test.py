import string

alpha = list(string.ascii_lowercase)

code = "14 15 20 7 5 20 20 9 14  20 8 5 20 15 18 5 16 1 7 5 18 14 15 20 8 9 14 7"
translated = ""

code_list = [chr(int(c) + 96) for c in code.split()]

for c in code_list:
    translated  += c

print(translated)

"""
"I'm so fucking disappointed.

Now we're most likely in Silksong.

"""