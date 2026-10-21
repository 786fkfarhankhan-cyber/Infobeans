# 3. Count the number of vowels and consonants in a string.


s = input("Enter a String = ")
vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
v = 0
c = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha(): # isalpha yani spaces special symbol wagera ko hata deta h sirf letter pe focus karta h
        c += 1

print(f"Vowels Count = {v}")
print(f"Consonant Count = {c}")
