#Build a number-base converter supporting binary, decimal, octal, and hexadecimal.

number = input("Enter a number: ")
base = input("Enter its base (binary, decimal, octal, or hexadecimal): ").lower()

if base == "binary":
    decimal_number = int(number, 2)
elif base == "decimal":
    decimal_number = int(number, 10)
elif base == "octal":
    decimal_number = int(number, 8)
elif base == "hexadecimal":
    decimal_number = int(number, 16)
else:
    print("Invalid base.")
    exit()

print("Binary:", bin(decimal_number)[2:])
print("Decimal:", decimal_number)
print("Octal:", oct(decimal_number)[2:])
print("Hexadecimal:", hex(decimal_number)[2:].upper())