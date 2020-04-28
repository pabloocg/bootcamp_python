import sys

def BuyCookbook():
    cookbook = {    'sandwich': {   'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                                    'meal': 'lunch',
                                    'prep_time': 10
                    },
                    'cake': {   'ingredients': ['flour', 'sugar', 'eggs'],
                                'meal': 'dessert',
                                'prep_time': 60
                    },
                    'salad': {
                                'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                                'meal': 'lunch',
                                'prep_time': 15
                    }
    }
    return cookbook

def printOnlyKeys(cookbook):
    print(f"{cookbook.keys()}")

def printOnlyValues(cookbook):
    print(f"{cookbook.values()}")

def printAllItems(cookbook):
    print(f"{cookbook.items()}")

def printRecipe(cookbook, recipe):
    try:
        print(f"\nRecipe for {recipe}:")
        print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
        print(f"To be eaten for {cookbook[recipe]['meal']}.")
        print(f"Take {cookbook[recipe]['prep_time']} minutes of cooking.")
    except KeyError:
        print("This recipe doesn't exists sorry", file=sys.stderr)

def printCookbook(cookbook):
    for recipe in cookbook:
        printRecipe(cookbook, recipe)
        print()

def delRecipe(cookbook, recipe):
    try:
        del cookbook[recipe]
    except KeyError:
        print("This recipe doesn't exists sorry", file=sys.stderr)

def addRecipe(cookbook, nameRecipe, ingredients, meal, prep_time):
    cookbook[nameRecipe] = {}
    cookbook[nameRecipe]['ingredients'] = ingredients
    cookbook[nameRecipe]['meal'] = meal
    cookbook[nameRecipe]['prep_time'] = prep_time

def questionsToAddRecipe(cookbook):
    recipeName = input("Please enter the recipe's name: ")
    recipeIngredients = input("Please enter the recipe's ingredients separated by commas: ").split(',')
    recipeMeal = input("Please enter the recipe's meal: ")
    recipePrep_time = int(input("Please enter the preparation time to the recipe: "))
    addRecipe(cookbook, recipeName, recipeIngredients, recipeMeal, recipePrep_time)

def questionToDelRecipe(cookbook):
    printOnlyKeys(cookbook)
    recipeName = input("Please enter the recipe's name to delete: ")
    delRecipe(cookbook, recipeName)

def questionPrintRecipe(cookbook):
    printOnlyKeys(cookbook)
    recipeName = input("Please enter the recipe's name: ")
    printRecipe(cookbook, recipeName)

def Options():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

def main():
    cookbook = BuyCookbook()
    while True:
        Options()
        try:
            inputUser = int(input(">> "))
        except ValueError:
            print("\nThis option does not exist, please type the corresponding number.\n")
        except (KeyboardInterrupt, EOFError):
            sys.exit(1)
        else:
            print("\n")
            if inputUser == 1:
                questionsToAddRecipe(cookbook)
            elif inputUser == 2:
                questionToDelRecipe(cookbook)
            elif inputUser == 3:
                questionPrintRecipe(cookbook)
            elif inputUser == 4:
                printCookbook(cookbook)
            elif inputUser == 5:
                break
            print("\n")

if __name__ == "__main__":
    main()
