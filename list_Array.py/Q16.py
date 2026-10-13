arr = [1, 0, 0, 1, 0, 1, 1]
count = 0                      # kitne subarrays mile

for i in range(len(arr)):      # i = subarray kahan se shuru hota hai
    zeros = 0                  # naya start = naya khali subarray
    ones = 0
    for j in range(i, len(arr)):   # j = subarray kahan tak gaya
        if arr[j] == 0:
            zeros += 1         # naya element 0 hai
        else:
            ones += 1          # naya element 1 hai
        if zeros == ones:      # dono barabar
            count += 1         # ek subarray mil gaya

print(count)                   # 8