s = input().strip()
words = []
current = ''
for char in s:
    if char == ' ':
        if current != '':
            words.append(current)
            current = ''
    else:
        current += char
if current != '':
    words.append(current)
result = ''
for word in words:
    if word:
        result += word[-1]
print(result)