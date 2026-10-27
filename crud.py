from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from main3 import engine, Product

def create_product(name, price):
    with Session(engine) as session:
        product = Product(name= name, price= price)
        session.add(product)
        session.commit()
        print(product.id)
        
def get_product(pr_id):
    with Session(engine) as session:
        sel = select(Product.name, Product.price, Product.id).where(Product.id == pr_id)
        result = session.execute(sel)
        products = result.all()
        print(products)
        
def update_product(id, new_price):
    with Session(engine) as session:
        upd = update(Product).where(Product.id == id).values(price = new_price)
        session.execute(upd)
        session.commit()
        print(True)
        
def delete_product(id):
    with Session(engine) as session:
        deleteing = delete(Product).where(Product.id == id)
        session.execute(deleteing)
        session.commit()
        print(True)
        
def delete_product(id):
    with Session(engine) as session:
        deleteing = delete(Product).where(Product.id == id)
        session.execute(deleteing)
        session.commit()
        print(True) 
        
def get_product(min_price):
    with Session(engine) as session:
        sel = select(Product.name, Product.price, Product.id).where(Product.price >= min_price)
        result = session.execute(sel)
        for product in result.all():
            print(product.id, product.name, product.price)
        
delete_product(3)
update_product(1, 500)
get_product(2)
create_product("xghfgg", 7000)
get_product(800)