# Warehouse Management System

This repository contains a Python-based Warehouse Management System (WMS) developed using clean architecture principles. The system allows for managing products, categories, and orders in a warehouse.

## Features

- Product Management: Add, retrieve, and list products with attributes such as name, price, quantity, and category.
- Category Management: Create, retrieve, and list product categories.
- Order Management: Manage orders containing multiple products.
- Database Integration: Uses SQLAlchemy for ORM and SQLite as the default database backend.
- Pre-commit Hooks: Ensures code quality using tools like Black, isort, mypy, and flake8.