# В массиве целых чисел с количеством элементов 19 определить максимальное число
# и заменить им все четные по значению элементы.

nums = [1, 2, 3, 4, 70, 6, 15, 20, 66, 76, 87, 75, 80, 77, 12, 11, 100, 64, 13]
print(nums)
swapped = True
while swapped:
    swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True

max_number = nums[-1]

print(nums)
print(f'max num - {max_number}')

for i in range(len(nums) - 1):
    if nums[i] % 2 == 0:
        nums[i] = max_number

print(nums)
