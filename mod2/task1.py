s = input().strip()
comma_index = s.find(',')
a_str = s[:comma_index].strip()
b_str = s[comma_index+1:].strip()
a = int(a_str)
b = int(b_str)
print(a % b)