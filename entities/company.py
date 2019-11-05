from enum import Enum

class Company:
    studentMatches = []

    def __init__(self, name, package, desired_years):
        self.name = name
        self.package = package
        self.desired_years = desired_years

    def getMatchingLevel(self, student):
        matchingLevel = 0
        
        self.studentMatches.append((student, matchingLevel))

class Package(Enum):
    DIAMOND = 40
    GOLD = 30
    SILVER = 20
    BRASS = 10
