from infrastructure.orm import CategoryOrm, OrderOrm, ProductOrm

from .models import Category, Order, Product
from .repositories import CategoryRepository, OrderRepository, ProductRepository


class WarehouseService:
    def __init__(
        self,
        product_repo: ProductRepository,
        order_repo: OrderRepository,
        category_repo: CategoryRepository,
    ):
        self.product_repo = product_repo
        self.order_repo = order_repo
        self.category_repo = category_repo

    def create_product(
        self, name: str, quantity: int, price: float, category: Category
    ) -> ProductOrm:
        product = Product(
            id=None, name=name, quantity=quantity, price=price, category=category
        )
        return self.product_repo.add(product)

    def create_order(self, products: list[Product]) -> OrderOrm:
        order = Order(id=None, products=products)
        return self.order_repo.add(order)
        # return order

    def create_category(self, name: str, description: str) -> CategoryOrm:
        category = Category(id=None, name=name, description=description)
        return self.category_repo.add(category)

        # return category
