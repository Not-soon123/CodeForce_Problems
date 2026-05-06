s = input()
SplittedNumber = s.split("+")
SortedNumber =  sorted(map(int, SplittedNumber))
print("+".join(map(str, SortedNumber)))