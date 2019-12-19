import constants as CONSTANT


class Student:
    def __init__(self, name, number, degree, year, preferences):
        self.name = name
        self.number = number
        self.degree = degree
        self.preferences = preferences

        if year >= 4:
            self.cycle = CONSTANT.MASTERS
        else:
            self.cycle = CONSTANT.BACHELORS
