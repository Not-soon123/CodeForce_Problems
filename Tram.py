Number_of_stops = int(input())
total_number_of_people = 0
s = []
for i in range(Number_of_stops):
    ai,bi = map(int, input().split())
    total_number_of_people = total_number_of_people - ai + bi
    s.append(total_number_of_people)
print(max(s))