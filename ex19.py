# ex19.py
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	print "WWwaiiitt what about the drinks!!! :O "

#Study drill addition
def drinks_n_all(bottle_count):
	print "I have about %d bottles of wine. :D" % bottle_count
	print "wow, thats awesome, wine and cheese ha, awesome twosome ;-)"
	print "***And dont forget the Blanket***\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
drinks_n_all(3)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
number_of_bottles = 5

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
drinks_n_all(number_of_bottles)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
drinks_n_all(19*5/5)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
drinks_n_all(number_of_bottles/5 + 2)
# Study Drill
# New function added and calls made to it.