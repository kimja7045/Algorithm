input_data = input()



columns = [97, 98, 99, 100, 101, 102, 103, 104]

def move_check(input_data):
    column = input_data[0]  # a
    row = int(input_data[1])  # 1
    result = 0

    if row-2 >= 1 and ord(column)-1 >= 97:
        result += 1
    if row-2 >= 1 and ord(column)+1 <= 104:
        result += 1
    if row+1 <= 8 and ord(column)-2 >= 97:
        result += 1
    if row-1 >= 1 and ord(column)-2 >= 97:
        result += 1
    if row+1 <= 8 and ord(column)+2 <= 104:
        result += 1
    if row-1 >= 1 and ord(column)+2 <= 104:
        result += 1
    if row+2 <= 8 and ord(column)-1 >= 97:
        result += 1
    if row+2 <= 8 and ord(column)+1 <= 104:
        result += 1
    return result

result = move_check(input_data)
print(result)
# upup left, upup right, leletop, leledown, riritop, riri down, bobo left, bobo right