class Company:
    def __init__(self, company_id, name, package, desired_cycle, desired_courses):
        self.company_id = company_id
        self.name = name
        self.package = package
        self.desired_courses = desired_courses
        self.desired_cycle = desired_cycle
        self.assigned_students = []
