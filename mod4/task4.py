s = input().strip()

freq = {}
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

odd_chars = []
for char, cnt in freq.items():
    if cnt % 2 != 0:
        odd_chars.append(char)

if len(odd_chars) > 1:
    print("Нельзя составить палиндром")
else:
    left_str = ''
    for char in freq:
        count = freq[char] // 2
        left_str += char * count
    
    right_str = ''
    i = len(left_str) - 1
    while i >= 0:
        right_str += left_str[i]
        i -= 1
    
    middle = odd_chars[0] if odd_chars else ''
    palindrome = left_str + middle + right_str
    print(palindrome)