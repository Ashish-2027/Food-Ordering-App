from Restaurant import *
rest = Restaurant()
print("Welcome to the food ordering App")
while True:
    role = int(input("Please select the role of the food ordering app \n1. Admin \n2. User \n0. Exit \n"))
    if role == 1 :
        while True:
            admin_input = int(input("Enter Your preferances \n1. Add Food items \n2. Edit Food Items \n3. Remove Food items \n4. Show all Food items \n0. Exit the Application \n"))
            if admin_input == 1:
                rest.add_food_items()
                new_item = int(input("Do you want to add more items \n1. Yes \n2. No\n"))
                if new_item == 1 :
                    rest.add_food_items()
            elif admin_input == 2:
                rest.update_food_item()
            elif admin_input == 3:
                rest.remove_food_items()
            elif admin_input == 4:
                rest.all_food_items()
            elif admin_input == 0:
                print("Exit from Application")
                break
            else:
                print("Invalid Input, Please select from the given options.")
    
    elif role == 2:
        print("Register Your Account \n")
        rest.register()
        print("Please Login to your Account")
        rest.login()
        while True:
            options = int(input("Select from the below options \n1. Place Order \n2.Show Order History \n3. Edit Personal Info \n0. Logout \n"))
            if options == 1:
                rest.place_order()
                add_order = int(input("Do you want to Order more items \n1. Yes \n2. No\n"))
                if add_order == 1:
                    rest.place_order()
            elif options == 2:
                rest.order_history()
            elif options == 3:
                rest.edit_personal_details()
            elif options == 0:
                print("Exit from Application")
                break
            else:
                print("Invalid Input, Please select from the given options.")
    
    elif role == 0:
        print("Thank You")
        break