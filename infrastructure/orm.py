from typing import Any

from sqlalchemy import Column, Float, ForeignKey, Integer, Sequence, String, Table
from sqlalchemy.orm import declarative_base, relationship

Base: Any = declarative_base()


class ProductOrm(Base):
    __tablename__ = "products"
    id = Column(Integer, Sequence("product_id_seq"), primary_key=True)
    name = Column(String)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("CategoryOrm", back_populates="products")


order_product_assocoations = Table(
    "order_product_assocoations",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id")),
)


class OrderOrm(Base):
    __tablename__ = "orders"
    id = Column(Integer, Sequence("order_id_seq"), primary_key=True)
    products = relationship("ProductOrm", secondary=order_product_assocoations)


class CategoryOrm(Base):
    __tablename__ = "categories"
    id = Column(Integer, Sequence("category_id_seq"), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    products = relationship("ProductOrm", back_populates="category")
