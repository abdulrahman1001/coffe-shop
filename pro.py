order = {}
total_item=[]
hot_drinks = {"Coffee": 20, "Tea": 15, "Hot Chocolate": 25}
cold_drinks = {"Soda": 10, "Iced Tea": 15, "Smoothie": 30}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheesecake": 70}

while True:
    print('Welcome\n1. Hot Drinks\n2. Cold Drinks\n3. Desserts')
    choice = input('Enter the number for your choice (Press Enter to exit): ')

    if choice == "":
        break

    if int(choice) == 1:
        print('-' * 20)
        for i, (name, price) in enumerate(hot_drinks.items(), start=1):
            print(f'{i}. {name}: {price} riyal')
        item = int(input('Enter the item number: '))
        quantity = int(input('Enter the number of items: '))
        if item == 1:
            order.update({"Coffee": {"price": 20, "quantity": quantity}})
        elif item == 2:
            order.update({"Tea": {"price": 15, "quantity": quantity}})
        elif item == 3:
            order.update({"Hot Chocolate": {"price": 25, "quantity": quantity}})

    elif int(choice) == 2:
        print('-' * 20)
        for i, (name, price) in enumerate(cold_drinks.items(), start=1):
            print(f'{i}. {name}: {price} riyal')
        item = int(input('Enter the item number: '))
        quantity = int(input('Enter the number of items: '))
        if item == 1:
            order.update({"Soda": {"price": 10, "quantity": quantity}})
        elif item == 2:
            order.update({"Iced Tea": {"price": 15, "quantity": quantity}})
        elif item == 3:
            order.update({"Smoothie": {"price": 30, "quantity": quantity}})

    elif int(choice) == 3:
        print('-' * 20)
        for i, (name, price) in enumerate(desserts.items(), start=1):
            print(f'{i}. {name}: {price} riyal')
        item = int(input('Enter the item number: '))
        quantity = int(input('Enter the number of items: '))
        if item == 1:
            order.update({"Ice Cream": {"price": 50, "quantity": quantity}})
        elif item == 2:
            order.update({"Chocolate Cake": {"price": 60, "quantity": quantity}})
        elif item == 3:
            order.update({"Cheesecake": {"price": 70, "quantity": quantity}})

    else:
        print('Invalid choice. Please enter a valid number.')

print('---'*10)
print('your order is:')
print('---'*10)


for item in order:
    print(f'Item: {item}')
    price = order[item]['price']
    quantity = order[item]['quantity']
    print(f'Price: {price}')
    print(f'Quantity: {quantity}')
    total = price * quantity
    print(f'Total: {total}')
    total_item.append(total)
    print('-'*20)
print('total order is:',sum(total_item))
    

            
        
        
    






            
    