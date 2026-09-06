#Build an ASCII-to-decimal converter.
s = ("Cool")

for c in s:
    print(ord(c))

print("\n")

print(",".join(str(ord(c)) for c in s))