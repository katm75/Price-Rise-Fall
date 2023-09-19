# This is exercise 3 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md
    # Modified to change "Bitcoin" to "Stock"

# Kathryn Marks
# kathryn.pythonprograms@gmail.com
# Created September 18, 2023
# Last modified September 18, 2023

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

from functools import total_ordering


print ("This is a program to calculate the change in price of your stock")
print ("")

price = int(input("Please type in the purchase price of your stock: ")) 
print ("You bought stock for : ", price)

price_change = int(input("Please type the percentage change of your stock:"))
print ("Your stock changed by ", price_change)

# calculation code goes here

print ("The new value of your stock is", total_value)