# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False

def paraen():
    s = "()[]{}"
    ans = []
    for i in s:
        if i=='{':
            ans.append('}')
        elif i=='[':
            ans.append(']')
        elif i=='(':
            ans.append(')')
        else:
            if i!=ans.pop():
                print("Invalid")
                break
    else:
        print("Valid Parentheses")

paraen()
