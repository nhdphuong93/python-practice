"""
31. Question:
Define a class named American and its subclass NewYorker.
"""


class American(object):
    nation = "American"

    @staticmethod
    def print_nationality():
        print American.nation


class NewYorker(American):
    state = "NewYork"

    @staticmethod
    def print_state():
        print NewYorker.state


person = NewYorker()

person.print_nationality()
person.print_state()
