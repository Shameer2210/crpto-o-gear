import socket
import requests
import json
from termcolor import colored

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",8000))
print("Socket created and waiting for request from client ")
while True :
    data,addr = s.recvfrom(1024)
    data = data.decode()
    if data.lower() == "stop":
        break
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=2000&page=1&sparkline=false')
    print("\nAPI status code : ",response.status_code,"\n")
    print("Requested data from the user : \n")
    obj = response.text 
    parse_json = json.loads(obj)
    length = int(len(parse_json))
    flag = 0
    for i in range(0,length):
        id = parse_json[i]['id']
        name = parse_json[i]['name']
        col = parse_json[i]['price_change_percentage_24h']
        last = parse_json[i]['last_updated']
        vol = parse_json[i]['total_volume']
        # print(id,name)
        if id.lower() == data.lower() or name == data:
            print("Data found  ")
            if col < 0:
                text = colored(col,'red')
                print(name,':',text,'%')
                print("Last modified : ",last,"\nTotal volume :",vol)
                flag=1
                break
            else:
                text = colored(col,'green')
                print(name,':',text,'%')
                print("Last modified : ",last,"\nTotal volume :",vol)
                flag=1
                break
    change = str(col)
    if flag == 1:
        print("\nSend response : Send a request for another coin ")
        s.sendto(str.encode(change),addr)
    else:
        print("No data found as given coin name is not a specified one , send correct request ")
        s.sendto(str.encode("no-match"),addr)
    
