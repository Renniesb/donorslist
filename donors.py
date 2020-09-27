#Rennie Bevineau


#Create the initial array to put the donors in
donors = []

#Establishes a variable to check for to run code only if there are more donars to add to the list
addDonor = "yes"

#this code adds donor arrays to the donors array to create a multidimensional array to account for the donars and the amount they donated
while(addDonor=="yes"):
    donorName = input("type the name of the donor you would like to add to the list")
    donorDonation = input("type the donation amount for this donor")
    donors.append([donorName,donorDonation])
    addDonor = input("Is there another donor you would like to add to the list")


#change the second value in each donor array to a string and double the integer amount
print("all donations will be doubled in the following list")

for d in donors:
    d[1]=str(int(d[1])*2) + " dollar donation"

#Print the donors array
print(donors)




