actual_cost=float(input("enter the actual price:"))
sale_amount=float(input("enter the sale price:"))
if(actual_cost>sale_amount):
    amount=sale_amount+actual_cost
    print("total profit={0}",format(amount))
else:
    print("no profit!!")