# Autor: Ana Luisa Castañeda Garce
# Shopping Cart Program

items = []
prices =[]
menu = 1

print('\nWelcome to the Shopping Cart Program!')




while menu != '6' :

    print('\nMenu: \n1. Add item to your cart \n2. View cart \n3. Remove an item \n4. Change the price or name of an item \n5. Computer total \n6. Quit')
    menu = input('\nPlease enter the number of the action you want to do. ')
    
    if menu == '1' : #Add to cart
        print()
        product = input('What is the name of the item you would like to add? ')
        cost = float(input('What is the price of the item? '))
        print()
        print ("\033[1m{}\033[00m" .format(product.capitalize()),end='')
        print(f' has been added to your cart with a price of ${cost:.2f}')

        items.append(product.lower())
        prices.append(cost)

        print('\n-----------------------------------------------')

    elif menu == '2' : # View cart

        print('\nThis is the content of your shopping cart.')

        for i in range(len(items)) :
            n = i + 1
            price = prices[i]
            print(f'{n}. {items[i]} - ${price:.2f}')
        
        print('\n-----------------------------------------------')


    elif menu == '3' : # Remove an item
        if (len(items) == 0) and (len(prices) == 0) :
            print('\nYour cart is empty.')
        else : 
            print('\nThis is the content of your shopping cart.')

            for i in range(len(items)) :
                n = i + 1
                price = prices[i]
                print(f'{n}. {items[i]} - ${price:.2f}')

            print()
            remove = int(input('What is the number of the item you want to remove? '))
            
            r = remove - 1
            items.pop(r)
            prices.pop(r)

            print(f'We removed {items[remove]} from your cart')
        
            print('\nThis is the new content of your shopping cart.')

            for i in range(len(items)) :
                n = i + 1
                price = prices[i]
                print(f'{n}. {items[i]} - ${price:.2f}')  

        print('\n-----------------------------------------------')

    elif menu == '4' : #Change the price or name of an item

        if (len(items) == 0) and (len(prices) == 0) : 
            print('\nYour cart is empty.')
        else :
            print('\nThis is the content of your shopping cart.')

            for i in range(len(items)) :
                n = i + 1
                price = prices[i]
                print(f'{n}. {items[i]} - ${price:.2f}')

            print()
            change = int(input('What is the number of the item you want to change? '))
            what = input('Do you want to change the NAME, the PRICE or BOTH? ')
            
            c = change - 1
            if what.lower() == 'name' :
                new_name = input('What is the new name for the item? ')
                items[c] = new_name

            elif what.lower() == 'price' :
                new_price = float(input('What is the new price of the item? '))
                prices[c] = new_price

            elif what.lower() == 'both' :
                new_name = input('What is the new name for the item? ')
                items[c] = new_name

                new_price = float(input('What is the new price of the item? '))
                prices[c] = new_price
            

            print('\nThis is the new content of your shopping cart.')

            for i in range(len(items)) :
                n = i + 1
                price = prices[i]
                print(f'{n}. {items[i]} - ${price:.2f}')  

        print('\n-----------------------------------------------')

    elif menu == '5' : # Compute total
        sum = 0
        for price in prices :
            sum += price

        print(f'\nYour total before taxes is: ${sum:.2f}')
        print()
        taxes = input ('Do you want to add taxes(yes/no)? ')
        if taxes.lower() == 'yes' :
            
            tax = float(input('What is your tax rate? '))
            sales_tax  = sum * (tax / 100)
            total = sum + sales_tax
            print(f'\nYour total after taxes is: ${total:.2f}')

        print('\n-----------------------------------------------')

    elif menu == '6' : # Quit
        menu = '6'
    else :
        print('\nThat is not a valid option. \nPlease choose one from the following options.')
    
else :
    print('\nThank you for using the Shopping Cart Program.')
    print('This program was made by', "\033[1m{}\033[00m" .format('Ana Luisa Castañeda.'))
    print('Godbye.\n')