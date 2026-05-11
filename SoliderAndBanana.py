cost_of_first_banana, dollars_soldier_has, number_of_bananas = map(int, input().split())

total_dollar = 0
for i in range(1,number_of_bananas+1):
    total_dollar += i*cost_of_first_banana 
many_to_borrow = total_dollar - dollars_soldier_has

if many_to_borrow > 0:
    print(many_to_borrow)
else:    print(0)
