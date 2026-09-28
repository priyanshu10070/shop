print("===== SHOP STOCK MANAGER =====")

stock = {}

command = input("Enter command (START / END): ")

if command.upper() == "START":

    print("Shop has started!")

    while True:

        print("\n===== MENU =====")
        print("1. Add Stock")
        print("2. View Stock")
        print("3. Record Sale")
        print("4. Refill Shelf")
        print("5. End Day")

        choice = input("Enter your choice: ")

        # ADD STOCK
        if choice == "1":

            product = input("Enter product name: ")
            quantity = int(input("Enter total quantity received: "))
            capacity = int(input("Enter shelf capacity: "))
            shelf = int(input("Enter quantity placed on shelf: "))
            minimum = int(input("Enter minimum shelf stock: "))

            if shelf > quantity:
                print("Shelf quantity cannot be greater than total stock!")

            elif shelf > capacity:
                print("Shelf quantity cannot be greater than shelf capacity!")

            else:

                back_stock = quantity - shelf

                stock[product] = {
                    "quantity": quantity,
                    "capacity": capacity,
                    "shelf": shelf,
                    "back_stock": back_stock,
                    "minimum": minimum
                }

                print("Stock added successfully!")

        # VIEW STOCK
        elif choice == "2":

            print("\n===== CURRENT STOCK =====")

            if len(stock) == 0:

                print("No stock available.")

            else:

                for product, details in stock.items():

                    print("\nProduct:", product)
                    print("Total stock:", details["quantity"])
                    print("Shelf:", details["shelf"], "/", details["capacity"])
                    print("Back stock:", details["back_stock"])
                    print("Minimum shelf stock:", details["minimum"])

                    if details["shelf"] == 0:

                        print("🔴 SHELF EMPTY!")

                        if details["back_stock"] > 0:
                            print("💡 Refill available!")

                    elif details["shelf"] <= details["minimum"]:

                        print("🟡 LOW STOCK!")

                        refill = details["capacity"] - details["shelf"]

                        if refill <= details["back_stock"]:
                            print("💡 Suggested refill:", refill)

                    else:

                        print("🟢 STOCK OK")

        # RECORD SALE
        elif choice == "3":

            product = input("Enter product sold: ")

            if product in stock:

                sold = int(input("Enter quantity sold: "))

                if sold <= stock[product]["shelf"]:

                    stock[product]["shelf"] -= sold
                    stock[product]["quantity"] -= sold

                    print("Sale recorded successfully!")

                    if stock[product]["shelf"] == 0:

                        print("🔴 WARNING: SHELF IS EMPTY!")

                        if stock[product]["back_stock"] > 0:
                            print("💡 You can refill the shelf.")

                    elif stock[product]["shelf"] <= stock[product]["minimum"]:

                        print("🟡 WARNING: LOW STOCK!")

                        refill = stock[product]["capacity"] - stock[product]["shelf"]

                        if refill <= stock[product]["back_stock"]:
                            print("💡 Suggested refill:", refill)

                else:

                    print("Not enough products on shelf!")

            else:

                print("Product not found!")

        # REFILL SHELF
        elif choice == "4":

            product = input("Enter product to refill: ")

            if product in stock:

                refill = int(input("Enter quantity to put on shelf: "))

                available = stock[product]["back_stock"]
                space = stock[product]["capacity"] - stock[product]["shelf"]

                if refill <= available and refill <= space:

                    stock[product]["shelf"] += refill
                    stock[product]["back_stock"] -= refill

                    print("Shelf refilled successfully!")

                else:

                    print("Cannot refill.")
                    print("Back stock available:", available)
                    print("Space on shelf:", space)

            else:

                print("Product not found!")

        # END DAY
        elif choice == "5":

            print("\n===== END OF DAY REPORT =====")

            for product, details in stock.items():

                print("\nProduct:", product)
                print("Total remaining:", details["quantity"])
                print("Shelf remaining:", details["shelf"])
                print("Back stock:", details["back_stock"])

                if details["shelf"] == 0:

                    print("🔴 RESTOCK REQUIRED!")

                elif details["shelf"] <= details["minimum"]:

                    print("🟡 LOW STOCK!")

                else:

                    print("🟢 OK")

            print("\n===== SHOP CLOSED =====")
            print("Shop has ended!")

            break

        else:

            print("Invalid choice!")

else:

    print("Invalid command!")