# Есть список arr = [1,2,3,4,4,4,5,5,2]
# 1. Найти сумму всех числел
# 4. Найти массив квадратов
# 5*. Найти кумулятивную сумму
# 6*. Найти медиану
# 7*. Найти верхнюю и нижнюю квартиль

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# count = 0
# result = 0
# while count < len(arr):
#     result += arr[count]
#     count += 1
#
# print(result)

# result = 0
# while arr:
#     result += arr.pop(0)
# print(result)


# Найти верхнюю и нижнюю квартиль = 0.75 * (n +1)     n - кол-во элементов
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
arr.sort()
print(arr)
index_v_dkvar = 0.75 * (len(arr) - 1)
int_index = int(index_v_dkvar)
if index_v_dkvar % 1:
    print(arr[int_index])
else:
    result = (arr[int_index] + arr[int_index + 1]) / 2
    print(result)
