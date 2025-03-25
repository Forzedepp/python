s = input().strip()
count0 = 0
count1 = 0
for c in s:
    if c == '0':
        count0 += 1
    elif c == '1':
        count1 += 1
print('yes' if count0 == count1 else 'no')