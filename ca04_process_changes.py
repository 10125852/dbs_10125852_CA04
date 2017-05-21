# -*- coding: utf-8 -*-
"""
CA04 - File processor
author: 10125852 InSun Ahn

"""

# Open the log file to process.
my_file = 'changes_python.log'
# Read all lines and strip whitespaces and trim the line.
data = [line.strip() for line in open(my_file, 'r')]

# Output data as csv file to check index of each element.
import csv
with open("data_output.csv", "wb") as cfile:
    mywriter = csv.writer(cfile)
    mywriter.writerow(data)


# print the number of lines read.
print(len(data))

# Define separater between each commit which is 72 -s.
sep = 72*'-'


# Define fucntion to iterate over the file and aggregate commit details.
def get_commits(data):
    commits = []
    index = 0
    while index < len(data):
        try:
            # Define the positions of commit details - revision number, author name, date and count of comment lines.
            details = data[index + 1].split('|')
            # Define the postion of the rest lines with changed path and comment.
            tails = data[index+2:data.index(sep,index+1)]
            # Cleanse data by remove characters and spaces at the end.
            # Set keys in the commit dictionary except for the changed path.
            commit = {'revision': details[0].strip().strip('r'),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[0],
                'comment': tails[-1]}
            # Append commit dictionaries in list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits


# Execute get_commits function.
commits = get_commits(data)


if __name__ == '__main__':
    print(commits[0])
    print(commits[1]["author"])
    print(commits[2]["date"])
    
    # Check whether the list contains 422 commit objects.
    print len(commits)


# Export commits list in a csv format.
import csv
with open("test_output01.csv", "w") as cfile:
    header = ["revision", "date", "author", "number_of_lines", "comment"]
    mywriter = csv.DictWriter(cfile, fieldnames = header, delimiter=',', lineterminator='\n',)
    # Give a header to the file with set keys.
    mywriter.writeheader()
    # Iterate over the list and add each commit object as a row to the file.
    index = 0
    while index < len(commits):
        mywriter.writerow(commits[index])
        index = index + 1
