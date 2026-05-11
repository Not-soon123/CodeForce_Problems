petys_input = input().lower()

vowels = "aeiou"

result = ""

for char in petys_input:
    if char not in vowels:
        result += "." + char

print(result)