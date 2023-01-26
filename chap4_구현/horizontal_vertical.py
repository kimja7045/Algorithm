n = int(input())
plans = list(map(str, input().split()))

x, y = 1, 1

for plan in plans:
    if plan == 'R' and y < n:
        y += 1
    elif plan == 'L' and y > 1:
        y -= 1
    elif plan == 'U' and x != 1:
        x -= 1
    elif plan == 'D' and x < n:
        x += 1        
print(f'{x} {y}')