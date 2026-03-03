letra=input()
if letra.isupper():
    print("uppercase")
if letra.islower():
    print("lowercase")
if letra in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")
