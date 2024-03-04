import json
import random
from datetime import datetime, timedelta

# Function to generate random UK postal codes
def generate_postcode():
    letters = [chr(random.randint(65, 90)) for _ in range(2)]
    numbers = [str(random.randint(0, 9)) for _ in range(2)]
    return ''.join(letters) + ''.join(numbers) + ' ' + ''.join([str(random.randint(0, 9)) for _ in range(1)])

# Function to generate random transactions for a credit card
def generate_credit_card_transactions():
    transactions = []
    current_date = datetime(2020, 1, 1)
    last_payment_date = 0  # Initialize last payment date
    for i in range(300):
        transaction_date = current_date.strftime('%Y-%m-%d')
        amount = round(random.uniform(-100, -1), 2)
        if amount < 0  and last_payment_date < 30:  # Expense transaction
            description = random.choice(["Groceries", "Transportation", "Shopping", "Food & Drink", "Dining Out", "Bills & Utilities", "Entertainment"])
            category = description
            merchant = {
                "address": {
                "address": str(random.randint(1, 100)) + " " + random.choice(["High Street", "Main Street", "Elm Street", "Park Avenue", "Station Road"]),
                "city": "London",
                "country": "GB",
                "latitude": round(random.uniform(51.45, 51.55), 4),
                "longitude": round(random.uniform(-0.25, 0.1), 4),
                "postcode": generate_postcode(),
                "region": "Greater London"
            },
            "created": "2010-01-01T00:00:00Z",
            "group_id": "grp_00008zIcpbBOaAr7TTP3sv",
            "id": "merch_" + ''.join([random.choice("0123456789abcdef") for _ in range(22)]),
            "logo": "https://example.com/merchant_logo.jpg",
            "emoji": random.choice(["🛒", "⛽", "📦", "☕️", "🍗", "🏪", "🎥", "🥪", "👗", "🚗", "🍔"]),
            "name": random.choice(["Tesco", "BP", "Amazon", "Starbucks", "Nando's", "Cinema", "Subway", "H&M", "Uber", "McDonald's"]),
            "category": random.choice(["grocery_store", "fuel_station", "online_retail", "coffee_shop", "restaurant", "entertainment", "fashion_store", "transportation"])
            }
            last_payment_date += 1
        else:  # Payment transaction
            amount = +2000  # Pay off the credit card in full
            description = "Credit Card Payment"
            category = "Payment"
            merchant = None
            last_payment_date = 0  # Update last payment date
        transactions.append({
            "transaction_id": "txn" + str(i + 1).zfill(3),
            "date": transaction_date,
            "amount": amount,
            "description": description,
            "category": category,
            "merchant": merchant
        })
        current_date += timedelta(days=random.randint(3, 5))
    return transactions

# Generate transactions for the credit card
credit_card_data = {
    "account": {
        "card_number": "1234567812345678",
        "expiry_date": "12/28",
        "card_holder": "John Doe",
        "credit_limit": 5000.00,
        "currency": "GBP"
    },
    "transactions": generate_credit_card_transactions()
}

# Save to JSON file
with open('SimulatedFinanceData/credit_card_transactions.json', 'w') as file:
    json.dump(credit_card_data, file, indent=4)

print("JSON file generated successfully.")
