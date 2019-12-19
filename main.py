
from areas import *
from company import *
from courses import *
from rule import *
from rule_aux import *
from student import *
from pathlib import Path
import xlrd

# import students data
file_path_students = input("Enter the path for the students data file: ")

# This list will contain the object students created during the cycles
students = []

# Opening file to work with
wb = xlrd.open_workbook(file_path_students)
sheet = wb.sheet_by_index(1)

# Converting from generator to list, excluding header row
rows = list(sheet.get_rows())[1:]

# Control variables
n_companies = 20
index_start = 8
index_end = index_start + n_companies

# Creating student profiles
for row in rows:
	name = row[2].value
	number = row[4].value
	degree = row[3].value
	year = int(row[5].value)
	preferences = []

	for i in range(index_start, index_end):
		if row[i].value == '':
			preferences.append(0)
		else:
			preferences.append(int(row[i].value))

	students.append(Student(name, number, degree, year, preferences))

# Importing companies from spreadsheet
file_path_companies = input("Enter the path for the companies data file: ")

companies = []

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