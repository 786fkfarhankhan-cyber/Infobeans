# 25. Find all duplicate characters and their frequencies. By Function
def dup_freq():
    s = input("Enter a string = ")

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in freq:
        if freq[ch] > 1:
            print(ch, "=", freq[ch])

dup_freq()