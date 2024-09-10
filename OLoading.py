class Product:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
    
    def __divmod__(self, other):
        return self.price, other.price
    

p1 = Product("Keyboard", 600)
p2 = Product('Mouse', 400)
print(p1, p2)
