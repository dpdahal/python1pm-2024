print('=================Computer Bazar===============')
print('1. Dell(Rs:20000)   2. Toshiba(Rs:30000)  3. MAC(RS:50000)')
dell_price=0
toshiba_price=0
mac_price=0
product_name=""
quantity=0
option = int(input('Enter your choice: '))
if option==1:
    quantity = int(input('Enter quantity: '))
    dell_price=20000*quantity
    product_name='Dell'
elif option==2:
    quantity = int(input('Enter quantity: '))
    toshiba_price=30000*quantity
    product_name='Toshiba'
elif option==3:
    quantity = int(input('Enter quantity: '))
    mac_price=50000*quantity
    product_name='MAC'
else:
    print('Invalid option')
    exit()
total = dell_price+toshiba_price+mac_price
delivery_price=0
print("Delivery: 1. Home(RS: 1000)  2.Pickup(Free)")
delivery_option = int(input('Enter delivery option: '))
if delivery_option==1:
    delivery_price=1000
plastic_bag=0
bag_price=0
gift_box=0
print("1. Plastic(Rs:1000) 2. Bag(Rs: 2000)  3. Gift box(Rs: 5000)")
packing_option = int(input('Enter packing option: '))
if packing_option==1:
    plastic_bag=1000
elif packing_option==2:
    bag_price=2000
elif packing_option==3:
    gift_box=5000
tax_amount=0
print("1. KTM(RS:13% TAX) 2. BKT(RS: 0% TAX) 3. LTP(RS: 0% TAX)")
tax_option = int(input('Enter tax option: '))
if tax_option==1:
    tax_amount=total*0.13
grand_total = total+delivery_price+plastic_bag+bag_price+gift_box+tax_amount
print('=================Invoice====================')
print('Product name: ',product_name)
print('Quantity: ',quantity)
print('Total: ',total)
print('Delivery: ',delivery_price)
print('Packing: ',plastic_bag+bag_price+gift_box)
print('Tax: ',tax_amount)
print("Grand total: ",grand_total)