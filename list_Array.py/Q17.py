# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.


arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
pos = []                       # non-negative numbers (order wahi)
neg = []                       # negative numbers (order wahi)

for x in arr:
    if x >= 0:
        pos.append(x)
    else:
        neg.append(x)

result = []
p = 0                          # pos list pe ungli
q = 0                          # neg list pe ungli
turn = 0                       # 0 = positive ki baari, 1 = negative ki baari

while p < len(pos) and q < len(neg):   # jab tak dono mein maal bacha ho
    if turn == 0:
        result.append(pos[p])
        p += 1
        turn = 1               # ab negative ki baari
    else:
        result.append(neg[q])
        q += 1
        turn = 0               # ab positive ki baari

# jo list bachi usko seedha jod do
while p < len(pos):
    result.append(pos[p])
    p += 1
while q < len(neg):
    result.append(neg[q])
    q += 1

print(result)                  # [9, -2, 4, -1, 5, -5, 0, -3, 2]











