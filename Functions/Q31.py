# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

def sub():
    t = "abcabcbb"

    seen = ""
    rep = False

    for ch in t:
        if ch in seen:
            repeat = ch
            rep = True

            break
        seen += ch

    print(seen,"\n Repeating Chracter = ",repeat)
sub()
