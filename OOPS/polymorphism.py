class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real , "i +", self.img, "j")

    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)
    
num1 = Complex(1,3)
num1.showNum()

num2 = Complex(3,5)
num2.showNum()

num3 = Complex(4,6)
num3.showNum()

num4 = num2 + num3
num4.showNum()
#-------------------------------------------------------------------#