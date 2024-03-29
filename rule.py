from builtins import len
from rule_aux import *


class Criteria:
	"""Abstract concept to represent a criteria"""
	def __init__(self, company, student):
		self.company = company
		self.student = student

	def validate(self):
		pass


class CriteriaCorrespondingArea(Criteria):
	def validate(self):
		"""Iterates through all the areas the company wants. Returns true if student course is in desired area"""
		if self.company.desired_courses != [] and self.student.degree in self.company.desired_courses:
			return True
		return False


class CriteriaCorrespondingCycle(Criteria):
	def validate(self):
		"""True if the students cycle is the same as the cycle the company is looking for"""
		return self.student.cycle == self.company.desired_cycle


class CriteriaStudentWantsCompany(Criteria):
	def validate(self):
		"""True if the student wants the company"""
		return self.student.preferences[self.company.company_id] != 0
