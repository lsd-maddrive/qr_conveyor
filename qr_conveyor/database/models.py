from sqlalchemy import Boolean, Column, Enum, Float, ForeignKey, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    size = Column(Enum('small', 'medium', 'large', name='product_size'), nullable=False)
    fragile = Column(Boolean, nullable=False)
    status_id = Column(ForeignKey('status.id'), index=True)

    def __repr__(self):
        return (f"<Product(name='{self.name}', "
                f"weight={self.weight}, "
                f"size='{self.size}', "
                f"fragile={self.fragile})>")
