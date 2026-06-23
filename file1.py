class praka:
    def __init__(self,name ,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)  
p1=praka("Alice", 30)
p1.display()