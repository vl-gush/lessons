from faker import Faker
from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Profile, Address, Purchase, Product
from utils import setup_db_engine, create_database_if_not_exists

fake = Faker()


def generate_user(session):
    user = User(
        email=fake.email(), password=fake.word()
    )
    profile = Profile(
        user=user, phone=fake.phone_number(), age=fake.pyint(min_value=18, max_value=60)
    )
    address = Address(
        user=user, city=fake.city(), address=fake.address()
    )
    session.add_all([user, profile, address])
    session.commit()
    return user


def generate_purchase(session):
    user = generate_user(session)
    product = Product(name=fake.company(), price=fake.pyfloat(min_value=20, max_value=100))
    purchase = Purchase(
        user=user, product=product, count=fake.pyint(min_value=1, max_value=5)
    )
    session.add_all([product, purchase])
    session.commit()


def all_products_purchased_by_user(session: Session, user_id):
    result = session.query(User).join(Purchase).join(Product).filter(
        User.id == user_id
    ).all()
    return result


def users_purchased_for_amount_of(session: Session, amount: int):
    result = session.query(User).join(Purchase).join(Product).filter(
        (Product.price * Purchase.count) > amount
    ).all()
    return result


def all_users_purchased_product(session: Session, product_name: str):
    result = session.query(User).join(Purchase).join(Product).filter(
        Product.name == product_name
    ).all()
    return result


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    a = all_users_purchased_product(current_session, "Flores Ltd")
    for b in a:
        print(b)
