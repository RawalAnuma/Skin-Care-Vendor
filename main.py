import read     # 'read' handles reading or displaying tasks
import operations   # 'operations' handles business logic like purchasing products and restocking products

while True:
    choice = read.get_choice()

    if choice == 1:
        read.product_display(read.get_details_of_products())

    elif choice == 2:
        operations.purchase_products(read.get_details_of_products())

    elif choice == 3:
        operations.add_products(read.get_details_of_products())

    elif choice == 4:
        print("Thank you for using program!!")
        break   # Exit the loop and terminate the program

    else:
        print("Invalid choice! Please enter a valid choice between 1 to 4!!")