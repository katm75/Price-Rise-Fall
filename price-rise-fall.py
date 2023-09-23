# This is exercise 3 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md
    # Modified to change "Bitcoin" to "Stock"

# Kathryn Marks
# kathryn.pythonprograms@gmail.com
# Created September 18, 2023
# Last modified September 22, 2023

# #You've bought some stock and now the price is on the rise

# Create a program that:

# Reads the value of the stock at the time of purchase
# Reads the percentage of increase (or decrease)
# Prints the total value of your stock
# Prints the increase or decrease value

# Example: bitcoin_value = 10000, bitcoin_increase = 10
# Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000

# Define the variables
    # price = the current price of the stock
    # price_change = the increase or decrease of the stock
    # total_value = the new value of the stock
    # percent_change = the percentage change in decimal form


print ("This is a program to calculate the change in price of your stock")
print ("")

price = float(input("Please type in the purchase price of your stock in dollars: ")) 
print ("You bought stock for : ", + str.format(price) + "dollars")
    # this doesn't work.  i don't know why.  
    # so i guess i'll format it in its own line and then do the print

price_change = float(input("Please type the percentage change of your stock:"))
print ("Your stock changed by ", + price_change + "percent")

# change the percent to a decimal for caluclation

percent_change = price_change/100

# there is something wrong because when you run the program with 1% change, it outputs 200

# total_value = price + price * price_change
    #this works, but price_change is as a percent and it needs to be changed to a decimal.  
    #This needs a new variable and calulation.

total_value = price + price * percent_change

print ("")
print ("The new value of your stock is ", + total_value + "dollars")