from sqlalchemy.orm import sessionmaker, Session

from models import User, Address, Profile, Base
from utils import setup_db_engine, create_database_if_not_exists


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


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    user = current_session.query(User).filter_by(email="test@test.com").first()
    update_or_create_address(
        session=current_session,
        user=user,
        city="Old City",
        address="Old Address"
    )
