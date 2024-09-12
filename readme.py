#CONCEPT USED : 
# Method we used to implement the project is "HALF-DUPLEX"

#ABOUT TEAM AND PROJECT :
# This is a project from Rithvik S and Shameer K , based on the "Crypto" currency which tells the coin name and the current change in percentage
# in its value using an API as per user wish ,which is like a API and refreshes automatically after a certain period if time 

# PACKAGES USED :
# socket   : for communication between client and server , where cliets's request is satisfied by server
# requests : to fetch the API and decode it for our purpose (pip install requests)
# json     : used for proper usage of API's data in our program for necessary output and program readable language    
# termcolor : for customize the output and for better user interface (pip install termcolor)

# DESCRIPTION :
# At first we created socket and then we bind server and client , after binding server get request form the client . Now server runs and fetch the 
# API and makes it in necceary formate . After Every input server checks the given data got from the client is "STOP" if so the conncetion between the 
# server and client ends , else runs the neccesary works on the server by checking the user given data is present in API(collection if crypto coins' details) 
# if so prints the coins' name and it's precentage change in its value time to time and sends found message to client so client can send request for new one. 
# if no coin can be found by the given data from the client then server sends no-match so client sends corrected request . Also we can send "N" number of 
# requeusts until we say "STOP". If the needed coin is an invalid one then it says "Enter correct request" and works if we send the correct one . Also this
# prints whether user can buy this coin or not after the percantge change of its value also the sane for selling the coin .