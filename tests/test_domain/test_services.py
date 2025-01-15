import pytest

from domain.models import Category, Order, Product


@pytest.fixture
def sample_category():
    return Category(id=1, name="Electronics", description="Electronic gadgets")


@pytest.fixture
def sample_product(sample_category):
    return Product(
        id=1, name="Smartphone", quantity=10, price=500.0, category=sample_category
    )


@pytest.fixture
def sample_order(sample_product):
    order = Order(id=1)
    order.add_product(sample_product)
    return order


def test_add_product_to_order(sample_product, sample_order):
    initial_product_count = len(sample_order.products)
    sample_order.add_product(sample_product)
    assert len(sample_order.products) == initial_product_count + 1
    assert sample_order.products[-1].name == "Smartphone"


def test_calculate_total_order_price(sample_order):
    total_price = sum(
        product.price * product.quantity for product in sample_order.products
    )
    assert total_price == 5000.0
