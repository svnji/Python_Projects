n = int(input())
groups = list(map(int, input().split()))
count = [0, 0, 0, 0]
for group in groups:
    count[group - 1] += 1
taxis = count[3] + count[2] + (count[1] * 2 + max(count[0] - count[2], 0) + 3) // 4
print(taxis)
