"""
Author: Shannon Kueneke
Date: January 31, 2025
File: Kueneke_lemonadeStand.py
Description: Hands-On 2.1: Functions
"""

#calculate total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
  total_cost = lemons_cost + sugar_cost
  return total_cost

#calculate total profit from selling lemonade, minus expenses
def calculate_profit(lemons_cost, sugar_cost, selling_price):
  total_cost = calculate_cost(lemons_cost, sugar_cost)
  total_profit = selling_price - total_cost
  return total_profit


lemons_cost = 3
sugar_cost = 1
selling_price = 5
cost = "%d + %d = %d." % (lemons_cost, sugar_cost, calculate_cost(lemons_cost, sugar_cost))
profit = "%d - (%d + %d) = %d" % (selling_price, lemons_cost, sugar_cost, calculate_profit(lemons_cost, sugar_cost, selling_price))

#print total cost
print(cost)

#print total profit
print(profit)