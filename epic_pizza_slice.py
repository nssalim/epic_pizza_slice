# Epic Pizza Slice
# Use lists to organize sales data

# Topping List:- To help keep track of the kinds of pizzas sold
toppings = ["pepperoni", 
"pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Price List:- To help keep track of how much each kind of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# Count how many times $2 slices appear in the price list
num_two_dollar_slices = prices.count(2)
print("Number of " + "$2 slices:-  " + str(num_two_dollar_slices))

# Find the length of the toppings list
num_pizzas = len(toppings)
print("Number of toppings!:- " + str(num_pizzas))

# Convert toppings and prices lists into a two-dimensional list
pizza_and_prices = ([2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"])
print("Price list (unordered):- " + str(pizza_and_prices))

# Sort pizzas by price (in ascending order)
print("Price list (ordered/ascending):- " + str(sorted(pizza_and_prices)))

# First element of sorted pizzas (price)
cheapest_pizza = sorted(pizza_and_prices)[0]
print("Cheapest pizza:-  " + str(cheapest_pizza))

# Last element of sorted pizzas (price)
priciest_pizza = sorted(pizza_and_prices)[-1]
print("Priciest pizza :-  " + str(priciest_pizza))

# Remove last element of sorted pizzas (price). One "anchovies" slice available.
pizza_and_prices = sorted(pizza_and_prices)
print("For sale!  Price list has one available anchovies pizza slice left!  " + str(pizza_and_prices))
anchovies_pizza_slice_gone = pizza_and_prices.pop() 
print("Sold! Last anchovies pizza slice taken and no longer available in price list! " + str(pizza_and_prices)) 

# Add new topping to sorted pizzas (price)
pizza_and_prices[4] = ([2.5, "peppers"])
print("New peppers topping added to price list!:-  " + str(pizza_and_prices))

# 3 lowest cost pizzas in Price list
three_cheapest = sorted(pizza_and_prices)[-3:]
print("Price list (3 lowest cost pizzas ):-  " + str(three_cheapest))
