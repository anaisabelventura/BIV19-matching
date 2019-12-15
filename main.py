from areas import *
from company import *
from courses import *
from rule import *
from rule_aux import *
from student import *
from pathlib import Path
import xlrd

file_path = input("Enter the path for the excel file: ")


# Opening file to work with
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(1)

i = 1

for row in sheet.get_rows():
	print(row)


# This list will contain the object students created during the cycles
students = []
companies = []

# Main cycle:
#for i in range(72):  # 72 is the number of enrolled students
	#students.append(Student(student_names[i], student_numbers[i], student_degrees[i], student_year[i], "lista ascendente de preferências"))

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

