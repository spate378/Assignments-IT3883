# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Shiv Patel
# Assignment Number: 3
# Due Date: 10/03/2025
# Purpose: Write a GUI program that converts MPG to Kilometers per Liter
# Resources Used: Module 3-1, 3-2 GUI Powerpoints

import tkinter as tk 

convertRate = 0.425143707   # conversion factor
def convertInput(event):
    userInput = mpgEntry.get()  # Get the user input
    try:
        mpg = float(userInput) # Makes user entered value(MPG) a float
        kml = mpg * convertRate # Multiply to get KM/L
        # Print output
        answer.config(text=str(round(kml, 3)) + " km/l")
    except:
        # Print in case there is no input or invalid
        answer.config(text="---")

# create the main window GUI
mainWindow = tk.Tk()
mainWindow.title(" MPG to KM/L Conversion ")

# Input the MPG
input1 = tk.Label(mainWindow, text="Enter Miles per Gallon:")
input1.grid(row=0, column=0)
mpgEntry = tk.Entry(mainWindow)
mpgEntry.grid(row=0, column=1)

# Output the KML
input2 = tk.Label(mainWindow, text="Kilometers per Liter:")
input2.grid(row=1, column=0)
answer = tk.Label(mainWindow, text="--")
answer.grid(row=1, column=1)

mpgEntry.bind("<KeyRelease>", convertInput)
mainWindow.mainloop()
