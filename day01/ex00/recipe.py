class Error(Exception):
   """Base class for other exceptions"""
   pass

class CookingLvlException(Error):
   """Raised when the input value is too small"""
   pass

class CookingTimeException(Error):
   """Raised when the input value is too large"""
   pass

class IngredientsException(Error):
   """Raised when the input value is too large"""
   pass

class RecipeTypeException(Error):
   """Raised when the input value is too large"""
   pass

class Recipe:
    def __init__(self, name: str, cook_lvl: int, cook_time: int, ingredients: tuple, recipeType: str, description:str=""):
        try:
            if cook_lvl <= 0 or cook_lvl > 5:
                raise CookingLvlException
            if cook_time < 0:
                raise CookingTimeException
            for ingr in ingredients:
                if not isinstance(ingr, str):
                    raise IngredientsException()
            if recipeType != "starter" and recipeType != "lunch" and recipeType != "dessert":
                raise RecipeTypeException
        except CookingLvlException:
            print("The cooking level must be between 1 and 5")
            exit(1)
        except CookingTimeException:
            print("The cooking time must be positive")
            exit(1)
        except IngredientsException:
            print("The ingredients must be all strings")
            exit(1)
        except RecipeTypeException:
            print("The recipe type must be starter or lunch or dessert.")
            exit(1)
        else:
            self.name = name
            self.cooking_lvl = cook_lvl
            self.cooking_time = cook_time
            self.ingredients = ingredients
            self.recipe_type = recipeType
            self.description = description

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""

        txt = 'Recipe name: ' + self.name + '\nCooking level: ' + str(self.cooking_lvl) + ' Cooking time: ' + str(self.cooking_time) + ' min\n'
        if len(self.description) > 0:
            txt += 'Recipe description: ' + self.description + '\n'
        txt += 'Recipe type: ' + self.recipe_type + '\nIngredients: '
        ingred = ', '.join(stri for stri in self.ingredients)
        return txt + ingred