string1 = input().lower()
string2 = input().lower()
if len(string1) == len(string2):
    #print(string1,string2)
    if string1 == string2:
        print(0)
    if string1 > string2:
        print(1)
    else:
        print(-1)
