# 20. Remove duplicate characters while preserving their original order. By Function
# Example: "programming" → "progamin"

def remove_duplicate():
    s = "programming"
    result = ""

    for i in s:
        if i not in result:
            result+=i
            print(i,end="")
        
remove_duplicate()










