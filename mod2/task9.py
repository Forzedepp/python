s = input().strip()
allowed = {'+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
result = ''
for c in s:
    if c in allowed:
        result += c
print(result)