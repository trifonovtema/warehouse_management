from dataclasses import dataclass, field
from typing import List


@dataclass
class Category:
    id: int | None
    name: str
    description: str | None = None


@dataclass
class Product:
    id: int | None
    name: str
    quantity: int
    price: float
    category: Category


@dataclass
class Order:
    id: int | None
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)
