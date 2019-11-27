from builtins import len
from rule_aux import *


class Criteria:
	def __init__(self, company, student):
		self.company = company
		self.student = student

	def validate(self):
		pass


class CriteriaCorrespondingArea(Criteria):
	def validate(self):
		"""Iterates throught all the areas the company wants. Returns true if student course is in desired area"""
		for area in self.company.desired_areas:
			if area.courses.contains(self.student.degree):
				return True
		return False


class CriteriaCorrespondingCycle(Criteria):
	def validate(self):
		"""True if the students cycle is the same as the cycle the company is looking for"""
		return self.student.cycle == self.company.desired_cycle


class CriteriaStudentWantsCompany(Criteria):
	def validate(self):
		"""True if the student wants the company"""
		if len(self.student.preferences) <= 5:
			return self.student.preferences.contains(self.company)
		else:
			return self.student.preferences.contains(self.company) \
				and self.student.preferences[self.company.name] >= get_preference_average(self.student.preferences)


class CriteriaCompanyHasStudentInTop3(Criteria):
	def validate(self):
		return self.company.desired_students.contains(self.student)
