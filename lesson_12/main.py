from sqlalchemy.orm import sessionmaker, Session

from models import User, Address, Profile, Base, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists

engine = setup_db_engine()
create_database_if_not_exists(engine=engine)

Base.metadata.create_all(engine)
CurrentSession = sessionmaker(bind=engine)
current_session = CurrentSession()


def create_user(
        session: Session, email: str, password: str, phone: str, age: int, city: str, address: str
) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)
    session.add_all((user, profile, address))
    session.commit()

    return user


def update_or_create_address(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address.city = city
        current_address.address = address
    else:
        address = Address(user=user, city=city, address=address)

    session.add(current_address)
    session.commit()

    return address


def create_product(
        session: Session, name: str, price: int, quantity: int, comment: str = ""
) -> Product:
    product = Product(name=name, price=price, quantity=quantity, comment=comment)
    session.add(product)
    session.commit()

    return product


def read_product(session: Session, name: str) -> Product:
    product = session.query(Product).filter_by(name=name).first()
    return product


def update_product(session: Session, id: int, new_name: str, new_price: int, new_quantity: int):
    session.query(Product).filter_by(id=id).update({
        "name": new_name,
        "price": new_price,
        "quantity": new_quantity
    })
    session.commit()


def remove_product(session: Session, id: int):
    product = session.query(Product).filter(Product.id == id).one()
    session.delete(product)
    session.commit()


def product_purchase(session: Session, user_id: int, product_id: int, count: int) -> Purchase:
    purchase = Purchase(user_id=user_id, product_id=product_id, count=count)
    session.add(purchase)
    session.commit()
    return purchase


def all_purchases_of_user(session: Session, user_id: int) -> Purchase:
    return session.query(Purchase).filter_by(user_id=user_id).all()


def purchases_to_string(session: Session, purchase: Purchase):
    user_email = session.query(User).filter_by(id=purchase.user_id).first()
    product_name = session.query(Product).filter_by(id=purchase.product_id).first()
    print(f"{user_email} bought {product_name}")


def filter_purchases(session: Session, **kwargs):
    return session.query(Purchase).filter_by(**kwargs).all()
