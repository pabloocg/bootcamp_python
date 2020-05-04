from book import Book
from recipe import Recipe

def main():
    buyBook = Book("The Book Master")
    tourte = Recipe("Pizza", 3, 60, ("Tomatoes", "Mass", "Cheese"), "lunch", "The pizza is the best")
    buyBook.add_recipe(tourte)
    tourte = Recipe("Coffee", 1, 20, ("Coffe Capsule", "Milk"), "starter", "The coffee wake up all the body")
    buyBook.add_recipe(tourte)
    tourte = Recipe("Cookies", 2, 40, ("Mass", "Milk", "Chocolat"), "starter", "Cookies Mastaaaaaaaaa")
    buyBook.add_recipe(tourte)
    recipe_rec = buyBook.get_recipe_by_name("Pizza")
    recipe_rec1 = buyBook.get_recipe_by_name("Pasta")
    recipe_starter = buyBook.get_recipes_by_types("starter")
    for recipe in recipe_starter:
        print(str(recipe))
    buyBook.add_recipe(3)

if __name__ == "__main__":
    main()
