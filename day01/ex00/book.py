from datetime import date
from recipe import Recipe

class Error(Exception):
   """Base class for other exceptions"""
   pass

class RecipeException(Error):
   """Raised when the input value is too small"""
   pass

class Book:
    def __init__(self, name: str):
        self.name = name
        self.creation_date = date.today()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name:str) -> Recipe:
        """Print a recipe with the name `name` and return the instance"""
        for value in self.recipes_list.values():
            for recipe in value:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print(f"The {name} recipe doesn't exists")
        return None

    def get_recipes_by_types(self, recipe_type:str) -> list:
        """Get all recipe names for a given recipe_type """
        for key in self.recipes_list:
            if key == recipe_type:
                return self.recipes_list[key]
        print(f"The {recipe_type} recipe type doesn't exists")
        return None

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        try:
            if not isinstance(recipe, Recipe):
                raise RecipeException
        except RecipeException:
            print("The type must be a Recipe object")
            exit(1)
        else:
            self.last_update = date.today()
            self.recipes_list[recipe.recipe_type].append(recipe)
