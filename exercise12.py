def PizzaMaker(num_pizzas):
    all_pizzas = {}
    for i in range(1, num_pizzas+1):
        print("How many toppings for pizza {}?".format(i))
        num_toppings = int(input())
        all_pizzas
        print("You have ordered a pizza with {} topping(s).".format(num_toppings))
        all_pizzas["pizza {}".format(i)] = num_toppings
    return all_pizzas

def display_full_order(pizzas):
    for pizza_name, num_toppings in pizzas.items():
        print("{}: {} toppings".format(pizza_name, num_toppings))

print("How many pizzas do you want to order?")
number_of_pizzas = int(input())
ordered_pizzas = PizzaMaker(number_of_pizzas)
print()
print("Here's your full order:")
display_full_order(ordered_pizzas)
