#  별 2개
# 1=바다, 0=육지
# 0=북쪽, 1=동쪽, 2=남쪽, 3=서쪽

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
arr = [[0] * m] * n
left_move_x = [-1, 0, 1, 0]  # 서, 남, 동, 북
left_move_y = [0, -1, 0, 1]

result = 1

for i in range(n):
    arr_second = list(map(int, input().split()))
    arr[i] = arr_second

arr[x][y] = 1


def turn_left(arr, x, y, direction):
    if direction == 0:  # 북쪽
        if arr[x+left_move_x[0]][y+left_move_y[0]] == 0:
            x += left_move_x[0]
            y += left_move_y[0]
        direction = 3
    elif direction == 1:  # 동쪽
        if arr[x+left_move_x[3]][y+left_move_y[3]] == 0:
            x += left_move_x[3]
            y += left_move_y[3]
        direction = 0
    elif direction == 2:  # 남쪽
        if arr[x+left_move_x[2]][y+left_move_y[2]] == 0:
            x += left_move_x[2]
            y += left_move_y[2]
        direction = 1
    elif direction == 3:  # 서쪽
        if arr[x+left_move_x[1]][y+left_move_y[1]] == 0:
            x += left_move_x[1]
            y += left_move_y[1]
        direction = 2
    return [arr, x, y, direction]


def exit_check(arr, x, y, direction):
    if arr[x+left_move_x[0]][y+left_move_y[0]] == 1 and arr[x+left_move_x[1]][y+left_move_y[1]] == 1 and \
            arr[x+left_move_x[2]][y+left_move_y[2]] == 1 and arr[x+left_move_x[3]][y+left_move_y[3]] == 1:
        if direction == 0:  # 북쪽
            y += 1
        elif direction == 1:  # 동쪽
            x -= 1
        elif direction == 2:  # 남쪽
            y -= 1
        elif direction == 3:  # 서쪽
            x += 1

        if arr[x][y] == 1:
            return True
        else:
            return False
    else:
        return False


while True:
    [arr, x, y, direction] = turn_left(arr, x, y, direction)
    if arr[x][y] == 0:
        arr[x][y] = 1
        result += 1
    is_exit = exit_check(arr, x, y, direction)
    if is_exit:
        break


print(f'\n\narr - {arr}\n\n{result}')
