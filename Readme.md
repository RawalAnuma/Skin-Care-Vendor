Welcome to Skin Care Shop, a Python-based web application for buying and restocking skincare products, with automated customer and supplier invoice generation and simple inventory management.

# Features
1. Browse and purchase skincare products
2. Add, update, and manage inventory
3. Apply promotional offers (e.g., Buy 3 Get 1 Free)
4. Generate customer invoices for each purchase
5. Generate supplier invoices for restocking
6. Store and update product data in a text file
7. User-friendly interface 

# Built With
Python 3

File I/O (for reading/writing product data)

Libraries:

os (for file operations)

datetime (for invoice timestamps)

No complex frameworks required — lightweight and easy to run!

# Project Structure

skin-care-shop/
├── main.py
├── read.py
├── write.py
├── operations.py
├── product_details.txt
├── customer/supplier_invoice.txt
├── README.md


# How to Run
1️. Clone this repository:
git clone https://github.com/your-username/skin-care-shop.git
2️. Navigate to the project directory:
cd skin-care-shop
3️. Run the main Python file:
python main.py
4️. Follow the prompts:

View products

Purchase products

Restock products

Generate and view invoices

# How It Works
Product Data: Stored in product_details.txt

Buying: Calculates discounts and creates a customer invoice with itemized costs and offers

Restocking: Updates stock levels and generates a supplier invoice for records

Invoices: Saved as .txt files for easy printing or sharing

# Contributing
Fork this repository

Create a new branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add new feature')

Push to your branch (git push origin feature/YourFeature)

Open a Pull Request

# License
This project is licensed under the MIT License — you’re free to use and modify it.

# Contact
Author: Anuma Rawal

Email: rawalanuma@gmail.com

GitHub: Rawal Anuma
