class Pizza:

    def __init__(self):
        self.size = ""
        self.crust_type = ""
        self.toppings = list()

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        topping_list = " and ".join(self.toppings)
        return print(f'I would like a {self.size} inch pizza with {self.crust_type}, topped with {topping_list}')

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust_type = "stuffed crust"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

supreme = Pizza()
supreme.size = 12
supreme.crust_type = "stuffed crust"
supreme.add_topping("Lettuce")
supreme.add_topping("Squash")
supreme.print_order()