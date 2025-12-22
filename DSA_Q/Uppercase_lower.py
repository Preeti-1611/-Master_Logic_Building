s = "HELLO"
res = ""

for ch in s:
    if 'A' <= ch <= 'Z':
        res += chr(ord(ch) + 32)
    else:
        res += ch

print(res)
