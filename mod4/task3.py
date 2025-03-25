s = input().strip()
a_str = ''
b_str = ''
space_found = False
for c in s:
    if c == ' ' and not space_found:
        space_found = True
    elif not space_found:
        a_str += c
    else:
        b_str += c
a = int(a_str)
b = int(b_str)

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(a, b))