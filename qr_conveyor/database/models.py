from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    size = Column(String)
    fragile = Column(Boolean)

    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship("Status", back_populates="products")

    def __repr__(self):
        return (f"<Product(name='{self.name}', "
                f"weight={self.weight}, "
                f"size='{self.size}', "
                f"fragile={self.fragile})>")


class Cells(Base):
    __tablename__ = 'cells'

    id = Column(Integer, primary_key=True)
    location = Column(Enum())

    inventory = relationship("Inventory", back_populates="cell")

    def __repr__(self):
        return (f"<Cell(id={self.id}, "
                f"location='{self.location})>")


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    status = Column(Enum('processed', 'unprocessed'))

    products = relationship("Product", back_populates="status")

    def __repr__(self):
        return (f"<Status(id={self.id},"
                f" status='{self.status}')>")


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    cell_id = Column(Integer, ForeignKey('cells.id'))
    timestamp = Column(DateTime)

    product = relationship("Product", back_populates="inventory")
    cell = relationship("Cell", back_populates="inventory")

    def __repr__(self):
        return (f"<Inventory(product_id={self.product_id}, "
                f"cell_id={self.cell_id}, "
                f"timestamp='{self.timestamp}')>")
