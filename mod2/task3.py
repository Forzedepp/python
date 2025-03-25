s = input().strip()
current = ''
numbers = []
for char in s:
    if char == ' ':
        if current != '':
            numbers.append(current)
            current = ''
    else:
        current += char
if current != '':
    numbers.append(current)
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
min_val = min(a, b, c)
max_val = max(a, b, c)
middle = a + b + c - min_val - max_val
print(middle)