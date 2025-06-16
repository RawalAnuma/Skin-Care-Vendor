def update_file(products_list):
    '''
    Updates the 'product_details.txt' file with current product data.
    Converts the displayed price back to original by dividing by 3.
    
    '''
    file_details = open("product_details.txt", "w") # Open product_details.txt file in write mode
    
    for i in range(1, len(products_list)):
        products = products_list[i]
        line = f"{products[1]}, {products[2]}, {int(products[3])}, {int(products[4])//3}, {products[5]}"
        file_details.write(f"{line}\n")
        
    print("File updated successfully")




def generate_purchased_products_invoice(purchased_product):
    '''
    This function generates a detailed invoice in text file for purchased products.
    It includes customer name, phone number, purchase details and total cost with 13% VAT.
    
    '''
    import datetime
    
    while True:
        '''
        Here, 
        strip() removes unwanted spaces at the beginning or end.
        customer_name.split() breaks the name into individual words.
        all(word.isalpha() for word in customer_name) ensures each word is fully alphabetic.
        '''
        customer_name = input("Enter customer's name: ").strip().title()    
        if all(word.isalpha() for word in customer_name.split()):
            break
        else:
            print("Invalid name! Please use only letters and spaces!")
            
    while True:
        phone_number = input("Enter 10-digit phone number: ").strip()
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Invalid phone number! Please enter 10-digit numeric phone number!")
    
    
    # Generate timestamped file name       
    date_of_transaction = str(datetime.datetime.now().replace(microsecond=0)).replace(":", "_")
    name_of_file = f"{customer_name.split()[0]}_{date_of_transaction}.txt"
    total_cost = 0
    
    file_details = open(name_of_file, "w")
    file_details.write("\n =====================================    Purchased Product Invoice    =========================================\n")
    file_details.write(f"Customer Name: {customer_name}\n")
    file_details.write(f"Phone Number: {phone_number}\n")
    file_details.write(f"{'Date & Time:':>85} {date_of_transaction}\n")
    file_details.write("Products Purchased:\n")
    file_details.write("-" * 120 + "\n")
    file_details.write(f"{'Product Name':^30}|{'Product Brand':^25}|{'Total Quantity(Paid+Free)':^35}|{'Price(per unit)':^25}\n")
    file_details.write("-" * 120 + "\n")
    
    for product in purchased_product:
        product_name, product_brand, paid_quantity, free_quantity, price_per_unit = product
        cost_of_product = paid_quantity * price_per_unit
        total_cost += cost_of_product
        file_details.write(f"{product_name:^30}{product_brand:^25}{str(paid_quantity)+'+'+str(free_quantity):^35}{price_per_unit:^25}\n")
    
    # Calculate VAT amount and final total cost
    vat_amount = total_cost * 0.13
    total_cost_with_vat = total_cost + vat_amount
    file_details.write("-" * 120 + "\n")
    file_details.write(f"{'Total Cost(excluding free products):':>95} Rs. {total_cost:>10.2f}\n")
    file_details.write(f"{'VAT (13%):':>95} Rs. {vat_amount:>10.2f}\n")
    file_details.write("-" * 120 + "\n")
    file_details.write(f"{'Total Cost(Including VAT):':>95} Rs. {total_cost_with_vat:>10.2f}\n")
    file_details.write("=" * 120 + "\n")
    file_details.close()
    
    file_details = open(name_of_file, "r")
    lines = file_details.readlines()
    for line in lines:
        print(line)
    file_details.close()
    
    print(f"\nBill generated successfully: {name_of_file}")
    





def generate_add_products_invoice(restocked_product):
    '''
    Generates a vendor invoice for restocked products.
    It includes vendoe name, phone number, products restocked and total cost.
    
    '''
    import datetime
    
    # Get vendor's name and validate it
    while True:
        vendor_name = input("Enter vendor's name: ").strip().title()
        if all(word.isalpha() for word in vendor_name.split()):
            break
        else:
            print("Invalid name! Please use only letters and spaces!")
    
    # Get phone number and validate it       
    while True:
        phone_number = input("Enter 10-digit phone number: ").strip()
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Invalid phone number! Please enter 10-digit numeric phone number!")
    
    # Create a filename with timestamp
    date_of_transaction = str(datetime.datetime.now().replace(microsecond=0)).replace(":", "_")
    name_of_file = f"{vendor_name.split()[0]}_{date_of_transaction}.txt"
    total_cost = 0
    
    # Write invoice details
    file_details = open(name_of_file, "w")
    file_details.write("\n========================================    Restocked Product Invoice      ================================================\n")
    file_details.write(f"Vendor Name: {vendor_name}\n")
    file_details.write(f"Phone Number: {phone_number}\n")
    file_details.write(f"{'Date & Time:':>85} {date_of_transaction}\n")
    file_details.write("Products added:\n")
    file_details.write("-" * 120 + "\n")
    file_details.write(f"{'Product Name':^30}|{'Product Brand':^25}|{'Total Restock Quantity':^35}|{'Price(per unit)':^25}\n")
    file_details.write("-" * 120 + "\n")
    
    for product in restocked_product:
        product_name, product_brand, paid_quantity, price_per_unit = product
        cost_of_product = paid_quantity * (price_per_unit // 3)
        total_cost += cost_of_product
        file_details.write(f"{product_name:^30}{product_brand:^25}{str(paid_quantity):^35}{price_per_unit // 3:^25}\n")
        
    file_details.write("-" * 120 + "\n")
    file_details.write(f"{'Total Cost:':>95} Rs. {total_cost:>10.2f}\n")
    file_details.close()
    
    file_details = open(name_of_file, "r")
    lines = file_details.readlines()
    for line in lines:
        print(line)
    file_details.close()
    
    print(f"\nBill generated successfully: {name_of_file}")
    
    
    
    