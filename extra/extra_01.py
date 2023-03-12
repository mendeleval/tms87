arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
arr_len = len(arr)
for run in range(arr_len - 1):
    for i in range(arr_len - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(arr)