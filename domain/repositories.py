from abc import ABC, abstractmethod
from typing import List

from infrastructure.orm import CategoryOrm, OrderOrm, ProductOrm

from .models import Category, Order, Product


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> ProductOrm:
        pass

    @abstractmethod
    def get(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list(self) -> List[Product]:
        pass


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order) -> OrderOrm:
        pass

    @abstractmethod
    def get(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def list(self) -> List[Order]:
        pass


class CategoryRepository(ABC):
    @abstractmethod
    def add(self, category: Category) -> CategoryOrm:
        pass

    @abstractmethod
    def get(self, category_id: int) -> Category | None:
        pass

    @abstractmethod
    def list(self) -> List[Category]:
        pass
