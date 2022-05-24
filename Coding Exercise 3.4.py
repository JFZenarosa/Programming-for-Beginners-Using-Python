#Coding Exercise 3.4
class Customer:
  greeting = "Welcome to Coffee Palace!"

c1 = Customer()
c1.name = "Samirah"
c1.beverage = "Iced Caffe Latte"
c1.food = "Cinnamon roll"
c1.total = 225

c2 = Customer()
c2.name = "Jerry"
c2.beverage = "Caramel Macchiato"
c2.food = "Glazed doughnut"
c2.total = 230

print(Customer.greeting)
print(c1.beverage)
print(c2.food)