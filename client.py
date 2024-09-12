import socket
from termcolor import colored

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("127.0.0.1",8000))  
while True :
    data = input("Enter Coin name for info : ")
    data2 = data.capitalize()
    # print(data)
    s.sendto(str.encode(data2),("127.0.0.1",8000))
    if data.lower() == "stop":
        break
    dat,addr = s.recvfrom(1024)
    dat1 = dat.decode()
    flag=0
    if dat1 >= "0" and flag == 0 and dat1 != 'no-match':
        flag=1
        dat1 = colored(dat1,'green')
        print("\nPercentage change : ",dat1,"% (",data2,")\n")
        print("Data found successfully on server You can buy this coin after decrease of it value If you already hold this coin you can sell this now\n")
    if dat1 != "no-match" and flag == 0:
        dat1 = colored(dat1,'red')
        print("\nPercentage change : ",dat1,"% (",data2,")\n")
        print("Data found successfully on server You can buy this coin If you already hold this coin you can sell this after prices increase in its value\n")
    if dat1 == "no-match":
        dat1 = colored(dat1,'magenta')
        data = colored(data,'cyan')
        print("'",dat1,"' says that '",data,"' is not a coin enter correct request for coin ")