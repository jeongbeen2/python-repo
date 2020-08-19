class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self,to_name):
        print("안녕 내이름은 " + self.name + " 나이는 " + str(self.age) + "살" + to_name +" 안녕?")

    def encorage(self,to_name):
        print("힘내, " + to_name +"! "+ self.name + "이가.")

class Police(Person):
    def arrest(self,to_name):
        print(to_name + ", 너는 체포되었다! 내마음속에. 내이름은 " + self.name)

jeongBeen = Police("정빈", 26)
dongHu =  Person("동후", 30)
yunSang = Person("윤상", 25)

jeongBeen.arrest("서현")
dongHu.say_hello("호이")