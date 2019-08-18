"""
44. Question:
Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be
close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
"""
BRACKETS = {
    "[" : "]",
    "{" : "}",
    "(" : ")"
}


def is_valid(string_to_check):
    list_brackets = []
    for bracket in string_to_check:
        if bracket in BRACKETS:
            list_brackets.append(BRACKETS[bracket])
        elif not list_brackets or list_brackets.pop() != bracket:
            return False
    return not list_brackets


print is_valid("}{")
print is_valid("()")
print is_valid("[)")
print is_valid("({[)]")
print is_valid("{{{")
