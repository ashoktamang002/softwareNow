text_analyse = input("Enter text to analyse: ")

total = 0
letters = 0
digits = 0
whitespace = 0
other = 0

for char in text_analyse:
    total += 1
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        whitespace += 1
    else:
        other += 1

print("Total characters:", total)
print("Letters:", letters)
print("Digits:", digits)
print("Whitespace:", whitespace)
print("Other:", other)


check = letters + digits + whitespace + other
if check == total:
    print("self check success: counts the total.")
else:
    print("Self-check failed: count does not equal total.")