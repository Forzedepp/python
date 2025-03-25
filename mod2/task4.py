s = input().strip()

def is_natural(s):
    if not s:
        return False
    for c in s:
        if not c.isdigit():
            return False
    return int(s) > 0

if not is_natural(s):
    print("Неверный ввод")
else:
    n = int(s)
    def convert(n, base):
        if n == 0:
            return '0'
        digits = []
        hex_digits = '0123456789ABCDEF'
        while n > 0:
            rem = n % base
            if base == 16:
                digits.append(hex_digits[rem])
            else:
                digits.append(str(rem))
            n = n // base
        digits.reverse()
        res = ''
        for d in digits:
            res += d
        return res

    binary = convert(n, 2)
    octal = convert(n, 8)
    hexa = convert(n, 16)
    print(f"{binary}, {octal}, {hexa}")