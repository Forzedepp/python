s_input = input().strip()
comma_index = s_input.find(',')
s = s_input[:comma_index]
char_part = s_input[comma_index+1:].strip()
target_char = char_part[0] if char_part else ''
count = 0
for c in s:
    if c == target_char:
        count += 1
    else:
        break
print(count)