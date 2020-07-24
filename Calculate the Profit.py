def val(cost,sell,inventory):
    return round((sell-cost)*inventory)
a=float(input('Enter the cost_price:'))
b=float(input('Enter the sell_prices:'))
c=float(input('Enter the inventory:'))
print('Profit:',val(a,b,c))