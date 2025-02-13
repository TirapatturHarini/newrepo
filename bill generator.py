items=[]
total_items=0
while True:
    item=input("Enter item type quit to finish:")
    if item.lower()=="quit":
        break
    qty=int(input("No.of items:"))
    price=float(input("Enter the Price:"))
    items.append((item,qty,price))
    sum_item=qty*price
    total_items=total_items+sum_item
tax=total_items*0.05
print("-----Bill Receipt----")
print(" Item    ", "Qty","Price")
for i in items:
    print(i[0],  i[1],  i[2])
print("Total Amount: ",total_items)
print("GST (5%): ",tax)
print(" Thankyou Visit Again....")