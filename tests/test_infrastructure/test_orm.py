import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.orm import Base, CategoryOrm, ProductOrm


@pytest.fixture
def sqlite_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return session()


def test_insert_and_query_product(sqlite_session):
    session = sqlite_session
    category = CategoryOrm(name="Electronics", description="Electronic gadgets")
    product = ProductOrm(name="Smartphone", quantity=10, price=500.0, category=category)

    session.add(category)
    session.add(product)
    session.commit()

    retrieved_product = session.query(ProductOrm).filter_by(name="Smartphone").one()
    assert retrieved_product.name == "Smartphone"
    assert retrieved_product.category.name == "Electronics"


def test_category_relationship(sqlite_session):
    session = sqlite_session
    category = CategoryOrm(name="Books", description="Fictional Books")
    product1 = ProductOrm(name="Book A", quantity=5, price=20.0, category=category)
    product2 = ProductOrm(name="Book B", quantity=3, price=25.0, category=category)

    session.add(category)
    session.add_all([product1, product2])
    session.commit()

    retrieved_category = session.query(CategoryOrm).filter_by(name="Books").one()
    assert len(retrieved_category.products) == 2
