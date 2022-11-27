class Restaurant:
    def __init__(self):
        self.foods = {}
        self.food_id = len(self.foods) + 1
        self.personal_details = {}
        self.ordered_items = []

    #-----------------Admin------------------------

    def add_food_items(self):
        self.Name = input("Enter the Food item Name: ")
        self.Quantity = int(input("Enter Food Quantity: (plates) "))
        self.Price = int(input("Enter Food Price: "))
        self.Discount = int(input("Enter Discount: (%) "))
        self.Stock = int(input("Enter Stock: "))
        self.item = {"name": self.Name, "Quantity": self.Quantity, "Price": self.Price, "Discount": self.Discount, "Stock": self.Stock}
        self.food_id = len(self.foods) + 1
        self.foods[self.food_id] = self.item
        print(self.foods)
        print("Item Added Successfully")

    def update_food_item(self):
        a = int(input("Enter Food ID of the item you want to edit: "))
        for i in self.foods[a]:
            self.foods[a][i] = input(f"Enter the {i} you want to update : ")  
        print("Food details updated Successfully")
        print(self.foods)

    def remove_food_items(self):
        x = int(input("Enter Food ID of the item you want to delete: "))
        del self.foods[x]
        print("Remaining Items Available: ",self.foods)

    def all_food_items(self):
        print("All the Food items are listed below")
        for i in self.foods:
            print("------------- \nFood ID : ",i,"\n----------")
            for l in self.foods[i]:
                print(l,":",self.foods[i][l])

    # --------------------User---------------------------
    def register(self):
        self.full_name = input("Enter your Full Name:  ")
        self.ph_no = int(input("Enter your Phone Number:  "))
        self.email = input("Enter your Email Address:  ")
        self.address = input("Enter your Address:  ")
        self.username = input("Enter your Username:  ")
        self.password = input("Enter New Password:  ")
        self.user_details = {"Name": self.full_name, "Phone Number": self.ph_no, "Email Address": self.email, "Address": self.address, "Username": self.username, "Password": self.password}
        for i in self.user_details:
            self.personal_details[i] = self.user_details
        print("Congratulations")
        print("You have successfully registered your account")

    def login(self):
        print("Welcome to Login Page")
        while True:
            user_id = input("Enter Username: ")
            password = input("Enter Password: ")
            if user_id == self.username:
                if password == self.password:
                    print("You have logged in Successfully")
                    break
                else:
                    print("Incorrect details, Please Try Again")
            else:
                print("Incorrect details, Please Try Again")

    def place_order(self):
        list_of_foods = [{"Name" :"Tandoori Chicken", "Quantity": "4 pieces", "Price": 240},
                         {"Name" :"Vegan Burger", "Quantity": "1 pieces", "Price": 320},
                         {"Name" :"Truffle Cake", "Quantity": "500gm", "Price": 900}]
        print("Here is the Menu: ")
        for i in list_of_foods:
            print(f"{list_of_foods.index(i)+1} {i['Name']} [{i['Quantity']}] (INR{i['Price']})")
        user_input = int(input("Select the food items you want to order \n1.Tandoori Chicken \n2. Vegan Burger \n3. Truffle Cake \n"))
        if user_input == 1:
            self.ordered_items.append(list_of_foods[0])
            print(list_of_foods[0])
        elif user_input == 2:
            self.ordered_items.append(list_of_foods[1])
            print(list_of_foods[1])
        elif user_input == 3:
            self.ordered_items.append(list_of_foods[2])
            print(list_of_foods[2])
        else:
            print("Choose the item from the Menu")
        
        order = int(input("Do you want to confirm the order \n1. Yes \n2.No \n"))
        if order == 1:
            print("Order placed Successfully")
        else:
            print("Order Cancelled")

    def order_history(self):
        for i in self.ordered_items:
            print("Previous Orders\n",i)

    def edit_personal_details(self):
        for i in self.personal_details:
            self.personal_details[i] = input(f"Enter the {i} you want to update: ")
        print("Personal details updated Successfully\n",self.personal_details)