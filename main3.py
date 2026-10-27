from sqlalchemy import create_engine, Integer, String, Boolean, DateTime, Float, Column, ForeignKey, Float, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

order_product = Table(
    "order_product",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(String(150), nullable=True)
    
    created_by_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable = True)
    created_by: Mapped[User] = relationship(back_populates="products")
    
    orders: Mapped[list[Order]] = relationship(secondary=order_product, back_populates="products")
    
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    
    products: Mapped[list[Product]] = relationship(back_populates="created_by")
    
    orders: Mapped[list[Order]] = relationship(back_populates="user")
    
class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    total_price: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="orders")
    
    products: Mapped[list[Product]] = relationship(secondary=order_product, back_populates="orders")

        
engine = create_engine("sqlite:///shop.db")
# Base.metadata.create_all(engine)