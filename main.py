from models.user import User
from utils import print_table
import sys


while True:
    print_table()
    check_num = input(" > ")
    if check_num == "1" :
        if User.login():
            while True:
                home_page()
                op = input(" > ")
                if op =="1":
                    pass
                elif op == "2":
                    pass
                elif op == "3":
                    pass
                elif op == "4":
                    pass
                else:
                    print_table("qaydadan urinib koring ")

    elif check_num == "2" :
        User.create_user()
    elif check_num == "3":
        sys.exit(0)
    else:
        sys.exit(1)
        

    




# User.create_user()




    
