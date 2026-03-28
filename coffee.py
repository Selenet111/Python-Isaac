class CoffeeMachine():
    pass #a block code without anything in it will return an error, use pass
    def __init__(self, water, milk, coffee): #creating attributes
        self.menu = {"espresso":[50, 0, 18, 1.5], "latte":[200, 150, 24, 2.5], "cappucino":[250, 100, 24, 3.0]}
        self.resources = {"milk":milk, "water":water, "coffee":coffee}
        self.nCoffeesMade = 0
        self.money = 0
        self.coffeesMadeByType = {"espresso":0, "latte":0, "cappucino":0}

    def __repr__(self):
        return f"This coffee machine can make the following coffees: {list(self.menu.keys())}\nThere is ${self.money} available."
        

    def checkIngredients(self, drink):
        drink = drink.lower()
        if drink not in self.menu.keys():
            print("Sorry, the drink you requested is not available.")
            return False
    
        recipe = self.menu[drink]
        if recipe[0] > self.resources["water"]:
            print("Not enough ingredients")
            return False
        if recipe[1] > self.resources["milk"]:
            print("Not enough ingredients")
            return False
        if recipe[2] > self.resources["coffee"]:
            print("Not enough ingredients")
            return False
        return recipe
    
    def makeDrink(self, drink):
        recipe = self.checkIngredients(drink)
        if recipe == False:
            return
        
        self.resources["water"] -= recipe[0]
        self.resources["milk"] -= recipe[1]
        self.resources["coffee"] -= recipe[2]
        self.money += recipe[3]
        self.nCoffeesMade += 1
        self.coffeesMadeByType[drink.lower()] += 1
        print(f"{drink.title()} was made successfully. Enjoy your coffee!")

    



thoCoffee = CoffeeMachine(1000, 1000, 100)
rmhCoffee = CoffeeMachine(5000, 5000, 250)
ylcCoffee = CoffeeMachine(250, 250, 100)

thoCoffee.makeDrink("espresso")
thoCoffee.makeDrink("americano")
thoCoffee.makeDrink("Cappucino")
print(thoCoffee.resources)
print(thoCoffee)