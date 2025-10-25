# Program Name: Assignment4B.py
# Course: IT3883/Section W01
# Student Name: Shiv Patel
# Assignment Number: 4
# Due Date: 10/26/2025
# Purpose: Get the string from Program A and convert to uppercase and send back
# Help received: Module 4 lecture videos Part 1 and 2, Module 4-1 Powerpoint

import socket

# create socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Information about connections, same from program A
hostIp = "127.0.0.1"
portNum = 45221

mySocket.bind((hostIp, portNum))
mySocket.listen(1)
print("The Program is waiting for message: ")
connection, clientAddress = mySocket.accept()
print("Connected at: ", clientAddress)

# Get message from Program A
userData = connection.recv(1024).decode()
print("User Input has been received: ", userData)

# convert everything to uppercase and send back
uppercaseInput = userData.upper()
connection.send(uppercaseInput .encode())


connection.close()
mySocket.close()
print("Program B Completed.")
