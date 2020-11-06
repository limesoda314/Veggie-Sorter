def sortVeggies():
    veggie_string = raw_input("Veggies to sort: ")

    if veggie_string != "quit":

        veggie = veggie_string.split(", ")
        vegetables = []

        for i in veggie:
            j = veggie.index(i)

            while j>0:
                a = 0
            
                if veggie[j-1] > veggie[j]:
                    #swap
                    veggie[j-1],veggie[j] = veggie[j],veggie[j-1]
                    vegetables.insert(a, veggie.index(veggie[j-1]))
                    a = a + 1
                
                else:
                    break
                j = j - 1

        reverseVeggies = vegetables[::-1]
        string_veggie = [str(int) for int in reverseVeggies]
        final = " ".join(string_veggie)
        print(final) 

        sortVeggies()

    elif veggie_string == "quit": 
        print("Have a good day!")
        
sortVeggies() 

