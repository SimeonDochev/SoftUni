n = int(input())
left_sum = 0
right_sum = 0

for i in range(n):
    num = int(input())
    left_sum += num

for j in range(n):
    num = int(input())
    right_sum += num

diff = abs(left_sum - right_sum)
if diff == 0:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')
