from termcolor import colored


def print_status(text, status):
    status_map = {
        'error': 'red',
        'succes': 'green'
    }
    text = colored(text, status_map.get(status, 'red'))
    print(text)

def print_table():
    print("1)login \n 2)registratsiya \n 3)chiqish")

def home_page():
    print("1) Maxsulotlar royxati \n 2) savatga qoshish \n 3) maxsulotni qidirish \n maxsulotni sotib olish") 

def print_products(products_list):
    for i, product in enumerate(products_list, start=1):
        print(f"{1}) {product['name']} - {product['price']} som")        