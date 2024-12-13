#import product.py which contains the main class for creation of products
from product import *

print("Welcome Admin!")
inventory = {}

while True:
    #Prompt User Input
    print()
    print("Press 1 to view Invetory, Press 2 to create new Inventory, Press 3 to delete Inventory, Press 4 to update Inventory., Press 5 to search Inventory, Press 6 to update Transactions, Press 7 to calculate Sales (0 to exit program)")
    option = int(input("Enter your choice: "))
    if option == 0:
        print("Have a Good Day!")
        break
    if option == 1:
        print()
        print("Viewing Inventory.....")
        if len(inventory) == 0: #Checking if Inventory is empty
            print("Inventory is empty!")
        else:
            print("Inventory:") 
            for name, product in inventory.items(): #Looping through Inventory keys and Printing
                print(f"Name: {name}, Import Price: ₹{product.get("import_price")}, Export Price: ₹{product.get("export_price")}, Stock: {product.get("stock")}, Shipped: {product.get("shipped")}")
        print()
        continue

    if option == 2:
        print()
        print("Creating new Inventory.....")
        while True:
            name = input("Enter inventory name (or exit to quit): ")
            if name.lower() == "exit": #Break Loop
                break
            ip = int(input("Enter import price: "))
            ep = int(input("Enter export price: "))
            stock = int(input("Enter stock: "))
            
            obj = Product(ip, ep, stock) #Instantiate Sub Values for Inventory Product
            
            inventory[name] = obj #Add to main inventory dictionary
            print()
            print("Inventory created successfully!",)
            print()
        continue
    
    if option == 3:
        print()
        print("Deleting Inventory.....")
        name = input("Enter inventory name to delete (or exit to quit): ")
        if name.lower() == "exit":
            break
        if name in inventory: #Looping Through keys of inventory to find desried key and delete it
            del inventory[name]
            print("Inventory deleted successfully!",)
            print()
        else:
            print("Inventory not found!")
            print()
        continue
    
    if option == 4:
        print()
        print("Updating Inventory.....")
        name = input("Enter inventory name to update (or exit to quit): ")
        if name.lower() == "exit":
            break
        if name in inventory: #Looping Through keys of inventory to find desried key and according to user input update values
            ip = int(input("Enter new import price (or leave unchanged by entering 0): "))
            ep = int(input("Enter new export price (or leave unchanged by entering 0): "))
            
            if ip!= 0:
                inventory[name].update("import_price", ip)
            
            if ep!= 0:
                inventory[name].update("export_price", ep)
            
            print("Inventory updated successfully!",)
            print()
        else:
            print("Inventory not found!")
            print()
        continue
    
    if option == 5:
        print()
        print("Searching Inventory.....") 
        name = input("Enter inventory name to be searched: ")
        if name in inventory: #Checking if key exists and printing if it does.
            print("Inventory found!")
            print(f"Name: {name}, Import Price: ₹{product.get("import_price")}, Export Price: ₹{product.get("export_price")}, Stock: {product.get("stock")}, Shipped: {product.get("shipped")}")
        else:
            print("Inventory not found!")
        print()
    
    if option == 6:
        print()
        print("Updating Transactions.....")
        while(True):
            name = input("Enter inventory name to be updated(exit to quit): ")
            if name.lower() == "exit":
                break
            if name in inventory: #Finding product to update transactions on
                print(f"Name: {name}, Import Price: ₹{product.get("import_price")}, Export Price: ₹{product.get("export_price")}, Stock: {product.get("stock")}, Shipped: {product.get("shipped")}")
                while(True):
                    #Prompting User for input to update transactions
                    c = int(input("Enter 1 to update Imported Inventory, 2 to update Shipped Inventory, 3 to Exit: "))
                    print()
                    if(c == 3):
                        break
                    elif c == 1: 
                        val = int(input("Enter number of items Imported: "))
                        inventory[name].update("stock", product.get("stock") + val) #Update Stock
                    elif c == 2:
                        val = int(input("Enter number of items Shipped: "))
                        if inventory[name].update("stock", product.get("stock") - val >= 0): #Making sure shipped units are not greater than the stock
                            #Updating Values
                            inventory[name].update("shipped", product.get("shipped") + val)
                            inventory[name].update("stock", product.get("stock") - val)
                            print("Inventory updated successfully!")
                        else:
                            print("Not enough stock!")
                            print("Inventory not Updated!")
                    else:
                        print("Invalid option!")
                        print()
                        continue
            else:
                print("Inventory not found!")
                print()
    if option == 7:
        print()
        print("Calculating Sales.....") 
        #Initializing sale variables
        tot_sell = 0
        net_profit = 0
        tot_inv = 0
        for name, product in inventory.items():
            tot_inv += product.get("shipped") * (product.get("export_price")) #Finding Total Sales
            net_profit += tot_sell - product.get("shipped") * product.get("import_price") #Finding Net Profit
            tot_inv += product.get("stock") * product.get("import_price") #Finding Valuation of remaining stock
        print(f"Total Sales: ₹{tot_sell}")
        print(f"Total Profit: ₹{net_profit}")
        print(f"Total Inventory Left: ₹{tot_inv}")
        print()
                   
        