def both_ends(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]

print(both_ends('helloworld'))
print(both_ends('my'))
print(both_ends('x'))
