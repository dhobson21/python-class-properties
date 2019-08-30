# SOLID STURDENT EXERCISE AND CONVERT STUDENT OBJECT TO STRING EXERCISE

#Define a Python class named Student. This class will have 5 properties.

#First name (string)
#Last name (string)
#Age (integer)
#Cohort number (integer)
#Full name (read-only string)

class Student:



#Define getters for all properties.
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0
    @property
    def full_name(self):
        try:
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return 0

#Define a setter for all but the read only property.
    @first_name.setter # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else: raise TypeError('Please provide a name for the firstname')

    @last_name.setter # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else: raise TypeError('Please provide a name for the lastname')

    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else: raise TypeError('Please provide a whole number for the age')

    @cohort_number.setter # The setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else: raise TypeError('Please provide a name for the lastname')
    #Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"

Dustin = Student()
Dustin.first_name = "Dustin"
Dustin.last_name = "Hobson"
Dustin.age = 30
Dustin.cohort_number = 33
#The full name property should return first name and last name separated by a space. It's value cannot be set.
print(Dustin)


