import sys,time,os
import socket
import time
greet = '\033[200mKnDjoshua: Hi There!\n'

for char in greet:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(3)
dormain = input( "\033[96mEnter Dormain Name To Convert: ")
ip = socket.gethostbyname(dormain)
loader = "............\n..................\n"
for char in loader:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(1)
print (f"\033[80mIP Address Of {dormain} =>=> {ip}")
