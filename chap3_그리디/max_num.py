# M = 8
# K = 3
# arr = [2, 4, 5, 4, 6]

M = 7
K = 2
arr = [3, 4, 3, 4, 3]

arr = sorted(arr, reverse=True)
total_num = 0


def same_num_check(arr):
    return arr[0] == arr[1]


is_same_num_in_arr = same_num_check(arr)
if is_same_num_in_arr:
    total_num = arr[0] * M
else:
    for i in range(2):
        total_num += arr[0] * K
        total_num += arr[1]

print(total_num)
