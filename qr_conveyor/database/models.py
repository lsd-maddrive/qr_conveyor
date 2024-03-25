from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
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
