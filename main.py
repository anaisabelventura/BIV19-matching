
from areas import *
from company import *
from courses import *
from rule import *
from rule_aux import *
from student import *
from pathlib import Path
import xlrd

#Import Student Data
file_path_students = input("Enter the path for the students file: ")
# This list will contain the object students created during the cycles
students = []

# Opening file to work with
wb = xlrd.open_workbook(file_path_students)
sheet = wb.sheet_by_index(1)

# Creating student profiles
for row in sheet.get_rows():
	name = row[2].value
	number = row[4].value
	degree = row[3].value
	year = row[5].value
	preferences = []

	for i in range(8, 28):
		if row[i].value != 0:
			# [number of column, how much he wants it]
			preferences += [i, row[i].value]
		else:
			pass

	students.append(Student(name, number, degree, year, preferences))

#Import Company Data
file_path_students = input("Enter the path for the students file: ")
# This list will contain the object students created during the cycles
students = []

# Opening file to work with
wb = xlrd.open_workbook(file_path_students)
sheet = wb.sheet_by_index(1)

# Creating student profiles
for row in sheet.get_rows():
	name = row[2].value
	number = row[4].value
	degree = row[3].value
	year = row[5].value
	preferences = []

	for i in range(8, 28):
		if row[i].value != 0:
			# [number of column, how much he wants it]
			preferences += [i, row[i].value]
		else:
			pass

	students.append(Student(name, number, degree, year, preferences))

for company in companies:
	perfect_students = []
	corresponding_area_students = []
	corresponding_cycle_students = []
	average_students = []
	for student in students:
		rule = CriteriaStudentWantsCompany(company, student)
		if rule.validate():
			if company.package == "DIAMOND" or company.package == "GOLD":
				rule1 = CriteriaCorrespondingArea(company, student)
				rule2 = CriteriaCorrespondingCycle(company, student)

				if rule1.validate() and rule2.validate():
					perfect_students += student
				elif rule1.validate():
					corresponding_area_students += student
				elif rule2.validate():
					corresponding_cycle_students += student
				else:
					average_students += student
			else:
				average_students += student
		else:
			pass
			# dont know what to do

	matching_students = [perfect_students, corresponding_area_students, corresponding_cycle_students, average_students]

	for lst in matching_students:
		if len(lst) > 0:
			max_want = lst[0].preferences[company.company_id]
			max_student = lst[0]
			for stdnt in lst:
				if stdnt.preferences[company.company_id] < max_want:
					max_want = stdnt.preferences[company.company_id]
					max_student = stdnt

			students.remove(max_student)
			company.assigned_students += max_student

