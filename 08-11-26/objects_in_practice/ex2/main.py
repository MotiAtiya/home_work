from classes.customer import Customer
from classes.order import Order

moti = Customer("moti", "Haifa")

order_1 = Order(moti, 200)
order_2 = Order(moti, 50)

print(order_1.customer.city, order_2.customer.city)

moti.city = "Tel Aviv"
print(order_1.customer.city, order_2.customer.city)
