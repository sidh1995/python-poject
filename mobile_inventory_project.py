mobile_store = {}

menu = '''
            MENU

    press 1 for product maneger
    press2 for customer
'''

status = True
while status:
    specification = {}
    print(menu)
    role = int(input('enter your role (1/2) : '))
    if role == 1:
        print('product maneger')
        product_name = input('enter product name:')
        model_num = input('enter model number:')
        colour = input('enter colour name:')
        qty = int(input('enter qty:'))
        price = int(input('enter price:'))


        specification['model'] = model_num
        specification['colour'] = colour
        specification['qty']  = qty
        specification['price'] = price 

        mobile_store[product_name] = specification

        print(mobile_store)


        choice = input("do you want to continue: press 'y' for yes and press'n' for no:")
        if choice == 'n' or choice == 'no':
            status = False

        for k in mobile_store.keys():
            print('------------------------------------------')
            print(f'product : {k}')
            print('----------------------')
            print('MODEL : ' + mobile_store[k]['model'])
            print('COLOUR : ' + mobile_store[k]['colour'])
            print('QTY : ' + str(mobile_store[k]['qty']))
            print('PRICE : ' + str(mobile_store[k]['model']))
    
    elif role == 2:
        print('couster')
    
    



