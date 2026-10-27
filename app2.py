from sqlalchemy import select
from sqlalchemy.orm import Session
from main3 import engine, Product, User, Time_reg

with Session(engine) as session:
    sel = select(Product.name, Product.price, Product.id).where(Product.name.like("Н%"))
    result = session.execute(sel)
    for product in result.all():
        print(product.id, product.name, product.price)