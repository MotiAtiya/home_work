class User:
    def __init__(self, age):
        self.age = age


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not 0 <= age <= 120:
            raise ValueError("age must be 0-120")
        self.__age = age

