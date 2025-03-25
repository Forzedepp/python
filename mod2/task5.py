s = input().strip()
parts = []
current = ''
for char in s:
    if char == '.':
        if current != '':
            parts.append(current)
            current = ''
    else:
        current += char
if current != '':
    parts.append(current)
for part in reversed(parts):
    print(part)