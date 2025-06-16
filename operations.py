import read
import write

def purchase_products(products_list):
    '''
    Allows a user to purchase products from the product list.
    It displays available products, accepts user input for selection and quantity.
    It also applies a promotional sales "buy three get one free", updates the stock and generate an invoice of pruchased products.
    '''
    read.product_display(products_list)
    purchased_product = []
    
    while True:
        try:
            serial_number = int(input("Enter the S.N number of the product you want to purchase: "))    # Ask user for product serial number
            if serial_number < 1 or serial_number >= len(products_list):    # validate the serial number
                print("Invalid S.N. Please enter a valid S.N!")
            else:
                while True:
                    try:
                        quantity_to_purchase = int(input("Enter the quantity you want to purchase: "))  # Ask user for the quantity to puchase
                        if quantity_to_purchase > 0:
                            free_quantity = quantity_to_purchase // 3   # Calculate free quantity
                            total_quantity = quantity_to_purchase + free_quantity
                            available_quantity = int(products_list[serial_number][3])   # Get available quantity from product list
                            if available_quantity > total_quantity: # Chcek if enough stock is available or not
                                products_list[serial_number][3] = available_quantity - total_quantity
                                print(f"Purchase successful! You received {free_quantity} extra for free!!")
                                choosed_product = products_list[serial_number]  #Get the selected product details
                                purchased_product.append([
                                    choosed_product[1], choosed_product[2], quantity_to_purchase,
                                    free_quantity, choosed_product[4]
                                ])
                                write.update_file(products_list)
                                break
                            else:
                                print("Sorry! Not enough quantity available!")
                        else:
                            print("Please enter a valid quantity more than 0!")
                    except:
                        print("Please enter a valid quantity!")
                while True:
                    try:
                        # Ask user whether to continue purchasing or proceed to billing
                        purchase_option = int(input("\nEnter 1 if you want to continue purchasing\nEnter 0 if you want to proceed to billing\nWhat do you want to do? "))
                        if purchase_option == 1:
                            break   # Continue the purchase loop
                        elif purchase_option == 0:
                            print("Generating Bill....")
                            write.generate_purchased_products_invoice(purchased_product)
                            write.update_file(products_list)
                            return  #Exit the function
                        else:
                            print("Please choose either 1 or 0")
                    except:
                        print("Please enter valid option!")
        except:
            print("Please enter a valid S.N!")
            
            
            

def add_products(products_list):
    '''
    Allows a user to restock products to the product list.
    It displays current stock, accepts user input for the product and quantity to add.
    Then, it updates the stock and generates an invoice of the products restocked.
    
    '''
    read.product_display(products_list) # Display the list of current products
    restocked_product = []  # Initialize an empty list to keep track of restocked products
    
    while True:
        try:
            serial_number = int(input("Enter the S.N number of the product you want to add: ")) # Ask user for the product serial number
            if serial_number < 1 or serial_number > len(products_list): # Validate the serial number
                print("Invalid S.N. Please enter a valid S.N!")
            else:
                while True:
                    try:
                        quantity_to_add = int(input("Enter the quantity you want to add: "))    # ASk for quantity to restock
                        if quantity_to_add > 0:
                            total_quantity = int(products_list[serial_number][3])   # Get current quantity
                            products_list[serial_number][3] = total_quantity + quantity_to_add  # Update with restocked quantity
                            print(f"Product added succesfully")
                            choosed_product = products_list[serial_number]  # Get selected product details
                            # Append restocked item details to list
                            restocked_product.append([
                                choosed_product[1], choosed_product[2],
                                quantity_to_add, choosed_product[4]
                            ])
                            write.update_file(products_list)
                            break
                        else:
                            print("Please enter a valid quantity!")
                    except:
                        print("Please enter a valid quantity!")
                while True:
                    try:
                        # Ask if user wants to continue restocking or proceed to billing
                        restock_option = int(input("\nEnter 1 if you want to restock more\nEnter 0 if you want to proceed to billing\nWhat do you want to do? "))
                        if restock_option == 1:
                            break
                        elif restock_option == 0:
                            print("Generating Bill....")
                            write.generate_add_products_invoice(restocked_product)
                            write.update_file(products_list)
                            return
                        else:
                            print("Please choose either 1 or 0")
                    except:
                        print("Please enter valid option!")
        except:
            print("Please enter a valid S.N!")
