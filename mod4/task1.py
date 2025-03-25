s = input().strip()
nums = []
current = ''
for c in s:
    if c == ' ':
        if current:
            nums.append(int(current))
            current = ''
    else:
        current += c
if current:
    nums.append(int(current))

if not nums:
    print("Список пуст")
else:
    unique = set(nums)
    if len(unique) == 1:
        print("Все числа равны")
    elif len(unique) == len(nums):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")