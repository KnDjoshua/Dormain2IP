import socket
import time
print('Hi There,')
time.sleep(3)
dormain = input("\033[96mEnter Dormain Name To Convert: ")
ip = socket.gethostbyname(dormain)
time.sleep(2)
print (f"\033[80mIP Address Of {dormain} =>=> {ip}")

