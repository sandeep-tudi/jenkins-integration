stock_price = [('APPL',200),('GOOG', 300),('MSFT', 400)]
for item,price in stock_price:
    print(item)
    print(price)

# Trying to unpack the tuple and try to increase the price of an Individual item in the tuple
for ticker,price in stock_price:
    print(price+(0.1*price))