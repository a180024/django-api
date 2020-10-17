from datetime import date 
  
class Person: 
    gender = None
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a  
    # Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 

    @classmethod
    def setGender(cls, gender):
        cls.gender = gender
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 21 
  
#  person2 = Person.fromBirthYear('mayank', 1996)

  
#  print (person1.age)
#  print (person2.age)

#  # print the result
#  print (Person.isAdult(22))
