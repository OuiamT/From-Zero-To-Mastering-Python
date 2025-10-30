"""
This script allows users to create and display a simple recipe.

Users can input a recipe name, ingredients, cooking time, and instructions.
After entering the information, the program waits a few seconds and then
displays the complete recipe details in a formatted output.
"""

import time


class Recipe:
    """A class to represent a cooking recipe with its details."""

    def __init__(self, name, ingredients, time_cooking, instruction):
        """
        Initialize a Recipe object.

        Parameters:
            name (str): The name of the recipe.
            ingredients (str): Ingredients required for the recipe.
            time_cooking (str): Time needed to cook the recipe.
            instruction (str): Steps or instructions for preparing the recipe.
        """
        self.name = name
        self.ingredients = ingredients
        self.time_cooking = time_cooking
        self.instruction = instruction

    def display_info(self):
        """
        Return a formatted string with recipe details.

        Returns:
            str: Formatted recipe information (name, ingredients, time, and instruction).
        """
        return f"""
Name: {self.name}
Ingredients: {self.ingredients}
Cooking time: {self.time_cooking}
Instruction: {self.instruction}
---------------------------------
"""


def put_information():
    """
    Prompt the user to enter recipe details and create a Recipe object.

    Returns:
        Recipe: A Recipe instance containing the user's input.
    """
    name = input("Enter recipe name:  ").capitalize()
    ingredients = input("Enter ingredients (comma separated):  ").title()
    time_cooking = input("Enter cooking time:  ").capitalize()
    instruction = input("Enter cooking instruction:  ")
    print("Recipe added successfully!")
    return Recipe(name, ingredients, time_cooking, instruction)


print("----- Welcome to Recipe Collection -----\n")
my_recipe = put_information()
time.sleep(3)
print("\nDisplaying recipe ....")
print(my_recipe.display_info())
