# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Shiv Patel
# Assignment Number: 5
# Due Date: 11/16/2025
# Purpose: Write a Python program to create and interact with a database. Show averages for Sundays and Thursdays
# Resources Used: Module 5-1, 5-2 Software Engineering Powerpoints, Lecture Video 11_11

import sqlite3

# Create a database (db)
connectionDb = sqlite3.connect("Temperatures.db")
cursorTemp = connectionDb.cursor()

# Make tables for database
cursorTemp.execute("CREATE TABLE IF NOT EXISTS DailyTemperature(" "ID INTEGER PRIMARY KEY AUTOINCREMENT, ""Day_Of_Week TEXT, ""Temperature_Value REAL)")

# Read and input assignment5input txt file
txt5File = "Assignment5input.txt"
with open(txt5File, "r") as file:
    for line in file:
        parts = line.strip().split()

        # Weekday and Tempreture variables
        weekdayName = parts[0]
        tempNum = float(parts[1])

        # Put values in the database
        cursorTemp.execute(""" INSERT INTO DailyTemperature (Day_Of_Week, Temperature_Value) VALUES (?, ?) """,
        (weekdayName, tempNum))
        
connectionDb.commit()

# Average Sunday
cursorTemp.execute(""" SELECT AVG(Temperature_Value) FROM DailyTemperature WHERE Day_Of_Week = 'Sunday' """)
sundayTemp = cursorTemp.fetchone()[0]

# Average Thursday
cursorTemp.execute(""" SELECT AVG(Temperature_Value) FROM DailyTemperature WHERE Day_Of_Week = 'Thursday' """)
thursdayTemp = cursorTemp.fetchone()[0]

# print results
print("Sunday's Average Temperature: ", round(sundayTemp, 2))
print("Thursday's Average Temperature: ", round(thursdayTemp, 2))

connectionDb.close()
