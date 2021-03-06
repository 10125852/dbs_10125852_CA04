# -*- coding: utf-8 -*-
"""
CA04 - File processor
author: 10125852 InSun Ahn

"""

# Define function to read a file, to strip whitespaces and trim the line.
def read_file(my_file):
    data = [line.strip() for line in open(my_file, 'r')]
    return data

# Open the log file to process and feed into the function to strip lines.
my_file = 'changes_python.log'
data = read_file(my_file)

# Output data as csv file to check index of each element.
import csv
with open("data_output.csv", "wb") as cfile:
    mywriter = csv.writer(cfile)
    mywriter.writerow(data)

# Define fucntion to iterate over the file and aggregate commit details.
def get_commits(data):
    # Define separater between each commit which is 72 -s.
    sep = 72*'-'
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
                'number_of__comment_lines': details[3].strip().split(' ')[0],
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
    
    # Print the total number of lines in data.
    print len(data)
    
    # Print the number of commit objects the list contains. It should be 422.
    print len(commits)
    
    # Print to see 1st, 2nd and 3rd elements in commits list. 
    # Print only specific keys for 2nd and 3rd elements/dictionaries.
    print(commits[0])
    print(commits[1]["author"])
    print(commits[2]["date"])
  

# Export commits list in a csv format.
import csv
with open("commits.csv", "w") as cfile:
    header = ["revision", "date", "author", "number_of__comment_lines", "comment"]
    mywriter = csv.DictWriter(cfile, fieldnames = header, delimiter=',', lineterminator='\n',)
    # Give a header to the file with set keys.
    mywriter.writeheader()
    # Iterate over the list and add each commit object as a row to the file.
    index = 0
    while index < len(commits):
        mywriter.writerow(commits[index])
        index = index + 1
