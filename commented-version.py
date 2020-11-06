def sortVeggies():
    veggie_string = raw_input("Veggies to sort: ")
    #first we need to get the input from the user
    #using raw_input allows us to just use something like 
    # I like pizza instead of "I like pizza"
    if veggie_string != "quit":
        veggie = veggie_string.split(", ") 
        # since we're getting multiple veggie names, each separated by a comma, we can split the string based on that and organize it in an array (I'm calling it veggie cuz why not)
        vegetables = [] #this empty array is for the indices, it's not going to be used yet

        for i in veggie: # so we're going to loop through the array veggie
            #  currently veggie is not organized
            j = veggie.index(i) 
            #i is not the first element 
            while j>0:
                # while it's still not in order, we're going to want to go through this loop
                a = 0
                # a is going to be our counter 
            
                if veggie[j-1] > veggie[j]:
                    # this is where we swap the veggies!!
                    veggie[j-1],veggie[j] = veggie[j],veggie[j-1]
                    #here the veggies get swapped. So the veggie at j is swapped with the veggie at index j-1, so the one right before it
                    vegetables.insert(a, veggie.index(veggie[j-1])) # remember the empty array we initialized outside of the for loop? Well this is where we use it!!
                    # the first line of the if statement swaps the veggies, but we don't get any instructions for the indices we need to swap
                    # that's why we have this line! vegetables.insert(a, veggie.index(veggie[j-1])) 
                    # veggie.index gives us the index of an element in an array. So for example, if veggie[j] was "tomatoes" and was the second element in the array, using veggie[j] would give us "tomatoes". 
                    # veggie.index("tomatoes") would give us the index of "tomatoes" in the array called veggies
                    a = a + 1 # we're incrementing a so it doesn't index at the exact same place
                
                else:
                    #in order
                    break
                j = j - 1 
                # at this point we finished sorting!

        reverseVeggies = vegetables[::-1]
        # for some reason inserting the veggies into the empty array gives us the order in reverse, 
        # however that's probably because I wasn't paying too close attention to how the insert works lol
        # I also didn't feel like fixing that part when reversing an array is really easy
        string_veggie = [str(int) for int in reverseVeggies]
        final = " ".join(string_veggie)
        # We're turning the indices in the array reverseVeggies (remember this one is in the correct order) into a string
        # if we were to get this to work with netcat, it'd have to be in this form, each step separated by a space
        print(final) 

        sortVeggies() # This will continue running the function until our if statement is false
    
    elif veggie_string == "quit": # this will make the program stop running (since the if statement is no longer true)
        print("Have a good day!")
        
sortVeggies() # This way our function runs when we run it

''''
#This part comes from the NaCTF sample... still need to get my function to work with it

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

