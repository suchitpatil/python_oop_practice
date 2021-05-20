from Shop.shop import Product
from shop import *

# Testing Product Class
sugar = Product(product_id=42, price=50)
print(sugar.product_id, sugar.price, sugar.stock)

sugar.add_stock(quanitity=100)
print(sugar.stock)
sugar.decrease_stock(quanitity=50)
print(sugar.stock)

sugar.set_price(75)
print(sugar.price)

# Testing Customer Class
customer = Customer(customer_id=123, balance=5000)
print(customer.balance)

customer.deposit_money(3500)
print(customer.balance)

customer.purchase(product_id=0, quantity=5)
print(customer.balance)

# Testing Shop Class
shop = Shop()
print(shop.current_balance)

for i in range(5):
    shop.add_product(product_id=i, price=(i+1)*20)
for i in range(5):
    shop.add_customer(customer_id=i, balance=(i+1)*200)

shop.sell_product(product_id=0, customer_id=1, quantity=7)
shop.purchase_stock(product_id=1, quanitity=15)