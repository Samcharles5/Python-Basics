n = int(input('Enter number of elements: '))
arr = []

for i in range(n):
    a = int(input(f'Enter element {i + 1}: '))
    arr.append(a)

# Bubble Sort
for i in range(n):
    for j in range(0, n - 1 - i):  # Fix: loop only till n - i - 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)














# for i in range(0,len(arr)-1):
#     for j in range(0,len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
            
# print(arr)