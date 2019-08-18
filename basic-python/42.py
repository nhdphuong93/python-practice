"""
42. Question:
Write a Python program to read a file line by line and store it into a list
"""
input_file_name = "42.py"

file_stream = open(input_file_name, "r")

result = []
while True:
    line = file_stream.readline()
    if line:
        result.append(line)
    else:
        break

file_stream.close()

print "## ".join(result)
