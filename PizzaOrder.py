# Pizza menu and price of each stored here
pizza_menu = {
    "Cheese": 10.00,
    "Pepperoni": 12.50,
    "Vegetarian": 11.50,
    "Hawaiian": 13.00,
}

#Display the pizza menu to the user
def display_menu():
  print("\n****Pizza Menu****")
  for pizza, price in pizza_menu.items():
    print(f"{pizza}: ${price:.2f}")
  print("\n======================\n")

#Function to take an order from the user
def take_order():
  order = {}
  #Loop to ask user for pizzas until they enter 'finish' to exit
  while True:
    pizza_name = input("Enter the pizza name (enter 'finish' to checkout): ")
    if pizza_name.lower() == 'finish':
      break
    #Check to make sure the user entry is valid
    if pizza_name not in pizza_menu:
      print("Invalid pizza name. Please choose from the menu.")
      continue
    #User entry for the quantity of the pizza they want
    quantity = int(input("Enter the quantity: "))
    #Check to make sure the user enters a quantity of at least 1
    if quantity <= 0:
      print("Invalid quantity. Please enter a positive number.")
      continue
    #Count the number of pizzas the user entered
    if pizza_name in order:
      order[pizza_name] += quantity
    else:
      order[pizza_name] = quantity
  return order

#Function to calculate the total of the order
def calculate_total(order):
  total = 0
  for pizza, quantity in order.items():
    if pizza in pizza_menu:
      #Price calculation used from pizza_menu dictionary
      price = pizza_menu[pizza]
      total += price * quantity
  return total


def main():
  print("Welcome to the Pizza Restaurant POS!")
  display_menu()
  order = take_order()

  #Statement for when the user checks out without an order
  if not order:
    print("No order taken. Goodbye!")
    return

  #Calculation for total cost of the order
  total_cost = calculate_total(order)
  print("\n****Summary Of Order****")
  #Print out order summary to user
  for pizza, quantity in order.items():
    print(
        f"{pizza}: {quantity} x ${pizza_menu[pizza]:.2f} = ${pizza_menu[pizza] * quantity:.2f}"
    )
  print("\n****Total****")
  print(f"Total: ${total_cost:.2f}")
  print("Thank you for your order. Enjoy your pizza!")


if __name__ == "__main__":
  main()
