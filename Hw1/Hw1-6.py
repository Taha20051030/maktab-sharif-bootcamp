products = {}
while True:
    inp = input("Please enter  the desired command: add, sell, search, show, save, report, exit\n")
    if inp == "add":
        name = input("Please enter the product name.\n")
        quantity = int(input("Please enter the product quantity.\n"))
        products[name] = products.get(name, 0) + quantity
    elif inp == "sell":
        name = input("Please enter the product name.\n")
        quantity = int(input("Please enter the product quantity.\n"))
        if name not in products:
            print("Product not found.")
        elif products[name] < quantity:
            print("Insufficient funds")
        else:
            products[name] -= quantity
            print("The sales transaction was successfully completed.")
            if products[name] == 0:
                del products[name]
    elif inp == "search":
        name = input("Enter the product name.\n")
        if name in products:
            print(products[name])
        else:
            print("Product does not exist.")
    elif inp == "show":
        print(f"name    quantity")
        for name, quantity in products.items():
            print(f"{name}  {quantity}")
    elif inp == "save":
        with open("report.txt", 'w') as f:
            for name, quantity in products.items():
                f.write(f"{name} - {quantity}\n")
            
    elif inp == 'report':
        print(f"Number of items in stock : {len(products)}")
        count = 0
        for i in products:
            count += products[i]
        print(f"Total inventory of all items : {count}")
        Max = max(products.values())
        Min = min(products.values())
        M = []
        m = []
        for i in products:
            if products[i] == Max:
                M.append(i)
            if products[i] == Min:
                m.append(i)
        print(f"Items with the highest stock level:")
        for i in M:
            print(i)
        print(f"Item with the lowest stock level:")
        for i in m:
            print(i)
    
    
    elif inp == 'exit':
        break
    else:
        print("The command is invalid.")