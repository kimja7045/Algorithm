n = int(input())
count = 0


for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            time = str(hour) + ':' + str(minute) + ':' + str(second)
            if str(n) in time:
                count += 1

print(count)

