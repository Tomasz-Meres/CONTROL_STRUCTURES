###
# a program that checks how much a product has been discounted
#

current_price = 140
previous_price = 200

discount = 100 - current_price / previous_price * 100

if discount >= 10:
    print(f'Current product price: {current_price}')
    print(f'Previous product price: {previous_price}')
    print('Buy the product!!')
    print(f'Product price reduced by {discount}%')
else:
    print(f'Current product price: {current_price}')
    print(f'Previous product price: {previous_price}')
