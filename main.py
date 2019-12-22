import xlrd

from company import Company
from rule import *
from student import *

'''
5 - Deloitte
6 - OLX Group
7 - Energetus
8 - JLL/Tetris
9 - Novabase
10 - JETsj
11 - Oak Peak
12 - Instituto de Soldadura e Qualidade
13 - Grupo ETE
14 - Engidro
15 - Premium Minds
16 - Skyline Communications
17 - Grupo de Lasers e Plasma
18 - Sidul
19 - Nerd Monkeys
20 - Life Emotions
21 - JSJ Structural Engineering
22 - Introsys
23 - IBM
24 - Slefty
'''

# This list will contain the object students created during the cycles
students = []

# Opening file to work with
try:
	wb = xlrd.open_workbook('students.xlsx')
except FileNotFoundError:
	print('Error while loading company file. Make sure it is called \'students.xlsx\'')
	exit(1)

sheet = wb.sheet_by_index(0)

# Converting from generator to list
rows = list(sheet.get_rows())

# Control variables
n_companies = len(rows[0]) - 5
index_start = 5
index_end = index_start + n_companies

# Creating student profiles
for row in rows:
	name = row[0].value
	number = row[1].value
	degree = row[2].value
	year = int(row[3].value)
	preferences = []

	for i in range(index_start, index_end):
		if row[i].value == '':
			preferences.append(0)
		else:
			preferences.append(int(row[i].value))

	students.append(Student(name, number, degree, year, preferences))

companies = []

# Opening file to work with
try:
	wb = xlrd.open_workbook('companies.xlsx')
except FileNotFoundError:
	print('Error while loading company file. Make sure it is called \'companies.xlsx\'')

sheet = wb.sheet_by_index(0)

# Converting from generator to list
rows = list(sheet.get_rows())

company_id = 0

# Creating company profiles
for row in rows:
	name = row[0].value
	package = row[1].value
	if package == 'Diamond' or package == 'Gold':
		cycles = row[2].value
		preferences = row[3].value
		companies.append(Company(company_id, name, package, cycles, preferences))
	else:
		companies.append(Company(company_id, name, package, '', []))

	company_id += 1


# Actual matching
while len(students) > 0:
	for company in companies:
		perfect_students = []
		corresponding_area_students = []
		corresponding_cycle_students = []
		average_students = []

		'''if company.package.upper() == 'DIAMOND' and len(company.assigned_students) == 4:
			continue
		elif company.package.upper() == 'GOLD' and len(company.assigned_students) == 3:
			continue'''
		if company.package.upper() == 'SILVER' and len(company.assigned_students) == 2:
			continue
		elif company.package.upper() == 'BRASS' and len(company.assigned_students) == 1:
			continue

		for student in students:
			rule = CriteriaStudentWantsCompany(company, student)
			if rule.validate():
				if company.package.upper() == 'DIAMOND' or company.package.upper() == 'GOLD':
					rule1 = CriteriaCorrespondingArea(company, student)
					rule2 = CriteriaCorrespondingCycle(company, student)

					if rule1.validate() and rule2.validate():
						perfect_students.append(student)
					elif rule1.validate():
						corresponding_area_students.append(student)
					elif rule2.validate():
						corresponding_cycle_students.append(student)
					else:
						average_students.append(student)
				else:
					average_students.append(student)
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
				company.assigned_students.append(max_student)


f = open('output.txt', 'w')
for company in companies:
	f.write(f'{company.name}: ')
	for student in company.assigned_students:
		f.write(student.name)
		f.write(', ')
	f.write('\n')


