from main import \
    create_user,\
    update_or_create_address,\
    create_product,\
    read_product,\
    update_product,\
    remove_product,\
    product_purchase,\
    all_purchases_of_user,\
    filter_purchases,\
    current_session
from models import User


def interface():
    choise = int(input("What do you wont to work with?\n1. User.\n2. Product.\n3. Purchases.\n"))
    if choise == 1:
        user()
    elif choise == 2:
        product()
    elif choise == 3:
        purchase()


def user():
    choise = int(input("Select an action:\n1. Create user.\n2. Update or create address.\n"))
    if choise == 1:
        email = input("Enter an email: ")
        password = input("Enter the password: ")
        phone = input("Enter phone number: ")
        age = input("Enter the age: ")
        city = input("Enter the city: ")
        address = input("Enter the address: ")
        create_user(current_session, email, password, phone, age, city, address)
    elif choise == 2:
        user_email = input("Enter the user's email: ")
        user = current_session.query(User).filter_by(email=user_email).first()
        city = input("Enter the city: ")
        address = input("Enter the address: ")
        update_or_create_address(current_session, user, city, address)


def product():
    choise = int(input("Select an action:\n\
1. Create product.\n2. Read product.\n3. Update product.\n4. Remove product.\n"))
    if choise == 1:
        name = input("Enter the product name: ")
        price = input("Enter the product price: ")
        quantity = input("Enter the product quantity: ")
        comment = input('Enter a comment on the product [""]: ')
        create_product(current_session, name, price, quantity, comment)
    elif choise == 2:
        name = input("Enter the product name: ")
        print(read_product(current_session, name))
    elif choise == 3:
        id = int(input("Enter the id of the product you want to update: "))
        new_name = input("Enter a new product name: ")
        new_price = int(input("Enter a new product price: "))
        new_quantity = int(input("Enter a new product quantity: "))
        update_product(current_session, id, new_name, new_price, new_quantity)
    elif choise == 4:
        id = int(input("Enter the id of the product you want to remove: "))
        remove_product(current_session, id)


def purchase():
    choise = int(input("Select an action:\n1. Product purchase.\n2. Show all user purchases.\n3. Filter purchases.\n"))
    if choise == 1:
        user_id = int(input("Enter the ID of the user who made the purchase: "))
        product_id = int(input("Enter the ID of the product that was purchased: "))
        count = int(input("Enter the quantity of the purchased item: "))
        product_purchase(current_session, user_id, product_id, count)
    elif choise == 2:
        user_id = int(input("Enter the ID of the user whose purchases you need: "))
        print(list(map(str, all_purchases_of_user(current_session, user_id))))
    elif choise == 3:
        parameters = {}
        while True:
            key = input('Enter the column name or "stop" to finish: ')
            if key.lower() == "stop":
                break
            value = input("Enter the column value: ")
            parameters[key] = value
        filter_purchases(current_session, **parameters)


if __name__ == "__main__":
    interface()
