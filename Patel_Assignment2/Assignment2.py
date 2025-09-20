# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Shiv Patel
# Assignment Number: Assignment2
# Due Date: 09/19/2025
# Purpose: Write a program that calculates the final averages for group of students and show the results in a descending order by the grade value
# Resources: Module 2-1, Module 2-2 Slides, Lecture Videos

def read_file(fileName):
    # Read the lines in the list
    with open(fileName, "r") as inFile:
        fileLines = inFile.readlines()
    return fileLines

def calculate_average(sGrades):
    total = 0
    for numGrade in sGrades:
        total += numGrade # add all the scores on the list
    return total / len(sGrades) # take the total and divide by total number of scores

def main():
    # Read all lines from the input file
    studentLines = read_file("Assignment2input.txt")
    studentResults = []

    # Process the lines in the data
    for line in studentLines: 
        fields = line.strip().split() 
        studentName = fields[0]

        # String to integer
        studentGrades = []
        for num in fields[1:]:
            studentGrades.append(int(num))

        avgGrade = calculate_average(studentGrades) # Find the avg grade
        studentResults.append((studentName, avgGrade)) # Add name of the student and avg

    # Sort from highest to lowest grade
    studentResults.sort(key=lambda x: x[1], reverse=True)

    # Print the results
    for student, average in studentResults: print(student, format(average, ".2f"))
main()