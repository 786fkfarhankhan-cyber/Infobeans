# 24.
# Write a Python program to find the sum and average of one dimensional integer array.

arr = [4, 8, 6, 2]
total = 0                      # sab numbers ka jod
count = 0                      # kitne numbers hain

for x in arr:
    total += x                 # element total mein jodo
    count += 1                 # ginti mein ek badhao

average = total / count        # / se decimal answer milta hai
print("Sum =", total)          # 20
print("Average =", average)    # 5.0







