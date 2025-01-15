from sqlalchemy.orm import Session

from domain.models import Category, Order, Product
from domain.repositories import CategoryRepository, OrderRepository, ProductRepository

from .orm import CategoryOrm, OrderOrm, ProductOrm


class SqlAlchemyProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: Product):
        product_orm = ProductOrm(
            name=product.name,
            quantity=product.quantity,
            price=product.price,
            category_id=product.category.id,
        )
        self.session.add(product_orm)
        return product_orm

    def get(self, product_id: int) -> Product:
        product_orm = self.session.query(ProductOrm).filter_by(id=product_id).one()
        category = Category(
            id=product_orm.category.id,
            name=product_orm.category.name,
            description=product_orm.category.description,
        )
        return Product(
            id=product_orm.id,
            name=product_orm.name,
            quantity=product_orm.quantity,
            price=product_orm.price,
            category=category,
        )

    def list(self) -> list[Product]:
        products_orm = self.session.query(ProductOrm).all()
        return [
            Product(
                id=p.id,
                name=p.name,
                quantity=p.quantity,
                price=p.price,
                category=Category(
                    id=p.category.id,
                    name=p.category.name,
                    description=p.category.description,
                ),
            )
            for p in products_orm
        ]


class SqlAlchemyOrderRepository(OrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order):
        order_orm = OrderOrm()
        order_orm.products = [
            self.session.query(ProductOrm).filter_by(id=p.id).one()
            for p in order.products
        ]
        self.session.add(order_orm)
        return order_orm

    def get(self, order_id: int) -> Order:
        order_orm = self.session.query(OrderOrm).filter_by(id=order_id).one()
        products = [
            Product(
                id=p.id,
                name=p.name,
                quantity=p.quantity,
                price=p.price,
                category=Category(
                    id=p.category.id,
                    name=p.category.name,
                    description=p.category.description,
                ),
            )
            for p in order_orm.products
        ]
        return Order(id=order_orm.id, products=products)

    def list(self) -> list[Order]:
        orders_orm = self.session.query(OrderOrm).all()
        orders = []
        for order_orm in orders_orm:
            products = [
                Product(
                    id=p.id,
                    name=p.name,
                    quantity=p.quantity,
                    price=p.price,
                    category=Category(
                        id=p.category.id,
                        name=p.category.name,
                        description=p.category.description,
                    ),
                )
                for p in order_orm.products
            ]
            orders.append(Order(id=order_orm.id, products=products))
        return orders


class SQLAlchemyCategoryRepository(CategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, category: Category):
        category_orm = CategoryOrm(
            id=category.id, name=category.name, description=category.description
        )
        self.session.add(category_orm)
        return category_orm

    def get(self, category_id: int) -> Category:
        category_orm = self.session.query(CategoryOrm).filter_by(id=category_id).one()
        return Category(
            id=category_orm.id,
            name=category_orm.name,
            description=category_orm.description,
        )

    def list(self) -> list[Category]:
        categories_orm = self.session.query(CategoryOrm).all()
        return [
            Category(id=c.id, name=c.name, description=c.description)
            for c in categories_orm
        ]
