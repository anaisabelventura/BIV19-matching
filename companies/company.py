from enum import Enum


class Company:
    def __init__(self, name, package, desired_cycle, desired_areas, desired_students):
        self.name = name
        self.package = package
        self.desired_areas = desired_areas
        self.desired_cycle = desired_cycle
        self.desired_students = desired_students


class Package(Enum):
    DIAMOND = (4,)
    GOLD = (3,)
    SILVER = (2,)
    BRASS = (1,)

    def __init__(self, student_amount):
        self.student_amount = student_amount

    @property
    def get_package_student_number(self):
        return self.student_number
