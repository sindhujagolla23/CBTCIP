from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_receipt(transaction_id, customer_name, amount, date, items):
    file_name = f"receipt_{transaction_id}.pdf"  # Ensure the file has a .pdf extension
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)

    # Title
    c.drawString(200, 750, "Payment Receipt")

    # Transaction details
    c.drawString(50, 700, f"Transaction ID: {transaction_id}")
    c.drawString(50, 680, f"Customer Name: {customer_name}")
    c.drawString(50, 660, f"Amount: ${amount:.2f}")
    c.drawString(50, 640, f"Date: {date}")

    # Item details
    c.drawString(50, 600, "Items:")
    y = 580
    for item in items:
        c.drawString(60, y, f"{item['description']} - ${item['price']:.2f}")
        y -= 20

    # Ensure the footer is on the same page
    if y < 120:
        y = 120

    # Footer
    c.drawString(50, y, "Thank you for your purchase!")

    c.save()
    print(f"Receipt saved as {file_name}")

    # Debugging: Check the file extension and type
    if os.path.exists(file_name):
        print(f"File '{file_name}' exists.")
        if file_name.lower().endswith('.pdf'):
            print("File has the correct .pdf extension.")
        else:
            print("File does not have the correct .pdf extension.")
    else:
        print(f"File '{file_name}' does not exist.")

# Example usage
transaction_id = "123456"
customer_name = "John Doe"
amount = 250.75
date = "2024-07-26"
items = [
    {"description": "Item 1", "price": 100.00},
    {"description": "Item 2", "price": 150.75},
]

create_receipt(transaction_id, customer_name, amount, date, items)
