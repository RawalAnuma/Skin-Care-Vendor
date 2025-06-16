def get_choice():
    '''
    Diplays the main menu and asks the user to select one choice.
    It returns the user's menu choice.
    
    '''
    print("""
        1. Show products and it's details
        2. Purchase products
        3. Add products
        4. Exit
        """)
    while True:
        try:
            choice = int(input("What task do you want to do? "))
            return choice   # Return user choice if input is valid 
        except:
            print("Please enter a valid choice\n")
    


def get_details_from_file():
    '''
    Reads product details from the 'product_details.txt' file.
    It returns lines from the file
    
    '''
    file_details = open("product_details.txt", "r") # Open file in read mode
    lines = file_details.readlines()    # Read all lines
    file_details.close()    # Close the file
    return lines


def get_details_of_products():
    '''
    Loads and appends product data from the file into the products list.
    Clears the existing products_list (except the header) amd appends updated data parsed from the file.
    It returns updated products_list with product details.
    '''
    from read import get_details_from_file
    products_list = [["S.N", "Product Name", "Brand Name", "Quantity Available", "Cost Price", "Country of Origin"]]
    del products_list[1:]   # Clears old product data except the header
    lines = get_details_from_file() # Read product lines from file
    for i in range(len(lines)):
        start_line = lines[i].strip()   # Removes whitespace
        product_description = start_line.split(",")
        description_of_each_product = []
        for j in range(len(product_description)):
            if j == 3:
                try:
                    description_of_each_product.append(int(product_description[j].strip()) * 3)
                except:
                    description_of_each_product.append(product_description[j].strip())
            else:
                description_of_each_product.append(product_description[j].strip())
        # Add serial number as the first element and append to product_list
        products_list.append([i + 1] + description_of_each_product)
    return products_list



def product_display(products_list):
    # Display all the product details in a formatted table.
    print("The details of the products are:\n")
    print("-" * 120 + "\n")
    for row in products_list:
        if len(row) < 6:
            continue
        # Print each row in a formatted table layout
        print(f"{(row[0]):<5}|{(row[1]):<20}|{(row[2]):<20}|{(row[3]):<20}|{(row[4]):<20}|{(row[5]):<20}")
        print("-" * 120)


