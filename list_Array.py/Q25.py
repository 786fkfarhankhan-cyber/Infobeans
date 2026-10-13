# 25.
# Write a Python program to swap first and last element of an integer 1-d array.


arr = [1, 2, 3, 4, 5]

temp = arr[0]                  # pehle element ko bacha lo
arr[0] = arr[-1]               # pehle ki jagah aakhri
arr[-1] = temp                 # aakhri ki jagah bachaya hua pehla

print(arr)    






