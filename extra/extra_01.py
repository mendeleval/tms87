# arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# arr_len = len(arr)
# for run in range(arr_len - 1):
#     for i in range(arr_len - 1):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print(arr)


nums = [3, 1, 3, 7, 4, 4, 5, 5, 2]
swapped = True
while swapped:
    swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True

print(nums)
