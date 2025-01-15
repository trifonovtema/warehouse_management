from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.services import WarehouseService
from infrastructure.database import DATABASE_URL
from infrastructure.orm import Base
from infrastructure.repositories import (
    SQLAlchemyCategoryRepository,
    SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
)
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main(category_repo=None):
    uow = SqlAlchemyUnitOfWork(SessionFactory)

    with uow:
        product_repo = SqlAlchemyProductRepository(uow.session())
        order_repo = SqlAlchemyOrderRepository(uow.session())
        category_repo = SQLAlchemyCategoryRepository(uow.session())
        warehouse_service = WarehouseService(product_repo, order_repo, category_repo)

        # Create a new category
        new_category = warehouse_service.create_category(
            name="Electronics", description="Electronic gadgets"
        )
        uow.commit()
        print(f"Created category: {category_repo.get(new_category.id)}")

        # Create a new product
        new_product = warehouse_service.create_product(
            name="Smartphone",
            quantity=10,
            price=500.0,
            category=new_category,
        )
        uow.commit()
        print(f"Created product: {product_repo.get(new_product.id)}")

        # List all products
        products = product_repo.list()
        print("List of products:")
        for product in products:
            print(
                f"- {product.id} - {product.name}: {product.quantity} units at ${product.price} each"
            )

        # Create an order
        new_order = warehouse_service.create_order(products=[new_product])
        uow.commit()
        print(f"Created order: {order_repo.get(new_order.id)}")

        # List all orders
        orders = order_repo.list()
        print("List of orders:")
        for order in orders:
            print(
                f"Order ID: {order.id}, Products: {[product.name for product in order.products]}"
            )


if __name__ == "__main__":
    main()
