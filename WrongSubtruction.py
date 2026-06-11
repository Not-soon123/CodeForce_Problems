number_tyla_substruct, number_of_times = map(int, input().split())

for i in range(number_of_times):
    if number_tyla_substruct % 10 == 0:
        number_tyla_substruct /= 10
    elif int(number_tyla_substruct) == 1:
        break
    else:
        number_tyla_substruct -= 1
print(int(number_tyla_substruct))