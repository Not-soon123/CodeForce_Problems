petys_input = input().lower()

vowels_withY = "aeiouy"

result = ""

for char in petys_input:
    if char not in vowels_withY:
        result += "." + char

print(result)