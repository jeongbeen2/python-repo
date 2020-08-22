class Human():

    def __init__(self,**kwargs):
        self.arms = 2
        self.legs = 2
        self.teeth = 24
        self.heart = 1
        self.age = kwargs.get("age","20")
        self.height = kwargs.get("height","170")

    def say_hello(self,name):
        print(f"Hello! my name is {name}")


jeongBeen = Human(age = "26", height = "174")
