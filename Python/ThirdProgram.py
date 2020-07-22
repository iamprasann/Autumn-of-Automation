import math

class Complex:
    def __init__(self, Re, Im):
        self.Re=Re
        self.Im=Im

    def add(self, b):
        Re_=self.Re+b.Re
        Im_=self.Im+b.Im
        c=Complex(Re_, Im_)
        return c

    def subtract(self, b):
        Re_=self.Re-b.Re
        Im_=self.Im-b.Im
        c=Complex(Re_, Im_)
        return c

    def multiply(self, b):
        Re_=self.Re*b.Re-self.Im*b.Im
        Im_=self.Re*b.Im+self.Im*b.Re
        c=Complex(Re_, Im_)
        return c

    def conjugate(self):
        Re_=self.Re
        Im_=-self.Im
        c=Complex(Re_, Im_)
        return c

    def modulus(self):
        value=self.Re*self.Re+self.Im*self.Im
        return math.sqrt(value)

    def inverse(self):
        Re_=self.Re/float(self.modulus()**2)
        Im_=-self.Im/float(self.modulus()**2)
        c=Complex(Re_, Im_)
        return c

    def divide(self, b):
        c=self.multiply(b.inverse)
        return c

    def display(self):
        res = str(self.Re)+" + "+str(self.Im)+"i"
        print(res)

if __name__=="__main__":
    a=Complex(3,4)
    a.display()
    a.conjugate().display()
    a.add(a.conjugate()).display()
    a.subtract(a.conjugate()).display()
    print(a.modulus())
    a.multiply(a.conjugate()).display()
