class Product:
    def __init__(self, product_id, product_price):
        self.product_id = product_id  # which product
        self.product_price = product_price  # product_price
        self.stock = 0  # temporary stock will be zero

    def add_stock(self, quantity):
        self.stock = self.stock + quantity

    def decrease_stock(self, quantity):
        self.stock = self.stock - quantity

    def set_price(self, price):
        self.product_price = price


class Customer:
    def __init__(self, customer_id, balance):
        self.customer_id = customer_id
        self.balance = balance
        self.customer_issued = -1

    def deposit_money(self, money_deposit):
        self.balance = self.balance + money_deposit

    def purchase(self, product_price, quantity):
        self.balance = self.balance - product_price * quantity


class Shop:
    def __init__(self, shop_balance):
        self.shop_balance = shop_balance
        self.product_id_dict = {}
        self.customer_id_dict = {}

    def add_product(self, product_id, product_price):
        if str(product_id) in self.product_id_dict:
            print("Product_Id  Already in use!")
        else:
            self.product_id_dict[str(product_id)] = Product(
                product_id=product_id, product_price=product_price
            )  # add new product.
            print("Added Product id   ", product_id, product_price)

    def add_customer(self, product_id, balance, customer_id):
        if str(customer_id) in self.customer_id_dict:
            print("Customer_Id  Already in use!")
        else:
            self.customer_id_dict[str(customer_id)] = Customer(
                customer_id=customer_id, balance=balance
            )  # add new product.
            print("Added Customer id  ", customer_id, balance)

    def purchase_stock(self, product_id, quantity):
        # add quantity of product id
        self.product_id_dict[str(product_id)].stock += quantity
        # balance should get reduce from shop balance
        self.shop_balance -= (
            self.product_id_dict[str(product_id)].product_price * quantity
        )

    def sell_product(self, product_id, customer_id, quantity):
        # check wether product is available or not
        if str(product_id) in self.product_id_dict:
            # check wether customer is added
            if str(customer_id) in self.customer_id_dict:
                # then sell product by multiplying product price into quantity
                total_cost = (
                    self.product_id_dict[str(product_id)].product_price * quantity
                )
                # reduce stock from shop
                self.product_id_dict[str(product_id)].stock = (
                    self.product_id_dict[str(product_id)].stock - quantity
                )
                # set customers product to customer id
                self.customer_id_dict[str(customer_id)].customer_issued == product_id
                # add balance in shop
                self.shop_balance = self.shop_balance + total_cost
                # total cost should be deducted from customer balance
                self.customer_id_dict[str(customer_id)].balance -= total_cost
            else:
                print("Please Add Customer .")
        else:
            print("Product is not avilable , please add the product")
