# coding=utf-8
from builtins import range

from areas import *
from company import *
from courses import *
from rule import *
from rule_aux import *
from student import *
from pathlib import Path
from excel import OpenExcel

companies = []
students = []

# Change file path according to where the file to work with is on
file_path = Path("C:\Users\sofys\OneDrive\Ambiente de Trabalho" "[BIV] Registration Form (Responses).xlsx")

# Opening file to work with
file = OpenExcel(file_path)

# Getting the input from the file. [1:] was used to remove the title of the column
student_names = file.read("E")[1:]
student_numbers = file.read("J")[1:]
student_degrees = file.read("F")[1:]
student_year = file.read("H")[1:]

# This list will contain the object students created during the cycles
list_of_students = []

# Main cycle:
for i in range(72):  # 72 is the number of enrolled students
    list_of_students.append(Student(student_names[i], student_numbers[i], student_degrees[i], student_year[i], "lista ascendente de preferências"))

for company in companies:
	perfect_students = []
	for student in students:
        rule = CriteriaStudentWantsCompany(company, student)
        if rule.validate():
			if company.package == "DIAMOND" or company.package == "GOLD":
				rule1 = CriteriaCorrespondingArea(company, student)
				rule2 = CriteriaCorrespondingCycle(company, student)
				if rule1.validate() and rule2.validate():
					perfect_students += student
			else:



