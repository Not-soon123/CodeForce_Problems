color = list(map(int,input().split()))
color_to_buy = len(color) - len(set(color))
print(color_to_buy)