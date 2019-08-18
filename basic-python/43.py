"""
43. Question:
Write a Python program to combine each line from first file with the corresponding line in second file
"""


def read_file_to_list(file_name):
    file_stream = open(file_name, "r")

    result = []
    while True:
        line = file_stream.readline()
        if line:
            result.append(line)
        else:
            break
    file_stream.close()
    return result


list_file_one = read_file_to_list("42.py")
list_file_two = read_file_to_list("43.py")

print "##".join([file1 + file2 for file1, file2 in zip(list_file_one, list_file_two)])
