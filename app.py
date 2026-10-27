from sqlalchemy.orm import Session
from main3 import engine, Product, User, Time_reg
import datetime

with Session(engine) as session:
    product = Product(name="Ноутбук", price=79999.90)
    user = User(name="api", is_admin= True, second_name = "fs")
    reg = Time_reg(name="api", is_admin= True, registration = datetime.datetime.now())
    session.add(product)
    session.add(user)
    session.add(reg)
    session.commit()
    print(product.name, product.id)
    print(user.name, user.id)
    print(reg.name, reg.id)