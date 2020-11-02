
def sortVeggies():
    veggie_string = raw_input("Veggies to sort: ")

        veggie = veggie_string.split(", ")
        vegetables = []

        for i in veggie:
            #not in order
            j = veggie.index(i)
            #i is not the first element 
            while j>0:
                #not in order
                a = 0
            
                if veggie[j-1] > veggie[j]:
                    #swap
                    veggie[j-1],veggie[j] = veggie[j],veggie[j-1]
                    vegetables.insert(a, veggie.index(veggie[j-1]))
                    a = a + 1
                
                else:
                    #in order
                    break
                j = j - 1

        reverseVeggies = vegetables[::-1]
        string_veggie = [str(int) for int in reverseVeggies]
        final = " ".join(string_veggie)
        print(final) 
        
sortVeggies() 
''''
#This first half with the netcat comes from the NaCTF sample... still need to adapt it

import socket

# Open socket to interact with challenge server
s = socket.socket()

# address = "challenges.ctfd.io", port = 30267
s.connect(("challenges.ctfd.io",30267))

# Receive initial info
info = s.recv(4096).decode("utf-8")
print(info)

# Choose challenge
s.send(b'2\n')
response = s.recv(4096).decode("utf-8")
print(response)

# Get veggies 
veggies = response.split("\n\n")[1].split(', ')
print (veggies)

# Send the robot instructions
s.send('1 2 3\n'.encode('utf-8'))
response = s.recv(4096).decode("utf-8")

print(response)

'''

