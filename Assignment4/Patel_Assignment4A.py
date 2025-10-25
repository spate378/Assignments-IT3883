# Program Name: Assignment4A.py
# Course: IT3883/Section W01
# Student Name: Shiv Patel
# Assignment Number: 4
# Due Date: 10/26/2025
# Purpose: Ask the user to input a string which will then be sent over a socket to program b
# Help received: Module 4 lecture videos Part 1 and 2, Module 4-1 Powerpoint

import socket

# create socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Information about connections
hostIp = "127.0.0.1"
portNum = 45221

# Connect to program b 
try:
    mySocket.connect((hostIp, portNum))
    print("You are now connected to Program B.")

    # Get userinput and send over socket 
    userInput = input("Enter text to send: ")
    mySocket.send(userInput.encode())

    # Get the response from sever
    replyOutput = mySocket.recv(1024).decode()
    print("Program B Reponse: ", replyOutput)
except Exception as e:
    print("Error has occured:", e)

mySocket.close()
print("Program A completed.")
