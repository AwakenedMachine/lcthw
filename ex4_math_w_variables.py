cars = 100
#this is the number of people per car
space_in_a_car = 4.0
#this is how many people we can put in a car
passengers = 90
#this is how many limp dicks don't have their driver's licenses
drivers = 30
#this is how many people actually got up early enough to go to driver's ed
cars_not_driven = cars - drivers
#this is the lost capacity for carrying people due to the limp dicks without DL's
cars_driven = drivers
#this is all we're left with for transportation capability
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")