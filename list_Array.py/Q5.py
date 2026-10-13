# Q.5 Find the kth largest and kth smallest element in array.

n = [10,5,7,3,8,9]
k=2
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[j]<n[i]:
            n[i],n[j]=n[j],n[i]
print(n)

for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[j]<n[i]:
            n[i],n[j]=n[j],n[i]
print("K Smallest = " , n[k-1])
print("K Largest = ",n[len(n)-k])
    