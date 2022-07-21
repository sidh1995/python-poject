mobile_store = {}
orderList = {}

menu = '''
            MENU

    press-1 for Product Maneger
    press-2 for Customer

'''

option = True
while option:
    print(menu)
    role = int(input('\n\tEnter your role (1/2) : '))

    if role == 1:
        manager_status = True
        while manager_status:
            specification = {}
            print('\n\n\tPRODUCT MANAGER')

            product_name = input('\n\tEnter product name:')
            model_num = input('\tEnter model number:')
            colour = input('\tEnter colour name:')
            qty = int(input('\tEnter qty:'))
            price = int(input('\tEnter price:'))

            specification['model'] = model_num
            specification['colour'] = colour
            specification['qty']  = qty
            specification['price'] = price 

            mobile_store[product_name] = specification

            for k in mobile_store.keys():
                print('\n\n\t------------------------------------------')
                print(f'\tProduct : {k}')
                print('\t------------------------------------------')
                print('\tModel : ' + mobile_store[k]['model'])
                print('\tColour : ' + mobile_store[k]['colour'])
                print('\tQty : ' + str(mobile_store[k]['qty']))
                print('\tPrice : ' + str(mobile_store[k]['price']))

            if input("\n\tWanna add more items as manager? press 'y' for yes and press'n' for no : ") == 'n':
                manager_status = False
    elif role == 2:
        customer_status = True
        while customer_status:
            orderLine = {}
            print("\n\n\tCUSTOMER")
            product_name = input('\n\tEnter product name:')
            colour = input('\tEnter colour name:')
            qty = int(input('\tEnter qty:'))

            products = mobile_store.keys()
            if (product_name in products) and (mobile_store[product_name]['qty'] > qty) and (colour == mobile_store[product_name]['colour']):
                orderLine["color"] = colour
                orderLine["qty"] = qty

                orderList[product_name] = orderLine
                # print(f"\n\t{orderList}")

                mobile_store[product_name]['qty'] -= qty # mobile_store[product_name]['qty'] = mobile_store[product_name]['qty'] - qty
            else:
                print("\n\tThe product you are looking for is not available")

            for k in orderList.keys():
                print('\n\n\t------------------------------------------')
                print(f'\tProduct : {k}')
                print('\t------------------------------------------')
                print('\tColor : ' + str(orderList[k]['color']))
                print('\tQty : ' + str(orderList[k]['qty']))


            if input("\n\tWanna buy some more products? press 'y' for yes and press'n' for no : ") == 'n':
                customer_status = False
    else:
        print("\n\tEnter valid role")

    if input("\n\tWanna switch roles? press 'y' for yes and press 'n' for no : ") == 'n':
        option = False