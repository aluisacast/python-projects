# 04 Prove: Milestone - Meal Price Calculator
print('\nWelcome to the Meal Price Calculator! Only input numbers please.')
price_child = float(input("\nWhat is the price of a child's meal? "))
price_adult = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))

subtotal = (price_child * children) + (price_adult * adults)
sales_tax  = subtotal * (tax / 100)
total = subtotal + sales_tax

descuento = input('\nDo you have a discount? (yes/no) ')

if descuento == 'yes' :
    discount = float(input('What is your discount percentage? '))
    propina=input('\nDo you want to leave a tip? (yes/no) ')
    if propina.lower() == 'yes' :

        tip = float(input('What is the percentage of tip you would like to give? '))
        total_discount = total * (discount / 100)
        total_tip = total * (tip / 100)
        total_to_pay = total + total_tip - total_discount

        print(f'\nSubtotal: ${"{:.2f}" .format(subtotal)}')
        print(f'Sales Tax: ${"{:.2f}" .format(sales_tax)}')
        print(f'Discount: ${"{:.2f}" .format(total_discount)}')
        print(f'Tip: ${"{:.2f}" .format(total_tip)}')
        print(f'Total: ${"{:.2f}" .format(total_to_pay)} \n')
        amount = int(input('What is the payment amount? '))
        change = amount - total_to_pay
        print(f'Change: ${"{:.2f}" .format(change)} \n')

    if propina.lower() == 'no' :
        total_discount = total * (discount / 100)
        total_to_pay = total - total_discount
        print(f'\nSubtotal: ${"{:.2f}" .format(subtotal)}')
        print(f'Sales Tax: ${"{:.2f}" .format(sales_tax)}')
        print(f'Discount: ${"{:.2f}" .format(total_discount)}')
        print(f'Total: ${"{:.2f}" .format(total_to_pay)}\n')

        amount = int(input('What is the payment amount? '))
        change = amount - total_to_pay
        print(f'Change: ${"{:.2f}" .format(change)} \n')

if descuento.lower() == 'no' :
    propina=input('\nDo you want to leave a tip? (yes/no) ')
    if propina == 'yes' :

        tip = float(input('What is the persentage of tip you would like to give? '))
        total_tip = total * (tip / 100)
        total_to_pay = total + total_tip

        print(f'\nSubtotal: ${"{:.2f}" .format(subtotal)}')
        print(f'Sales Tax: ${"{:.2f}" .format(sales_tax)}')
        print(f'Tip: ${"{:.2f}" .format(total_tip)}')
        print(f'Total: ${"{:.2f}" .format(total_to_pay)} \n')
        amount = int(input('What is the payment amount? '))
        change = amount - total_to_pay
        print(f'Change: ${"{:.2f}" .format(change)} \n')


    if propina.lower() == 'no':
        print(f'\nSubtotal: ${"{:.2f}" .format(subtotal)}')
        print(f'Sales Tax: ${"{:.2f}" .format(sales_tax)}')
        print(f'Total: ${"{:.2f}" .format(total)}\n')

        amount = int(input('What is the payment amount? '))
        change = amount - total
        print(f'Change: ${"{:.2f}" .format(change)} \n')
