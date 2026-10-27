from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from main3 import engine, Product, User, Time_reg

# with Session(engine) as session:
#     product = session.get(Product, 1)
#     product.name = "Поменял имя данному продукту"
#     session.commit()
    
# with Session(engine) as session:
#     deleteing = delete(Product).where(Product.name == "Ноутбук")
#     session.execute(deleteing)
#     session.commit()
    
with Session(engine) as session:
    upd = update(Product).where(Product.name == "Ноутбук").values(price = 54300, name ="Ноутбук88")
    session.execute(upd)
    session.commit()