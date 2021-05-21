from Shop.shop import Product
from shop import *

print("************ Welcome To Super Shop ************")
# Testing Product Class
sugar = Product(product_id=42, product_price=50)
print(
    "The Product id is {} , The Price of the product is {} And stock is {}".format(
        sugar.product_id, sugar.product_price, sugar.stock
    )
)

sugar.add_stock(quantity=100)
print("The New added stock quantity is: {}".format(sugar.stock))
sugar.decrease_stock(quantity=50)
print("The decreased stock quantity is: {}".format(sugar.stock))

sugar.set_price(75)
print("The price of product is: {}".format(sugar.product_price))

# Testing Customer Class
customer = Customer(customer_id=123, balance=5000)
print("The Current Customer Balance is: {}".format(customer.balance))

customer.deposit_money(3500)
print("The Deposited Money in Customer balance is: {}".format(customer.balance))

customer.purchase(product_price=10, quantity=5)
print("After purchase of product the customer balance is: {}".format(customer.balance))

# Testing Shop Class
shop = Shop(shop_balance=10000)
print("The Shop Balance is: {}".format(shop.shop_balance))

for i in range(5):
    shop.add_product(product_id=i + 1, product_price=(i + 1) * 20)
for i in range(5):
    shop.add_customer(customer_id=i + 1, product_id=i + 1, balance=(i + 1) * 200)

# print items of product object of id 1 -initially
print(shop.product_id_dict["1"].product_id)
print(shop.product_id_dict["1"].product_price)
print(shop.product_id_dict["1"].stock)
print(shop.shop_balance)

shop.purchase_stock(product_id=1, quantity=15)
print(shop.product_id_dict["1"].product_id)
print(shop.product_id_dict["1"].product_price)
print(shop.product_id_dict["1"].stock)
print(shop.shop_balance)
print(shop.customer_id_dict["1"].balance)

shop.sell_product(product_id=1, customer_id=1, quantity=10)

print(shop.product_id_dict["1"].product_id)
print(shop.product_id_dict["1"].product_price)
print(shop.product_id_dict["1"].stock)
print(shop.shop_balance)
print(shop.customer_id_dict["1"].balance)

print(shop.product_id_dict)
