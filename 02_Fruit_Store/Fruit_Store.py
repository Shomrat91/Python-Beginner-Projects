
# ======================================================
# Fruit Shop System
# Author: Sajjad Ahmed Shomrat
# Description:
# A command-line fruit store where users can buy fruits,
# add items to a cart, and get a final bill.
# ======================================================



# STORE DATA / DATABASE


# Dictionary storing fruit prices
fruit_prices = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "cherry": 15,
    "grape": 12,
    "watermelon": 20,
    "pineapple": 18,
    "mango": 14,
    "jackfruit": 25,
    "peach": 9


}

# Discount percentage if quantity condition is met
discount_percent = 10

# Cart 
# This will store what the user buys
cart = {}



# SHOW AVAILABLE FRUITS


def show_fruits():
   #available fruits and their prices.
    print("\n====== Available Fruits ======")

    for fruit , price in fruit_prices.items():
       print(f"{fruit.capitalize()} : ${price} per unit")
       
    
    
    print("==============================\n")






    # ==============================
# 3️⃣ GET FRUIT FROM USER
# ==============================

def get_fruit():
    """
    Ask the user which fruit they want.
    if fruit not available → give second chance.
    """

    while True:

        # Ask user to enter fruit name
        fruit_name = input("Enter the fruit you want to buy: ").lower()

        # Check if fruit exists in fruit_prices
        if fruit_name in fruit_prices:
            return fruit_name
        else:
        # If fruit NOT available
            print("Sorry, that fruit is not available.")

            print("1. Try another fruit")
            print("2. Exit shop")

        # Ask user for choice
            choice = input("Enter your choice (1 or 2): ")
        
        # if user chooses 1 → continue loop
        if choice == "1":
            continue
        # if user chooses 2 → exit program
        elif choice == "2":
            print("Thank you for visiting the fruit shop. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")




# GET QUANTITY


def get_quantity(fruit):
    """
    ask how many fruits the customer wants.
    Validate that input is a number.
    """
    while True:

        # Ask quantity
        quantity = input(f"How many {fruit}s do you want to buy? ")

        # Check if quantity is a digit
        if quantity.isdigit():
            return int(quantity)
        else:
            print("Please enter a valid number.")




# ADD ITEM TO CART


def add_to_cart(fruit, quantity):
    """
    Adds selected fruit to cart.
    If fruit already exists in cart → increase quantity.
    """

    # TODO:
    # Check if fruit already in cart
    
    if fruit in cart:
        # If yes → increase quantity
        cart[fruit] += quantity
    else:
        # If no → add new fruit
        cart[fruit] = quantity

    

#ASK USER IF THEY WANT MORE


def ask_continue():
    """
    Ask user if they want to buy another fruit.
    """

    # Ask yes/no
    choice = input("Do you want to buy another fruit? (yes/no): ").lower()
    
    # If yes → return True
    if choice == "yes":
        return True
    # If no → return False
    elif choice == "no":
        return False
    else: 
        print("Invalid choice. Please enter yes or no.")
        return ask_continue()  # Ask again if invalid input

        
#CALCULATE BILL


def calculate_bill():
    """
    Calculate total price of all items in cart.
    """

    total = 0

    # Loop through cart items
    for fruit, quantity in cart.items():

    # Get fruit price from fruit_prices
        price = fruit_prices[fruit]
    # Multiply price * quantity
        total += price * quantity
    # Add to total

    return total




# APPLY DISCOUNT

def apply_discount(total):
    """
    Apply discount if total crosses condition.
    """

    # Calculate discount amount
    if total >= 50:
        discount_amount = total * (discount_percent / 100)
        return discount_amount
    else:
        return 0
    


# PRINT FINAL BILL


def print_bill():

    print("\n========== FINAL BILL ==========")

    # Loop through cart
    for fruit, quantity in cart.items():
        # Get fruit price from fruit_prices
        price = fruit_prices[fruit]

        # Print fruit name, quantity and cost
        print(f"{fruit.capitalize()} x {quantity} : ${price * quantity}")

        
    print("--------------------------")


    total = calculate_bill()
    discount = apply_discount(total)


    print(f"Total: ${total}")
    print(f"Discount: ${discount}")
    print("==========================")
    print(f"Final Price: ${total - discount}")



# MAIN SHOP PROGRAM


def main():

    print("Welcome to the Python Fruit Shop 🍎")

    # Show available fruits
    show_fruits()

    while True:


        # Get fruit choice
        fruit = get_fruit()

        # Get quantity
        quantity = get_quantity(fruit)

        # Add to cart
        add_to_cart(fruit, quantity)

        # Ask if user wants to continue
        if not ask_continue():
            break

    # After user finishes shopping
    print_bill()




if __name__ == "__main__":
    main()
