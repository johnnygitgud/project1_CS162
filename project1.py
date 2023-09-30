# Author: Elvis Ardon
# GitHub username: johnnygitgud
# Date: 09/29/2023
#Description: This program will emulate a Fast Food restaurant.

class BuildaBurger:
  def __init__(self, name):
    self._name = name
    self._ingredients = [] #starting with an empty list of ingredients

  def add_ingredient(self, ingredient_name):
    self._ingredients.append(ingredient_name)

  def remove_ingredient(self, ingredient_name):
    print("Removing ingredient", ingredient_name)
    self._ingredients.remove(ingredient_name)

  def print_ingredients(self):
    print("Your burger has:")
    print(self._ingredients)

user_input = ''

while user_input != 'y':
  print("Welcome to Build A Burger would you like to Build your own Burger today?")
  user_input = input("Type y for yes or n for no: ")

  if user_input == "y":
      burger = BuildaBurger("Your Burger") #create an object
      bun_input = input("Would you like a bun? y or n: ")
      if bun_input != 'n':
        burger.add_ingredient("Bun") #add an ingredient
      lettuce_input = input("Would you like lettuce? y or n: ")
      if lettuce_input != 'n':
        burger.add_ingredient("Lettuce")
      tomato_input = input("Would you like to add tomatoes? y or n: ")
      if tomato_input != 'n':
        burger.add_ingredient("Tomatoes")
      cheese_input = input("Would you like to add cheese? y or n: ")
      if cheese_input != 'n':
        burger.add_ingredient("Cheese")
      patty_input = input("Would you like to add a burger patty? y or n: ")
      if patty_input != 'n':
        burger.add_ingredient("Burger Patty")      
      #bhel_recipe.remove_ingredient("Salt") #remove an ingredient
      burger.print_ingredients() #print the list of ingredients so far
  elif user_input == "n":
    print("Thank you have a great day")
  else:
      print("Please type y for yes or n for no")