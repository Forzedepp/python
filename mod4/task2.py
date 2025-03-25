s = input().strip()
a_str = ''
n_str = ''
space_found = False
for c in s:
    if c == ' ' and not space_found:
        space_found = True
    elif not space_found:
        a_str += c
    else:
        n_str += c
a = int(a_str)
n = int(n_str)

def fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_pow(a * a, n // 2)
    else:
        return a * fast_pow(a, n - 1)

print(fast_pow(a, n))