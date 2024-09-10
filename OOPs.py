class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def print(self):
        print(f"{self.real} + i {self.imag}")

    def add(self, c):
        self.real += c.real
        self.imag += c.imag

# Correcting the variable names and method calls
c1 = Complex(10, 20)
c1.print()  # This will print the initial values of c1

c2 = Complex(20, 30)  # Correctly creating another Complex object
c1.add(c2)  # Adding c2 to c1
c1.print()  # Printing the values of c1 after addition

