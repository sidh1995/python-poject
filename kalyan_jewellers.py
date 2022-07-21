print('***************************KALYAN JEWELLERS***********************************************')


name = input('ENTER YOUR NAME:')
mobile_number = int(input('ENTER YOUR MOBILE_NUMBER:'))
gender = input('ENTER YOUR GENDER:')
age = int(input('ENTER YOUR AGE:'))
qty = float(input('ENTER YOUR QUNTITY:'))
product_name = input('WHICH PRODUCT DO YOU WANT:')


current_price = 4900.0  # 1 gram price
making_charge = 600.0
# buying mande than 10 gram making charge increase by 10%
total_amt2 = qty * current_price

print("\n\n-------------------------- Invoice --------------------------")
print(f"Name : {name}")
print(f"Mobile number : {mobile_number}")
print(f"Gender : {gender}")
print(f"Age : {age}")
print(f"Product : {product_name}")
print(f"Quantity : {qty}")
print(f"Current price : {current_price}")


if qty > 10:
    add_makingcharge = (making_charge * 10) / 100
    new_makingcharge = making_charge + add_makingcharge
    print(f'Making charge:{new_makingcharge}')
    total_amt = total_amt2 + new_makingcharge
    print(f'total ammount:{total_amt}')
    if gender == 'male' and age > 60:
        if total_amt > 20000:
            print("-------------------------------------------------")
            discount = (total_amt * 10) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 500000:
            print("-------------------------------------------------")
            discount = (total_amt * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt * 20) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
    elif gender == 'male' and age < 60:
        if total_amt > 200000:
            print("-------------------------------------------------")
            discount = (total_amt * 5) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 500000:
            print("-------------------------------------------------")
            discount = (total_amt * 10) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
    elif gender == 'female' and age > 60:
        if total_amt > 200000:
            print("-------------------------------------------------")
            discount = (total_amt * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 500000:
            print("-------------------------------------------------")
            discount = (total_amt * 20) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt * 25) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
    elif gender == 'female' and age < 60:
        if total_amt > 200000:
            print("-------------------------------------------------")
            discount = (total_amt * 10) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 500000:
            print("-------------------------------------------------")
            discount = (total_amt * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        elif total_amt > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt * 20) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
else:
    print(f'Making charges:{making_charge}')
    if gender == 'male' and age > 60:
        if qty > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 20) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 500000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 200000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 10) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'Net amount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'net amount :{final_payout}')
    elif gender == 'male' and age < 60:
        if qty > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 500000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 10) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 200000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 5) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
    elif gender == 'female' and age > 60:
        if qty > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 25) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 500000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 20) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 200000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
    elif gender == 'female' and age < 60:
        if qty > 1000000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 20) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 500000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 15) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        elif qty > 200000:
            print("-------------------------------------------------")
            discount = (total_amt2 * 10) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (total_amt2 * 18) / 100
            print(f'GST:{gst}')
            final_payout = total_amt2 + gst
            print(f'Net amount:{final_payout}')
        else:
            discount = (total_amt2 * 0) / 100
            print(f'discount:{discount}')
            dis_amt = total_amt2 - discount
            print(f'dis ammount:{dis_amt}')
            gst = (dis_amt * 18) / 100
            print(f'GST:{gst}')
            final_payout = dis_amt + gst
            print(f'Net amount:{final_payout}')
