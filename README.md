# Coffe-shop_challenge

This is a Python OOP project that models a simple coffee shop system. It features three main classes: `Customer`, `Coffee`, and `Order`, designed to reflect real-world relationships between customers, the coffees they order, and the orders themselves.

---

## Project Overview

This project models a coffee shop using object-oriented programming (OOP) concepts in Python. It focuses on:

- Class creation
- Property decorators
- Data validation
- Object relationships
- Class methods

---

## Models

### 1. `Customer`

- Stores a name (1–15 characters).
- **Properties**:
  - `name` (get/set)
- **Methods**:
  - `Customer.most_aficionado(coffee)` → returns the customer who spent the most on a given coffee.

### 2. `Coffee`

- Stores a coffee name (minimum 3 characters).
- **Properties**:
  - `name` (read-only / immutable)

### 3. `Order`

- Links a `Customer` and `Coffee` with a price.
- **Properties**:
  - `customer` (immutable)
  - `coffee` (immutable)
  - `price` (immutable, float between 1.0 and 10.0)

---

## 🔗 Relationships

- A **Customer** has many **Orders**
- A **Coffee** has many **Orders**
- An **Order** belongs to one **Customer** and one **Coffee**
- This creates a **many-to-many relationship** between Customers and Coffees via Orders

## how to run

1. clone the repo
   bash: git clone git@github.com:Gitkorir/Coffe-shop_challenge.git
2. run the project
   bash: python debug.py

## Auther

NAME: Arnold Kiprop Korir
