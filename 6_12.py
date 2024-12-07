###
# A program that calculates the amount to be paid.
# If product is purchased over two the discount is charged for each product
#

num_of_products = int(input('Number of products purchased: '))
price = int(input('Product price: '))
amount_to_pay = 0
discount = 0.25  # 25%

if num_of_products > 2:
    amount_to_pay = 2 * price + (num_of_products - 2) * price * (1 - discount)
else:
    amount_to_pay = num_of_products * price

print(f'Amount to pay: {amount_to_pay}')
