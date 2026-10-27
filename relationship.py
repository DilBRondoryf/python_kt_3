from sqlalchemy.orm import Session
from datetime import datetime
from main3 import engine, User, Product, Order

# with Session(engine) as session:
#     admin = User(name="Trol", is_admin = True, created_at= datetime.now())
    
#     product1 = Product(name="nolo", price= 19088, created_by=admin)
#     product2 = Product(name="tron", price= 8742, created_by=admin)
    
#     session.add(admin)
#     session.commit()
    
#     print(product1.created_by_id)
#     print(product1.created_by.name)
    
#     for product in admin.products:
#         print(product.name)

with Session(engine) as session:
    user = User(name = "Artur", is_admin = True, created_at=datetime.now())
    order_1 = Order(total_price = 2345235, created_at=datetime.now(), user=user)
    order_2 = Order(total_price = 88885, created_at=datetime.now(), user=user)
    
    laptop = Product(name = "laptop", price = 34342.32)
    phone = Product(name = "phone", price = 34568.32)
    dog = Product(name = "dog", price = 4567.32)
    
    cat = Product(name = "cat", price = 7689.32)
    tea = Product(name = "tea", price = 5463.32)
    ice = Product(name = "ice", price = 6783.32)
    
    order_1.products.append(laptop)
    order_1.products.append(phone)
    order_1.products.append(dog)
    
    order_2.products.append(laptop)
    
    order_2.products.append(cat)
    order_2.products.append(tea)
    order_2.products.append(ice)
    
    session.add(order_1)
    session.add(order_2)
    session.commit()
    
    print("товары_1 \n")
    for product in order_1.products:
        print(product.name, product.price)
        
    print("")
        
    print("товары_2 \n")
    for product in order_2.products:
        print(product.name, product.price)
        
    print("")        

    print("заказ_2 \n")
    for order_1 in ice.orders:
        print(order_1.total_price, order_1.id)
        
    print("")
    
    print("заказ_1 \n")
    for order_1 in dog.orders:
        print(order_1.total_price, order_1.id)
            
    print("")     
        
    print("все заказы \n")
    for order_2 in user.orders:
        print(order_2.total_price, order_2.id)
        