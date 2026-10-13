class Student:
    def __init__(self,name,id,grade):
        self.name=name
        self.id=id
        self.grade=grade
        
    def khara(self):
        print(f"Name:{self.name}")
        print(f"ID:{self.id}")
        print(f"Grade:{self.grade}")
        
if __name__ == "__main__":
    s1 = Student("Youssef", 202501148, "A+")
    s1.khara()