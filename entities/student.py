class Student:
    def __init__(self, name, email, degree, cycle, year, preferences):
        self.name = name
        self.email = email
        self.degree = degree
        self.cycle = cycle
        self.year = year
        self.preferences = preferences

    def matchesCompanyPreference(self, companyName):
        return self.preferences.contains(companyName)

    #def matchesDegree(self, area):
