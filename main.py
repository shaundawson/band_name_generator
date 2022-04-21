#. Create a greeting for program
print("Welcome to the Band Name Generator.")
# Ask the user for the city that they grew up in.
city = input("Which city did you grow up in? ")
# Ask the user for the name of a pet
pet = input("What's your pet's name? ")
# Combine the name of their city and pet and show them their band name
band_name = city + " " + pet
#Make sure the input cursor shows up on a new line
print("Your band name could be" + " " + band_name)