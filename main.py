import json
from sys import exit
from models.product import Product
from models.user import User
from utils.printers import print_table ,  print_status

while True:
    print_table()
    
    tanlov = int(input("tanlang : "))
    if tanlov == 1:
        User.create_user()

    elif tanlov == 2:
        products = Product.load_products()