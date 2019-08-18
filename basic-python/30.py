"""
30. Question:
Define a class named American which has a static method called printNationality.

Hints: Use @staticmethod decorator to define class static method.
"""


class American(object):
    nation_name = "American"

    @staticmethod
    def printNationality():
        print American.nation_name


person_nation = American()

person_nation.printNationality()
