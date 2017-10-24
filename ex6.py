types_of_people = 10 #this sets the number of people though it also sets up the punchline since 10 is 2 in binary
x = f"there are {types_of_people} types of people."

#the following is setting the variable binary so that it reads "binary"
binary = "binary"
#the following is setting the variable do_not so that it reads the contraction: "don't"
do_not = "don't"
#the following is setting the variable as a function string which inserts two variables, binary and do_not
y = f"Those who know {binary} and those who {do_not}."

#this is printing the variable x
print(x)
#this is printing the variable y
print(y)


print(f"I said: {x}") #since the strings were made into variables, they could be repeated without retyping
print(f"I also said: '{y}'")

#the following variable allows for a word to be inserted in multiple places and can be changed later
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)