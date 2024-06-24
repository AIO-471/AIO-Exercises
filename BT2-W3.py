class Person():
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob
        
    def describe(self):
        pass
    def get_yob(self):
        return self._yob
    
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade
        
    def describe(self):
        print (f"Student - Name:{self._name}- YoB:{self._yob} - Grade: {self.__grade}")

student1 = Student('Thai', 2008, 10)


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject
        
    def describe(self):
        print (f"Teacher - Name:{self._name}- YoB:{self._yob} - Subject: {self.__subject}")

teacher1 = Teacher('Truc', 1988, "Math")
teacher2 = Teacher('Hai', 1980, "English")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist
        
    def describe(self):
        print (f"Doctor - Name:{self._name}- YoB:{self._yob} - Specialist: {self.__specialist}")

doctor1 = Doctor('Thien', 1980, "CK1")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()
    
    def add_person(self, person:Person):
        self.__list_people.append(person)
        
    def describe(self):
        print(f'Name:{self.__name}')
        for p in self.__list_people:
            p.describe()
    
    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance (p,Doctor):
                counter +=1
        return counter
    
    def sort_yob(self):
        return self.__list_people.sort(key= lambda x: x.get_yob(), reverse= True)
        
    def compute_average(self):
        total = 0
        counter = 0
        for p in self.__list_people:
            if isinstance (p, Teacher):
                counter +=1
                total += p.get_yob()
        return total/counter   
            
ward1 = Ward('Ward1')
ward1.add_person(student1)
ward1.add_person(doctor1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.describe()
print(ward1.count_doctor())
ward1.sort_yob()
ward1.describe()
print(ward1.compute_average())
