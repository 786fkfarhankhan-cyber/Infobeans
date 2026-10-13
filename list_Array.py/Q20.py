# Q.20) Find Maximum product contigeous sub array
# Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.


arr = [6, -3, -10, 0, 2]
best = arr[0]                  # ab tak ka sabse bada product

for i in range(len(arr)):      # subarray kahan se shuru
    product = 1                # guna ke liye 1 se shuru (0 se nahi, warna sab 0)
    for j in range(i, len(arr)):
        product = product * arr[j]   # naya element guna karo
        if product > best:
            best = product     # naya record

print(best)    